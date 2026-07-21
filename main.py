"""
Enterprise AI Assistant

Main Entry Point
"""

from app.config import Settings
from app.llms.factory import get_model


def main():

    print("=" * 50)
    print("Enterprise AI Assistant")
    print("=" * 50)

    print()

    # Validate Configuration
    Settings.validate()

    print(f"Default Model : {Settings.DEFAULT_MODEL}")
    print()

    # Load Model
    model = get_model()

    print("✅ Model Loaded Successfully")
    print()

    # Test Prompt
    response = model.invoke(
        "What is Generative AI?"
    )

    print("=" * 50)
    print("AI RESPONSE")
    print("=" * 50)

    print(response.content)


if __name__ == "__main__":
    main()