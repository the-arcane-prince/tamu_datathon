import pytest
from dotenv import load_dotenv

@pytest.fixture(scope="session", autouse=True)
def load_env():
    print("Loaded Enviornment Variables from .dotenv")
    load_dotenv()