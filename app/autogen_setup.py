from autogen import UserProxyAgent, AssistantAgent, config_list_from_dotenv

# Load OpenAI key
config_list = config_list_from_dotenv()

# Create an assistant
assistant = AssistantAgent(
    name="assistant",
    llm_config={"config_list": config_list, "cache_seed": 42}
)

# Create a user proxy (interface between user and agents)
user_proxy = UserProxyAgent(name="user", code_execution_config=False)

# Start the interaction
user_proxy.initiate_chat(
    assistant,
    message="What is the capital of France?"
)
