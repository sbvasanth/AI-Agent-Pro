from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

load_dotenv()


def get_llm():
    """Create and return the configured Groq LLM."""
    return ChatGroq(
        model="openai/gpt-oss-20b",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0,
    )
