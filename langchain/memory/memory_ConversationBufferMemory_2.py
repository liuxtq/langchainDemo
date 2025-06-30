from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains.conversation.base import ConversationChain

# 初始化大模型
llm = ChatOpenAI(
    temperature=0.95,
    model="deepseek-chat",
    openai_api_key="sk-f0d8e6d4e9f1436f981daf3f2c12ce76",
    openai_api_base="https://api.deepseek.com/v1"
)

# 添加聊天对话记忆
memory = ConversationBufferMemory()
memory.chat_memory.add_user_message("你是谁？")
memory.chat_memory.add_ai_message("你好，我是LangChain专家。")

# 初始化对话链
conv_chain = ConversationChain(llm=llm,memory=memory)


result = conv_chain.invoke({"input":"你是谁？"})
print(result)
