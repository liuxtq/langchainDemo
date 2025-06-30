from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory

# 初始化大模型
llm = ChatOpenAI(
    temperature=0.95,
    model="deepseek-chat",
    openai_api_key="sk-f0d8e6d4e9f1436f981daf3f2c12ce76",
    openai_api_base="https://api.deepseek.com/v1"
)

# 创建提示，有两个输入键：实际输入与来自记忆类的输入，需确保PromptTemplate和ConversationBufferMemory中的键匹配
template = """
你可以与人类对话。

当前对话：{chat_history}

人类问题：{question}

回复：
"""
prompt = PromptTemplate(input_variables=["chat_history","question"],template=template)

# 创建聊天对话记忆
memory = ConversationBufferMemory(memory_key="chat_history")

# 初始化链
conv_chain = LLMChain(llm=llm,prompt=prompt,memory=memory)

#提问
result = conv_chain.invoke({"question":"你是LangChain专家。"})
print(str(result)+"\n")
result = conv_chain.invoke({"question":"我的名字叫波波老师。"})
print(str(result)+"\n")
result = conv_chain.invoke({"question":"我的名字是什么？"})
print(str(result)+"\n")

