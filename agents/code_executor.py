from autogen_agentchat.agents import CodeExecutorAgent

def getCodeExecutorAgent(code_executor):
    agent = CodeExecutorAgent(
        name="CodeExecutorAgent",
        code_executor=code_executor,
    )

    return agent