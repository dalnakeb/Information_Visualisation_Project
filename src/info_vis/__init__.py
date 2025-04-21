from pathlib import Path

PROJECT_PATH = Path(__file__).parent.parent.parent.absolute()
DATA_PATH = PROJECT_PATH / "data"
PREPROCESSED_DATA_PATH = DATA_PATH / "preprocessed"
