from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

""" chain的调用方式 ： chain.batch()"""
prompt = PromptTemplate(
    input_variables=["role","fruit"],
    template="{role}喜欢出{fruit}"
)

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    temperature=0.95,
    model="deepseek-chat",
    openai_api_key="sk-f0d8e6d4e9f1436f981daf3f2c12ce76",
    openai_api_base="https://api.deepseek.com/v1"
)

inputs = [{"role":"猪八戒","fruit":"西瓜"},{"role":"孙悟空","fruit":"桃子"}]
llm_chain = LLMChain(
    llm=llm,
    prompt=prompt  # 此处是prompt template
)
result = llm_chain.batch(inputs)
print(result)
