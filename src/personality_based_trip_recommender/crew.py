
from crew import CrewBase, agent, task, crew
from crew.agents import Agent
from crew.tasks import Task
from crew.process import Process
from crew.llms import LLM

@CrewBase
class PersonalityBasedTripRecommenderCrew:
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def personality_analyzer(self) -> Agent:
        return Agent(config=self.agents_config["personality_analyzer"], verbose=True, llm=LLM(model="claude-sonnet-4-6"))

    @agent
    def trip_recommender(self) -> Agent:
        return Agent(config=self.agents_config["trip_recommender"], verbose=True, llm=LLM(model="claude-sonnet-4-6"))

    @task
    def analyze_personality(self) -> Task:
        return Task(config=self.tasks_config["analyze_personality"])

    @task
    def recommend_trip(self) -> Task:
        return Task(config=self.tasks_config["recommend_trip"])

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )