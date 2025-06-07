# app/services/agent_runner.py
from autogen import AssistantAgent, UserProxyAgent, config_list_from_dotenv

config_list = config_list_from_dotenv()

assistant = AssistantAgent(
    name="assistant",
    llm_config={"config_list": config_list, "cache_seed": 42}
)

user_proxy = UserProxyAgent(name="user", code_execution_config=False)

def run_agent(prompt: str) -> str:
    messages = user_proxy.initiate_chat(assistant, message=prompt)
    return str(messages)
