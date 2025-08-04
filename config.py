import os
from dotenv import load_dotenv

load_dotenv()

SERPER_API_KEY = os.getenv("SERPER_API_KEY")
SERPER_BASE_URL = os.getenv("https://google.serper.dev/places")

OUTPUT_FILE_DIR = os.getenv("OUTPUT_FILE_DIR", "./OutputFile/")
OUTPUT_FILE_CENTRAL_SOURCE = os.getenv("OUTPUT_FILE_Central_Source", "./OutputFile/Final/")
OUTPUT_FILE_States_SOURCE = os.getenv("OUTPUT_FILE_States_Source", "./OutputFile/States/")


