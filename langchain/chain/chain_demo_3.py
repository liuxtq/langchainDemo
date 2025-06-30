from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_experimental.utilities import PythonREPL

template = """
Write some python code to resolve user's problem.
Return only python code in Markdown format, e.g:
```python
...
```
"""
prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", "{input}")
])


def _sanitize_output(text: str):
    _, after = text.split("```python")
    return after.split("```")[0]


from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    temperature=0.95,
    model="deepseek-chat",
    openai_api_key="sk-f0d8e6d4e9f1436f981daf3f2c12ce76",
    openai_api_base="https://api.deepseek.com/v1"
)

# PythonREPL().run 就是调用了以下exec函数执行代码
chain = prompt | llm | StrOutputParser() | _sanitize_output | PythonREPL().run
# chain = prompt | llm | StrOutputParser()

result = chain.invoke({"input": "whats 2 plus 2"})
print(result)
