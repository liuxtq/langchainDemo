from langchain_openai import ChatOpenAI
from langchain.chains.conversation.base import ConversationChain

# 初始化大模型
llm = ChatOpenAI(
    temperature=0.95,
    model="deepseek-chat",
    openai_api_key="sk-f0d8e6d4e9f1436f981daf3f2c12ce76",
    openai_api_base="https://api.deepseek.com/v1"
)
# 初始化对话链
conv_chain = ConversationChain(llm=llm)

# 打印对话的模板
print(conv_chain.prompt.template)
result = conv_chain.invoke("我是波波老师。")
print(result)
result = conv_chain.invoke("你是谁？")
print(result)
result = conv_chain.invoke("我是谁？")
print(result)

