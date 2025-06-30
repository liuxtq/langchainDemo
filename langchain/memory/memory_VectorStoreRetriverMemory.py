import faiss
from langchain.chains.conversation.base import ConversationChain
from langchain.memory import VectorStoreRetrieverMemory
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
embeddings_fn = embeddings.embed_query

# 初始化向量存储
embeddings_size = 1535 # 维度
index = faiss.IndexFlatL2(embeddings_size)
vectorstore = FAISS(embeddings_fn,index,InMemoryDocstore({}),{})

# 向量查找语义相关的信息
retriever = vectorstore.as_retriever(search_kwargs=dict(k=1))
# 相关文档信息放到memory
memory = VectorStoreRetrieverMemory(retriever=retriever)

memory.save_context({"Human":"我最喜欢的食物是披萨"},{"AI":"我很喜欢知道"})
memory.save_context({"Human":"我最喜欢的运动是跑步"},{"AI":"好的，我知道了"})
memory.save_context({"Human":"我最喜欢的运动是足球"},{"AI":"好的，我知道了"})

# 初始化大模型
llm = ChatOpenAI(
    temperature=0.95,
    model="deepseek-chat",
    openai_api_key="sk-f0d8e6d4e9f1436f981daf3f2c12ce76",
    openai_api_base="https://api.deepseek.com/v1"
)
_DEFAULT_TEMPLATE = """
以下是人类和人工智能之间的友好对话。人工智能很健谈，并从起其上下文中提供了许多具体细节。如果人工智能不知道问题的答案。他会如实说他不知道。

之前对话的相关片段：{history}
（如果不相关，则无需使用这些信息）

当前对话：
Human:{input}
AI:
"""


prompt = PromptTemplate(
    input_varaibles=["history","input"],
    template=_DEFAULT_TEMPLATE
)
# print(prompt)

# 初始化链
conv_chain = ConversationChain(llm=llm,prompt=prompt,memory=memory,verbose=True)

#提问
result = conv_chain.predict(input="我喜欢的食物是什么呢？")
print(str(result))


