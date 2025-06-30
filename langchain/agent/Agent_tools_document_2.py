from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings

# 加载html内容为一个文档对象
loader = WebBaseLoader("https://finance.sina.com.cn/tech/roll/2024-09-10/doc-incnqzux8236851.shtml")
docs = loader.load()

# 分割文档
documents = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200).split_documents(docs)

# 向量化
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector = FAISS.from_documents(documents, embeddings)

# 创建检索器
retriever = vector.as_retriever()

# 测试检索结果
print(retriever.get_relevant_documents("目前市场上苹果手机16的售价是多少？"))
