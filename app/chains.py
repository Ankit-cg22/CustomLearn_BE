import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from app.groq_client import GroqClient
from dotenv import load_dotenv
import yaml
from app.config import COURSE_GEN_PROMPT_NAME

load_dotenv()

class Chains:

    def __init__(self):
        """
        Initializes the Chains object by loading the language model and prompts.

        Args:
            None

        Returns:
            None
        """
        self.llm = GroqClient().get_model()
        self.prompts = self.load_prompts()

    @staticmethod
    def load_prompts():
        """
        Loads prompt configurations from the 'prompts.yml' file .

        Args:
            None

        Returns:
            dict: A dictionary containing the loaded prompts from the YAML file.
        """
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        prompts_path = os.path.join(base_dir,"app",  "prompts", "course_generation_prompts.yml")
        with open(prompts_path, "r") as file:
            prompts = yaml.safe_load(file)
        return prompts

    def get_prompt(self, key):
        """
        Fetches a specific prompt by key.

        Args:
            key (str): The key for the desired prompt.

        Returns:
            str: The prompt template string.

        Raises:
            Exception: If the key is not found in the prompts.
        """
        if key not in self.prompts:
            raise Exception(f"Prompt '{key}' not found in prompts.yml")
        return self.prompts[key]

    def get_course_plan(self, skill, current_knowledge=None, hours_per_week=None, no_of_weeks=None, learning_style=None, learning_goal=None):
        prompt_name = COURSE_GEN_PROMPT_NAME
        prompt_course_gen = PromptTemplate.from_template(self.get_prompt(prompt_name))
        chain_extract = prompt_course_gen | self.llm
        res = chain_extract.invoke(input={
            "skill": skill,
            "currentKnowledge": current_knowledge,
            "hoursPerWeek": hours_per_week,
            "noOfWeeks": no_of_weeks,
            "learningStyle": learning_style,
            "learningGoal": learning_goal
        })
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse data.")
        return res
