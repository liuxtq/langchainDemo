from langchain_openai import OpenAIEmbeddings

""" 文本嵌入模型：langchain提供的默认接入的文本嵌入模型是openAI，运行不了，没充钱"""
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

# 定义一个文本字符串
text = "大模型"

# 嵌入文档
doc_result = embeddings.embed_documents([text])
print(doc_result[0][:5])

#嵌入查询
query_result = embeddings.embed_query(text)
print(query_result[:5])