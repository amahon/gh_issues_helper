
import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
GITHUB_USERNAME = os.environ.get("GITHUB_USERNAME")
GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN")
GITHUB_REPOSITORY = os.environ.get("GITHUB_REPOSITORY")
ZENHUB_API_TOKEN = os.environ.get("ZENHUB_API_TOKEN")
PORT = os.environ.get("PORT")
