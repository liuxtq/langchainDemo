from crewai import Agent, Task, Crew, Process

from crewai.llm import LLM  # 0.141+ 专用

# 1. 构造 DeepSeek LLM
llm = LLM(
    model="deepseek-chat",  # 或 deepseek-reasoner
    base_url="https://api.deepseek.com/v1",
    api_key="sk-f0d8e6d4e9f1436f981daf3f2c12ce76",
    temperature=0.3
)

researcher = Agent(
    role="研究员",
    goal="研究AI最新前景",
    backstory="你是一个AI研究助手",
    verbose=True,
    allow_delegation=False,
    llm=llm
)
writer = Agent(
    role="写作人员",
    goal="编写关于AI前景相关的吸引人的博客",
    backstory="你是一个AI博主，专门写AI前景相关的博客",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

task1 = Task(description="研究AI最新的趋势", agent=researcher, expected_output="一份关于AI最新趋势的研究报告")
task2 = Task(description="写一篇引人入胜的关于AI最新趋势的博客", agent=writer, expected_output="一篇引人入胜的博客文章")
crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, task2],
    verbose=True,
    process=Process.sequential

)

result = crew.kickoff()
