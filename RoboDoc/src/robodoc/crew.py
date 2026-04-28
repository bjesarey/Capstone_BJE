from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

search_tool = SerperDevTool()

@CrewBase
class Robodoc():
    """Robodoc crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

   
    @agent
    def symptom_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config['symptom_analyzer'],
            tools=[search_tool],
            verbose=True
        )

    @agent
    def diagnosis_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['diagnosis_specialist'],
            tools=[search_tool],
            verbose=True
        )

    @task
    def analyze_symptoms(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_symptoms']
        )

    @task
    def diagnose(self) -> Task:
        return Task(
            config=self.tasks_config['diagnose']
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )