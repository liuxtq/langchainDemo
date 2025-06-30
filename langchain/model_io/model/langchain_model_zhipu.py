from langchain_openai import ChatOpenAI
""" 大语言模型：langchain大模型智谱清言"""
text = "大模型是什么？"

llm = ChatOpenAI(
    temperature=0.95,
    model="glm-4",
    openai_api_key="2a1ea53aaae642078c2c49d11c157e8d.UygshpEQmESHddIe",
    openai_api_base="https://open.bigmodel.cn/api/paas/v4/"
)

result = llm.invoke(text)
print(result)