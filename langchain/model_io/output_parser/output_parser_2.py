from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import DatetimeOutputParser
"""
DatetimeOutputParser
"""
# 定义prompt 模板
template="""
回答用户的问题：{question}

{format_instructions}
"""
# 使用日期时间解析器
output_parser = DatetimeOutputParser()

prompt = PromptTemplate.from_template(
    template,
    partial_variables={"format_instructions":output_parser.get_format_instructions()}
    )
"""
write a datetime str that matches the following pattern:'%Y-%m-%dT%H:%M:%S.%fZ'
Example:1949-08-11T00:31:18.305832Z
Return only this str, no other words!
"""
# 大模型
from langchain_openai import ChatOpenAI
""" langchain大模型DeepSeek"""

llm = ChatOpenAI(
    model="moonshot-v1-8k",
    openai_api_key="sk-aoSkzLYwD03brkH0BEodIu3b755x98U66iyezXhCKLkdJEm3",
    openai_api_base="https://api.moonshot.cn/v1"
)

# 将提示词和模型合并调用
chain = prompt | llm | output_parser
result = chain.invoke({"question":"新中国是什么时候成立的？"})
print(result)

format_str = "%Y年%m月%d日"
print(result.strftime(format_str))


