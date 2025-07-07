# Langchain

## Tools

https://python.langchain.com/docs/integrations/tools/

## Model IO

![Model_io.png](langchain%2Fimage%2FModel_io.png)

### 提示模板

![Model_prompt_template_1.png](langchain%2Fimage%2FModel_prompt_template_1.png)
![Model_prompt_template_2.png](langchain%2Fimage%2FModel_prompt_template_2.png)
**PromptTemplate 与 ChatPromptTemplate在使用场景的上的区别：**
![Model_prompt_template_3.png](langchain%2Fimage%2FModel_prompt_template_3.png)

### Model

![Model_1.png](langchain%2Fimage%2FModel_1.png)

#### 大语言模型

1. openAI [langchain_model_openapi.py](langchain%2Fmodel_io%2Fmodel%2Flangchain_model_openapi.py)
2. 智谱清言 [langchain_model_zhipu.py](langchain%2Fmodel_io%2Fmodel%2Flangchain_model_zhipu.py)
3. 通义千问 [langchain_model_tongyiqianwen.py](langchain%2Fmodel_io%2Fmodel%2Flangchain_model_tongyiqianwen.py)
4. KIMI [langchain_model_moonshot.py](langchain%2Fmodel_io%2Fmodel%2Flangchain_model_moonshot.py)
5. DeepSeek [langchain_model_deepseek.py](langchain%2Fmodel_io%2Fmodel%2Flangchain_model_deepseek.py)

#### 聊天模型

![Chat_Model_1.png](langchain%2Fimage%2FChat_Model_1.png)

#### 文本嵌入模型

1. openAI [langchain_model_embedding_openapi.py](langchain%2Fmodel_io%2Fmodel%2Flangchain_model_embedding_openapi.py)
2.

thirdParty [langchain_model_embedding_thirdparty.py](langchain%2Fmodel_io%2Fmodel%2Flangchain_model_embedding_thirdparty.py)

### 输出解析

![Model_parse_output.png](langchain%2Fimage%2FModel_parse_output.png)

## Memory

### 基本介绍

![Memory_1.png](langchain%2Fimage%2FMemory_1.png)

### 工作流程

![Memory_2.png](langchain%2Fimage%2FMemory_2.png)

### Chat Message

![Memory_3.png](langchain%2Fimage%2FMemory_3.png)
[memory_ChatMessageHisotry.py](langchain%2Fmemory%2Fmemory_ChatMessageHisotry.py)

### Memory Classes

![Memory_4.png](langchain%2Fimage%2FMemory_4.png)
**ConversationChain**

[memory_ConversationBufferMemory_1.py](langchain%2Fmemory%2Fmemory_ConversationBufferMemory_1.py)

**ConversationBufferMemory**

[memory_ConversationBufferMemory_2.py](langchain%2Fmemory%2Fmemory_ConversationBufferMemory_2.py)

**LLMChain**
_（为非聊天大模型增加记忆）_

[memory_ConversationBufferMemory_3.py](langchain%2Fmemory%2Fmemory_ConversationBufferMemory_3.py)

[memory_ConversationBufferMemory_4.py](langchain%2Fmemory%2Fmemory_ConversationBufferMemory_4.py)

## Chain链

![Chain_1.png](langchain%2Fimage%2FChain_1.png)

API地址：https://python.langchain.com/api_reference/langchain/chains.html

### LLM链的基本使用

![Chain_LLMChain.png](langchain%2Fimage%2FChain_LLMChain.png)

[chain_without_llmchain_1.py](langchain%2Fchain%2Fchain_without_llmchain_1.py)

[chain_with_llmchain_2.py](langchain%2Fchain%2Fchain_with_llmchain_2.py)

![Chain_2.png](langchain%2Fimage%2FChain_2.png)

![Chain_3.png](langchain%2Fimage%2FChain_3.png)

[chain_demo_3.py](langchain%2Fchain%2Fchain_demo_3.py)

### chain的调用方式

1. chain.invoke() （推荐）
2. chain.predict()：predict用于获取模型预测的结果，可能会跳过chain中的某些步骤，比如输入预处理获后处理。它专注于模型的预测部分，而不是整个chain的流程。
   因此，predict的速度可能会更快，但是结果也可能不符合chain的预期。
3. chain.batch():batch方法允许输入列表运行链，以此处理多个输入。[chain_demo_4.py](langchain%2Fchain%2Fchain_demo_4.py)

### 官方工具链

API地址：https://python.langchain.com/api_reference/langchain/chains.html

1. 文档链 create_stuff_documents_chain链将获取文档列表并将它们全部格式化为提示（文档列表），然后将该提示传递给LLM。
   [chain_demo_5.py](langchain%2Fchain%2Fchain_demo_5.py)
2. 数学链 LLMMathChain 将用户问题转化成数学问题，然后将数学问题转换为可以使用python的numexpr库执行的表达式。  
   `pip install numexpr` [chain_demo_6.py](langchain%2Fchain%2Fchain_demo_6.py)
3. SQL查询链 create_sql_query_chain是创建生成SQL查询的链，用于将自然语言转换成数据库的SQL查询。
   `pip install pymysql`
   [chain_demo_7.py](langchain%2Fchain%2Fchain_demo_7.py)

## Agent

![Agent_1.png](langchain%2Fimage%2FAgent_1.png)

### 基本使用

[Agent_tools_tavily_1.py](langchain%2Fagent%2FAgent_tools_tavily_1.py)

[Agent_tools_document_2.py](langchain%2Fagent%2FAgent_tools_document_2.py)

[Agent_tools_demo_3.py](langchain%2Fagent%2FAgent_tools_demo_3.py)

[Agent_tools_demo_3.py](langchain%2Fagent%2FAgent_tools_demo_3.py)

### ReAct Agent

![Agent_reActAgent_1.png](langchain%2Fimage%2FAgent_reActAgent_1.png)

[Agent_ReActAgent_5.py](langchain%2Fagent%2FAgent_ReActAgent_5.py)

[Agent_ReActAgent_6.py](langchain%2Fagent%2FAgent_ReActAgent_6.py)

### Self-Ask with Search Agent

![Agent_selfAskWithAgent.png](langchain%2Fimage%2FAgent_selfAskWithAgent.png)

# 下载模型和数据集

## 从hugginface下载模型

`huggingface-cli download maidalun1020/bce-embedding-base_v1 --local-dir ./maidalun1020`

## 从hugginface下载数据集

`huggingface-cli download --repo-type dataset lavita/medical-qa-shared-task-v1-toy`

## 从魔塔社区下载模型

`pip install modelscope`

`from modelscope import snapshot_download
model_dir = snapshot_download("Cecelianchenen/bge-large-zh-v1.5",cache_dir="")`