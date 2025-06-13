import os
from langchain_groq import ChatGroq
from .config import CUSTOMLEARN_GROQ_API_KEY , MODEL_ID

class GroqClient:
    """
    Manages the instantiation and configuration of a ChatGroq language model client.
    """

    def __init__(self, api_key: str = None, model: str = MODEL_ID):
        """
        Initializes the GroqClient with the specified API key and model.

        Args:
            api_key (str, optional): The API key for Groq. If not provided, uses the CUSTOMLEARN_GROQ_API_KEY environment variable.
            model (str, optional): The model name to use. Defaults to "llama-3.3-70b-versatile".

        Returns:
            None

        Raises:
            ValueError: If no API key is provided or found in the environment.
        """
        self.api_key = api_key or CUSTOMLEARN_GROQ_API_KEY
        self.model = model
        if not self.api_key:
            raise ValueError(
                "CUSTOMLEARN_GROQ_API_KEY is not set. Please set it in the environment variables."
            )

        self.llm = ChatGroq(model=self.model, temperature=0, groq_api_key=self.api_key)

    def get_model(self):
        """
        Returns the ChatGroq model instance.

        Args:
            None

        Returns:
            ChatGroq: The instantiated ChatGroq model object.
        """
        return self.llm