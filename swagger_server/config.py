import os

searching_path_env = os.getenv('SEARCHING_PATH')

if searching_path_env:
    SEARCHING_PATH = searching_path_env
else:
    SEARCHING_PATH = os.path.dirname(os.path.abspath(__file__))
