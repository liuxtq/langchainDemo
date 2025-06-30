from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,SystemMessage

"""聊天模型：langchain默认使用OpenAI聊天模型"""

chat_model = ChatOpenAI(model="gpt-4o")
messages = [SystemMessage(content="你是一位乐于助人的助手，你叫波波老师"),HumanMessage(content="你是谁？")]
result = chat_model.invoke(messages)
print(result)