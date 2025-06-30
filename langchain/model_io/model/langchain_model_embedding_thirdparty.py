from langchain_community.embeddings import HuggingFaceEmbeddings

""" 文本嵌入模型： langchain使用第三方文本嵌入模型，可以通过Huggingface-cli或者魔塔社区下载"""
import os
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# 定义一个文本字符串
text = "大模型"

# 嵌入文档
doc_result = embeddings.embed_documents([text])
print(doc_result[0][:5])

#嵌入查询
query_result = embeddings.embed_query(text)
print(query_result[:5])