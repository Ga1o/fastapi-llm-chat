import os


class Config:
    llm_api = os.getenv('LLM_API_URL')


app_config = Config()
