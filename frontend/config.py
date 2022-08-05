import os

# data directory
DATA_DIR = "../data/images"

# client
TOP_K = 10
DEBUG = True

# serving via REST
SERVER = os.getenv("SERVER", "https://0df596d980.wolf.jina.ai")