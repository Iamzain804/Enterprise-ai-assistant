"""Project Configuration

Purpose:
- Load environment variables
- Validate required settings
- Keep configuration in one place
"""

import os 
from dotenv import load_dotenv

#load .env file
load_dotenv()

class Settings:
    """ Every module will import values from here."""
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    DEFAULT_MODEL =   os.getenv("DEFAULT_MODEL","groq")

    @classmethod
    def validate(cls):
        """
        validate required configuration
        """
        if not cls.GROQ_API_KEY:
            print("GROQ_API_KEY is missing.")

        if not cls.GOOGLE_API_KEY:
            print("GOOGLE_API_KEY is missing.")

if __name__ == "__main__":
    Settings.validate()
