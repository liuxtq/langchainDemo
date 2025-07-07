import calendar
import dateutil.parser as parser
from datetime import datetime
from langchain.tools import tool
from langchain.agents import load_tools
from langchain import hub
from dotenv import load_dotenv

load_dotenv()
tools = load_tools(['serpapi'])


# 自定义工具
@tool("weekday")
def weekday(date_str: str):
    """Convert date to weekday name"""
    date_str = date_str.strip('"')  # 去掉字符串两端的双引号
    date_str = date_str.strip()  # 去掉字符串两端的空格
    d = datetime.strptime(date_str, "%Y-%m-%d")  # 指定日期格式
    return calendar.day_name[d.weekday()]


# 将自定义的工具加入tools数组中
tools += [weekday]

from langchain_openai import ChatOpenAI

""" 大语言模型：langchain大模型DeepSeek"""

llm = ChatOpenAI(
    temperature=0.95,
    model="qwen-plus",
    openai_api_key="sk-db95afe6d5c643ef86b8d1a8cd4069bd",
    openai_api_base="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 下载一个现有的prompt模板
prompt = hub.pull("hwchase17/react")
# print(prompt)
from langchain.agents import create_react_agent

agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)

from langchain.agents import AgentExecutor

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
agent_executor.invoke({"input": "周杰伦的生日是星期几？"})
