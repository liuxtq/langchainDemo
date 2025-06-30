from langchain_openai import ChatOpenAI

""" 大语言模型：langchain大模型通义千问"""
text = "大模型是什么？"

llm = ChatOpenAI(
    temperature=0.95,
    model="qwen-plus",
    openai_api_key="sk-db95afe6d5c643ef86b8d1a8cd4069bd",
    openai_api_base="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

result = llm.invoke(text)
print(result)