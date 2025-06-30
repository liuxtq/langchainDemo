from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate


template = "桌子上有{number}个苹果，四个桃子和3本书，一共有几个水果？"
# 创建langchain模板
prompt_template = PromptTemplate.from_template(template)

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    temperature=0.95,
    model="deepseek-chat",
    openai_api_key="sk-f0d8e6d4e9f1436f981daf3f2c12ce76",
    openai_api_base="https://api.deepseek.com/v1"
)

# 创建LLMChain
# llm_chain = LLMChain(
#     llm=llm,
#     prompt=prompt_template  # 此处是prompt template
# )
llm_chain = prompt_template | llm
result = llm_chain.invoke({"number":2})
print(result)