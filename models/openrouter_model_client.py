from autogen_ext.models.openai import OpenAIChatCompletionClient
from config.consts import MODEL
import os
from dotenv import load_dotenv
load_dotenv()

open_router_api_key=os.getenv("OPENROUTER_API_KEY")

def get_model_client():
    model_client = OpenAIChatCompletionClient(
        base_url="https://openrouter.ai/api/v1",
        model=MODEL,
        api_key=open_router_api_key,
        model_info={
            "family": 'deepseek',
            "vision": True,
            "function_calling": True,
            "json_output": False
        }
    )

    return model_client