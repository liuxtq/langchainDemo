from langchain.prompts import PromptTemplate

"""
少样本提示词
"""
examples = [
    {"input":"2+2","output":"4","description":"加法运算"},
    {"input":"5-2","output":"3","description":"减法运算"}
]

# 创建提示模板
template = "您是一位数学专家，算式：{input}，值：{output},使用：{description}。"
prompt_sample = PromptTemplate.from_template(template)

print(prompt_sample.format_prompt(**examples[0]))
print(prompt_sample.format_prompt(input="5-2",output="3",description="减法运算"))
