"""
LLM Model Initialization

Purpose:
- Initialize all supported chat models.
- No business logic should exist here.
"""

from langchain.chat_models import init_chat_model
from app.config import Settings

def creat_groq_model():
    """ Create and return Groq model """

    return init_chat_model(
        model = "llama-3.3-70b-versatile",
        model_provider = "groq",
        api_key = Settings.GROQ_API_KEY
        
    )

def create_gemini_model():
    """Create and return Gemini model"""
    return init_chat_model(
        model= "gemini-2.5-flash",
        model_provier = "google_genai",
        api_key = Settings.GOOGLE_API_KEY
    )

    