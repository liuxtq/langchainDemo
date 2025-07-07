from langchain import hub
from langchain.agents import AgentExecutor, create_self_ask_with_search_agent
from langchain_community.tools.tavily_search import TavilyAnswer
from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="moonshot-v1-8k",
    openai_api_key="sk-aoSkzLYwD03brkH0BEodIu3b755x98U66iyezXhCKLkdJEm3",
    openai_api_base="https://api.moonshot.cn/v1"
)

# 初始化工具，让它提供答案而不是文档
tools = [TavilyAnswer(max_results=1, name="Intermediate Answer", description="Answer Search")]
prompt = hub.pull("hwchase17/self-ask-with-search")
# 使用搜索代理构建自主询问
agent = create_self_ask_with_search_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)
# 运行代理
agent_executor.invoke(
    {"input": "中国有哪些省份呢？用中文回答。"})
