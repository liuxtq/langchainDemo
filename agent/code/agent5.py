from langchain_openai import ChatOpenAI
from langchain.agents import load_tools
from dotenv import load_dotenv

load_dotenv()

""" 
聊天模型
会做数学题
不知道答案的时候可以搜索
无记忆
"""

llm = ChatOpenAI(
    temperature=0.95,
    model="deepseek-chat",
    openai_api_key="sk-f0d8e6d4e9f1436f981daf3f2c12ce76",
    openai_api_base="https://api.deepseek.com/v1"
)
# 搭建工具 serpapi是一个聚合搜索引擎，需要安装google搜索包(pip install google-search-results)以及申请账号。https://serpapi.com/manage-api-key
tools = load_tools(['serpapi', 'llm-math'], llm)

from langchain.agents import initialize_agent
from langchain.agents import AgentType

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True  # 是否打印日志
)
text = "美国现任总统是谁？他的年龄的平方是多少？"
agent.run(text)
