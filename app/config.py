import os 
from dotenv import load_dotenv

load_dotenv()

# ids 
CLIENT_ID = os.getenv("CLIENT_ID")
CUSTOMLEARN_GROQ_API_KEY = os.getenv("CUSTOMLEARN_GROQ_API_KEY")

# prompts
COURSE_GEN_PROMPT_NAME = "course_gen_prompt"

# url 
BASE_URL = os.getenv("BASE_URL")

# database
MONGODB_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("DB_NAME")
