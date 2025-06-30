from langchain_openai import ChatOpenAI
""" 大语言模型：langchain大模型DeepSeek"""
text = "大模型是什么？"

llm = ChatOpenAI(
    temperature=0.95,
    model="deepseek-chat",
    openai_api_key="sk-f0d8e6d4e9f1436f981daf3f2c12ce76",
    openai_api_base="https://api.deepseek.com/v1"
)

result = llm.invoke(text)
print(result)