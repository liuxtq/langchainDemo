from langchain_openai import ChatOpenAI
""" 大语言模型：langchain提供的默认接入大模型是openAI，运行不了，没充钱"""
text = "大模型是什么？"
llm = ChatOpenAI()
result = llm.invoke(text)
print(result)