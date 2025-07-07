from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI

""" 大语言模型：langchain大模型DeepSeek"""

llm = ChatOpenAI(
    temperature=0.95,
    model="qwen-plus",
    openai_api_key="sk-db95afe6d5c643ef86b8d1a8cd4069bd",
    openai_api_base="https://dashscope.aliyuncs.com/compatible-mode/v1"
)
# 设置工具：加载使用的工具，serpapi：调用google搜索引擎，llm-math：通过LLM进行数学计算的工具
tools = load_tools(['serpapi', 'llm-math'], llm=llm)
# 初始化agent：使用工具、语言模型和代理类型来初始化代理。ZERO_SHOT_REACT_DESCRIPTION类型的代理可以在没有预先训练的情况下尝试解决新的问题
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# 让代理来回答提出的问题
agent.invoke({"input": "目前市场上苹果手机16 128G的售价是多少？如果我在此基础上加价5%卖出，应该如何定价？请用中文回答"})
