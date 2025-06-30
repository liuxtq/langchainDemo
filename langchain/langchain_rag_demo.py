from langchain_community.document_loaders import  PyPDFLoader

# 加载文档
loader = PyPDFLoader("刘峰-CN&EN简历.pdf")
pages = loader.load_and_split()
# print(f"第0页：\n{pages[0]}")

# 文档切片
from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=30,
    chunk_overlap=10,
    length_function=len,
    add_start_index=True
)

paragraphs = []
for page in pages:
    paragraphs.extend(text_splitter.create_documents([page.page_content]))
# 文本档向量化&持久化
# from langchain_openai import OpenAIEmbeddings
# from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import os
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
# print(os.getenv("HF_ENDPOINT"))
# db = Chroma.from_documents(paragraphs,OllamaEmbeddings(model="llama3"))
db = Chroma.from_documents(paragraphs,HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"))

# 向量检索
retriever = db.as_retriever()
user_query = "刘峰会日语吗？"
docs = retriever.invoke(user_query)
for doc in docs:
    print(f"{doc.page_content}\n")

# 组装prompt
prompt = f"""
   你是一个问答机器人。
   你的任务是根据下述给定的已知信息回答用户问题。
   确保你的回复完全依据下述已知信息，不要编造答案。
   如果下述已知信息不足以回答用户的问题，请直接回复“我无法回复你的问题”。

   已知信息
   {docs}

   用户问：
   {user_query}

   请用中文回答用户问题。
   """

# 大模型生成回答
from openai import OpenAI

client = OpenAI(
    api_key="sk-f0d8e6d4e9f1436f981daf3f2c12ce76",
    base_url="https://api.deepseek.com/v1"  # 兼容OpenAI的端点
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": prompt}
    ],
    temperature=0, # 采样温度，介于 0 和 2 之间。更高的值，如 0.8，会使输出更随机，而更低的值，如 0.2，会使其更加集中和确定。
    stream=False
)

print(response.choices[0].message.content)