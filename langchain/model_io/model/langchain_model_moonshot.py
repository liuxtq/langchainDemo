from langchain_openai import ChatOpenAI
""" 大语言模型：langchain大模型KIMI"""
text = "大模型是什么？"

llm = ChatOpenAI(
    model="moonshot-v1-8k",
    openai_api_key="sk-aoSkzLYwD03brkH0BEodIu3b755x98U66iyezXhCKLkdJEm3",
    openai_api_base="https://api.moonshot.cn/v1"
)

result = llm.invoke(text)
print(result)