from langchain_openai import ChatOpenAI
from langchain.agents import load_tools
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv

load_dotenv()
""" 
推理模型
会做数学题
不知道答案的时候可以搜索
有记忆
"""

llm = ChatOpenAI(
    temperature=0.95,
    model="deepseek-reasoner",
    openai_api_key="sk-f0d8e6d4e9f1436f981daf3f2c12ce76",
    openai_api_base="https://api.deepseek.com/v1"
)
# 搭建工具 serpapi是一个聚合搜索引擎，需要安装google搜索包(pip install google-search-results)以及申请账号。https://serpapi.com/manage-api-key
tools = load_tools(['serpapi', 'llm-math'], llm)

# 记忆组件-短时记忆
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)  # return_messages=True 必须立刻返回模型消息

from langchain.agents import initialize_agent
from langchain.agents import AgentType

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=True  # 是否打印日志
)
from langchain import PromptTemplate

template = """
{input}
"""
prompt = PromptTemplate(
    input_variables=['input'],
    template=template
)

agent.run(prompt.format(input="我是刘峰"))

agent.run(prompt.format(input="我是谁"))
