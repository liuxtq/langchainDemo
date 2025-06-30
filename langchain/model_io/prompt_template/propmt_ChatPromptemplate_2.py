from langchain.chains.summarize.refine_prompts import prompt_template
from langchain.prompts.chat import ChatPromptTemplate
from langchain.prompts import (
ChatMessagePromptTemplate,
SystemMessagePromptTemplate,
AIMessagePromptTemplate,
HumanMessagePromptTemplate
)


system_template = "您是一位翻译专家，擅长将{input_language}语言翻译成{output_language}语言。"
system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)

human_template = "{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

prompt_template = ChatPromptTemplate.from_messages([system_message_prompt,human_message_prompt])

# 格式化消息生成提示
chat_prompt = prompt_template.format_prompt(input_language="英文",
    output_language="中文",
    text="I Love Large Language Model!").to_messages()


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