from sentence_transformers import SentenceTransformer

# 使用预训练的 Sentence-BERT 模型
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# 将文档文本转换为向量
def embed_documents(documents):
    embeddings = model.encode(documents)
    return embeddings
