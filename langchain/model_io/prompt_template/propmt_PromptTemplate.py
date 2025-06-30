from langchain.prompts.prompt import PromptTemplate

from langchain.model_io.prompt_template.propmt_ChatPromptemplate import chat_prompt

# 创建原始模板
template = "您是一位专业程序员。\n对于 {text} 进行简短描述。"

# 根据原始模板创建langchain提示模板
# prompt = PromptTemplate.from_template(template)

prompt = PromptTemplate(
    input_variables=['text'],
    template="您是一位专业程序员。\n对于 {text} 进行简短描述。"
)

# 打印提示模板内容
print(prompt)
print("="*50)
print(prompt.format(text="langchain"))

# 调用大模型...
