from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import bs4 # 爬虫

""" 文档链 create_stuff_documents_chain"""

#创建提示模板
prompt = ChatPromptTemplate.from_messages([
    ("system","""根据提供的上下文：{context} \n\n 回答问题：{input}""")
]
)

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    temperature=0.95,
    model="deepseek-chat",
    openai_api_key="sk-f0d8e6d4e9f1436f981daf3f2c12ce76",
    openai_api_base="https://api.deepseek.com/v1"
)

# 构建链，这个链将文档作为输入，并使用之前定义的提示模板和初始化的大模型来生成答案
chain = create_stuff_documents_chain(llm,prompt)
# 加载文档
loader = WebBaseLoader(
    web_path="http://www.npc.gov.cn/npc/c2/c30834/202006/t20200602_306457.html",
    bs_kwargs=dict(parse_only=bs4.SoupStrainer(id="Zoom"))
)
docs = loader.load()
# 分割文档
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=50)
documents = text_splitter.split_documents(docs)
# print(documents)
print(len(documents))

# 执行链
result = chain.invoke({"input":"民事法律行为？","context":documents[:5]})
print(result)
