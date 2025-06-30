from langchain_community.utilities import SQLDatabase

""" SQL查询链 create_sql_query_chain是创建生成SQL查询的链，用于将自然语言转换成数据库的SQL查询。
pip install pymysql
"""
# 链接 MySQL数据库
db_user = "root"
db_password = "123456"
db_host = "127.0.0.1"
db_port = "3306"
db_name = "llm"
db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")

# print("哪种数据库：",db.dialect)
# print("获取数据表：",db.get_usable_table_names())
#
# # 执行查询
# result = db.run("select count(*) from students;")
# print("查询结果",result)

from langchain.chains import create_sql_query_chain
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    temperature=0.95,
    model="deepseek-chat",
    openai_api_key="sk-f0d8e6d4e9f1436f981daf3f2c12ce76",
    openai_api_base="https://api.deepseek.com/v1"
)
chain = create_sql_query_chain(llm, db)
# result = chain.invoke({"question":"查询考试科目一共有多少？"})
result = chain.invoke({"question": "查询每个学生各科成绩平均分是多少？"})
# 限制使用制定表
# result = chain.invoke({"question":"一共有多少学生？","table_names_to_use":["students"]})
print(result)
