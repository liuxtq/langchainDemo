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

# print(prompt_sample.format_prompt(**examples[0]))
# print(prompt_sample.format_prompt(input="5-2",output="3",description="减法运算"))

from langchain.prompts.few_shot import FewShotPromptTemplate
prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=prompt_sample,
    suffix="您是一位数学专家，算式：{input}，值：{output}", # 对应用户输入的信息
    input_variables=["input","output"]
)
result = prompt.format(input="2+5",output="7")
print(result)

"""
输出：
您是一位数学专家，算式：2+2，值：4,使用：加法运算。 -- 样本

您是一位数学专家，算式：5-2，值：3,使用：减法运算。 -- 样本

您是一位数学专家，算式：2+5，值：7 -- 用户输入

"""

# 大模型生成回答
from openai import OpenAI

client = OpenAI(
    api_key="sk-f0d8e6d4e9f1436f981daf3f2c12ce76",
    base_url="https://api.deepseek.com/v1"  # 兼容OpenAI的端点
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": result}
    ],
    temperature=0, # 采样温度，介于 0 和 2 之间。更高的值，如 0.8，会使输出更随机，而更低的值，如 0.2，会使其更加集中和确定。
    stream=False
)

print(response.choices[0].message.content)