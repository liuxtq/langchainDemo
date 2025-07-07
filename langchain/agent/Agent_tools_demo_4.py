from langchain_community.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv

load_dotenv()

search = TavilySearchResults()
# 创建将在下游使用的工具列表
tools = [search]

from langchain_openai import ChatOpenAI

""" 大语言模型：langchain大模型DeepSeek"""

llm = ChatOpenAI(
    temperature=0.95,
    model="deepseek-chat",
    openai_api_key="sk-f0d8e6d4e9f1436f981daf3f2c12ce76",
    openai_api_base="https://api.deepseek.com/v1"
)

from langchain import hub

# 获取要使用的提示
prompt = hub.pull("hwchase17/openai-functions-agent")

# 使用openAI function代理
from langchain.agents import create_openai_functions_agent

# 构建openAI函数代理，使用LLM、提示模板和工具来初始化代理
agent = create_openai_functions_agent(llm, tools, prompt)

# 将代理与AgentExecutor工具结合起来
from langchain.agents import AgentExecutor

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 执行代理
# 传入一个空的消息列表给chat_history，因为它是聊天中的第一条信息
from langchain_core.messages import AIMessage, HumanMessage

chat_history = []

# 使用代理执行任务
result = agent_executor.invoke({"input": "hello 我是刘老师", "chat_history": chat_history})
# print("result", result)

# 加入聊天历史
chat_history.append(HumanMessage(content=result['input']))
chat_history.append(AIMessage(content=result['output']))

agent_executor.invoke({
    "input": "我的名字是什么？",
    "chat_history": chat_history
})
