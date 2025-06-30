from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from torch.backends.mkl import verbose

# 加载html内容为一个文档对象
loader = WebBaseLoader("https://finance.sina.com.cn/tech/roll/2024-09-10/doc-incnqzux8236851.shtml")
docs = loader.load()

# 分割文档
documents = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200).split_documents(docs)

# 向量化
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector = FAISS.from_documents(documents, embeddings)

# 创建检索器
retriever = vector.as_retriever()

# 创建一个工具来检索文档
from langchain.tools.retriever import create_retriever_tool

retriever_tool = create_retriever_tool(
    retriever,
    "iPhone_price_search",
    "搜索有关于iPhone16的价格信息，对于iPhone16的任何问题，您必须使用此工具！"
)

from langchain_community.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv

load_dotenv()
search = TavilySearchResults()
# 创建将在下游使用的工具列表
tools = [search, retriever_tool]

# 初始化大模型
from langchain_openai import ChatOpenAI

""" 大语言模型：langchain大模型DeepSeek"""
text = "大模型是什么？"

llm = ChatOpenAI(
    temperature=0.95,
    model="deepseek-chat",
    openai_api_key="sk-f0d8e6d4e9f1436f981daf3f2c12ce76",
    openai_api_base="https://api.deepseek.com/v1"
)

from langchain import hub

# 获取要使用的提示
prompt = hub.pull("hwchase17/openai-functions-agent")
print(prompt)
# 使用openAI function代理
from langchain.agents import create_openai_functions_agent

# 构建openAI函数代理，使用LLM、提示模板和工具来初始化代理
agent = create_openai_functions_agent(llm, tools, prompt)

# 将代理与AgentExecutor工具结合起来
from langchain.agents import AgentExecutor

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 使用代理执行任务
agent_executor.invoke({"input": "美国2024年谁生出美国总统？"})
