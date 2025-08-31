from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileReadTool,CSVSearchTool


@CrewBase
class MatchToProposalCrew:
    """A crew to match profiles to job proposals."""
    agents_config = 'config/agents.yaml'
    tasks_config  = 'config/tasks.yaml'

    @agent
    def cv_reader(self) -> Agent:
        return Agent(
            config = self.agents_config['cv_reader'],
            tools  = [FileReadTool()],
            verbose=True,
            allow_delegation=False
        )

    @agent
    def matcher(self) -> Agent:
        return Agent(
            config = self.agents_config['matcher'],
            tools  = [FileReadTool(),CSVSearchTool()],
            verbose=True,
            allow_delegation=False
        )

    @task
    def cv_read_task(self) -> Task:
        return Task(
            config=self.tasks_config['read_cv_task'],
            agent = self.cv_reader()
        )

    @task
    def match_cv_task(self) -> Task:
        return Task(
            config=self.tasks_config['match_cv_task'],
            agent = self.matcher()
        )

    @crew
    def crew(self) -> Crew:
        """Define the crew process. """
        return Crew(
            agent =self.agents,
            tasks = self.tasks,
            process=Process.sequential,
            verbose=True
        )
