from langchain.chains.llm import LLMChain
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import PromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts.chat import ChatPromptTemplate

# 初始化大模型
llm = ChatOpenAI(
    temperature=0.95,
    model="deepseek-chat",
    openai_api_key="sk-f0d8e6d4e9f1436f981daf3f2c12ce76",
    openai_api_base="https://api.deepseek.com/v1"
)

prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content="你是一个与人类对话的机器人。"),
    MessagesPlaceholder(variable_name="chat_history"),
    HumanMessagePromptTemplate.from_template("{question}")
])
print(prompt)


# 创建聊天对话记忆
memory = ConversationBufferMemory(memory_key="chat_history",return_messages=True)

# 初始化链
conv_chain = LLMChain(llm=llm,prompt=prompt,memory=memory)

#提问
result = conv_chain.invoke({"question":"你是LangChain专家。"})
print(str(result)+"\n")
result = conv_chain.invoke({"question":"我的名字叫波波老师。"})
print(str(result)+"\n")
result = conv_chain.invoke({"question":"我的名字是什么？"})
print(str(result)+"\n")

