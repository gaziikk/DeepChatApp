import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Конфигурация"""
    API_KEY = os.getenv("API_KEY")
    MODEL = "deepseek/deepseek-r1"
    API_URL = "https://openrouter.ai/api/v1/chat/completions"
