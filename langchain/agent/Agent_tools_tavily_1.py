from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults

load_dotenv()

# Tavily 在线检索工具
# 需要先在https://tavily.com上注册申请TAVILY_API_KEY
search = TavilySearchResults()
result = search.invoke("目前市场上苹果手机16的售价是多少？")
print(result)
