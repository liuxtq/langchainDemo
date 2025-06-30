from langchain_core.prompts import ChatPromptTemplate
# 定义prompt 模板
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一位专业程序员"),
    ("human", "{input}")
]
    )

# 大模型
from langchain_openai import ChatOpenAI
""" langchain大模型DeepSeek"""

llm = ChatOpenAI(
    temperature=0.95,
    model="deepseek-chat",
    openai_api_key="sk-f0d8e6d4e9f1436f981daf3f2c12ce76",
    openai_api_base="https://api.deepseek.com/v1"
)

# 定义输出解析器
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
output_parser = JsonOutputParser()
# output_parser = StrOutputParser()

# 将提示词和模型合并调用
chain = prompt | llm | output_parser
result = chain.invoke({"input":"Langchain是什么？ 问题用question，回答用ans，返回一个JSON格式"})
print(result)



