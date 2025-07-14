from langchain_openai import ChatOpenAI
from langchain.agents import load_tools, initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv

# 加载 .env 中的环境变量
load_dotenv()
""" 
聊天模型
会做数学题
不知道答案的时候可以搜索
有记忆
"""
# 初始化 LLM
llm = ChatOpenAI(
    temperature=0.95,
    model="deepseek-chat",
    openai_api_key="sk-f0d8e6d4e9f1436f981daf3f2c12ce76",
    openai_api_base="https://api.deepseek.com/v1"
)

# 加载工具
tools = load_tools(['serpapi', 'llm-math'], llm=llm)

# 搭建对话内存，关键参数：memory_key 必须是 chat_history
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# 初始化 Agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=True
)

# 用 agent 进行对话，自动写入 memory
print("\n=== 第 1 轮 ===")
response1 = agent.run("你好")
print(f"AI: {response1}")

print("\n=== 第 2 轮 ===")
response2 = agent.run("我是刘峰")
print(f"AI: {response2}")

print("\n=== 第 3 轮 ===")
response3 = agent.run("我们都聊了什么？")
print(f"AI: {response3}")

# 查看完整对话上下文
print("\n=== 内存状态 ===")
print(memory.load_memory_variables({}))
