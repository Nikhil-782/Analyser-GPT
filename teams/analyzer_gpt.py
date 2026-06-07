from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from agents.code_executor import getCodeExecutorAgent
from agents.data_analyzer import getDataAnalyzerAgent
from config.consts import MAX_TURNS


def getDataAnalyzerTeam(docker,model):
    code_executor_agent = getCodeExecutorAgent(docker)
    code_analyzer_agent = getDataAnalyzerAgent(model)
    agents=[code_analyzer_agent,code_executor_agent]
    termination_condition=TextMentionTermination("STOP")
    data_analyzer_team = RoundRobinGroupChat(
        participants=agents,
        termination_condition=termination_condition,
        max_turns=MAX_TURNS
    )

    return data_analyzer_team
