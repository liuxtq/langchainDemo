from langchain.chains import LLMMathChain

""" 数学链 LLMMathChain 
将用户问题转化成数学问题，然后将数学问题转换为可以使用python的numexpr库执行的表达式。
pip install numexpr
"""

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    temperature=0.95,
    model="deepseek-chat",
    openai_api_key="sk-f0d8e6d4e9f1436f981daf3f2c12ce76",
    openai_api_base="https://api.deepseek.com/v1"
)
llm_math = LLMMathChain.from_llm(llm)
result = llm_math.invoke("10 ** 3 + 100的结果是多少？")
print(result)