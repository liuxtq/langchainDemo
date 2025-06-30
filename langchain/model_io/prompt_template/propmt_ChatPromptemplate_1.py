from langchain.prompts.chat import ChatPromptTemplate

# 创建原始模板
template = "您是一位翻译专家，擅长将{input_language}语言翻译成{output_language}语言。"
human_template = "{text}"

# 根据原始模板创建langchain提示模板
chat_prompt = ChatPromptTemplate.from_messages([
    ("system",template),
    ("human",human_template)
]
)

# 打印提示模板内容
print(chat_prompt)
print("="*50)

# 调用大模型...
from langchain_openai import ChatOpenAI
""" langchain大模型KIMI"""
llm = ChatOpenAI(
    model="moonshot-v1-8k",
    openai_api_key="sk-aoSkzLYwD03brkH0BEodIu3b755x98U66iyezXhCKLkdJEm3",
    openai_api_base="https://api.moonshot.cn/v1"
)
message = chat_prompt.format_messages(
    input_language="英文",
    output_language="中文",
    text="I Love Large Language Model!"
)
print(message)
print("="*50)
result = llm.invoke(message)
print(result.content)