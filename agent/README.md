# Agent

## Agent 是什么？

![agent_1.png](images%2Fagent_1.png)
![agent_2.png](images%2Fagent_2.png)
**名词解释：**

ReAct Loop 是一种AI代理决策循环机制，全称为 Reasoning + Acting
Loop，即将“推理（Reason）”与“行动（Act）”交替进行，形成一个迭代闭环，直到完成任务或达到最大循环次数。

| 步骤                  | 说明                                |
|---------------------|-----------------------------------|
| **Thought**（思考）     | 分析当前问题，制定下一步策略或行动计划               |
| **Action**（行动）      | 根据思考结果，调用工具或执行某个操作（如搜索、计算、API调用等） |
| **Observation**（观察） | 获取行动结果，作为下一轮推理的输入                 |
| **Loop or Answer**  | 如果结果不足或错误，继续下一轮循环；否则给出最终答案并结束流程   |

## AgentType

![agent_3.png](images%2Fagent_3.png)
> ZERO_SHOT_REACT_DESCRIPTION 零样本增强式生成，即在没有示例的情况下可以自主的进行对话的类型，
>
> https://blog.csdn.net/weixin_42010722/article/details/131182669
>
> [agent1.py](code%2Fagent1.py)
>
> CHAT_ZERO_SHOT_REACT_DESCRIPTION 使用chat model
>
> [agent2.py](code%2Fagent2.py)
>
> CONVERSATIONAL_REACT_DESCRIPTION 一个对话型的agent,这个agent要求与memory使用
>
> [agent3.py](code%2Fagent3.py)
>
> CHAT_CONVERSATIONAL_REACT_DESCRIPTION 使用chat model
>
> [agent4.py](code%2Fagent4.py)
>
> CHAT_ZERO_SHOT_REACT_DESCRIPTION 使用chat model

## 如何给agent正确的增加记忆

![agent_4.png](images%2Fagent_4.png)


