import os
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)

list_of_files = [
    '.github/workflow/.gitkeep',
    'src/__init__.py',
    'src/components/__init__.py',
    'src/utils/__init__.py',
    'src/config/__init__.py',
    'src/config/configuration.py',
    'src/pipeline/__init__.py',
    'src/entity/__init__.py',
    'src/constants/__init__.py',
    'config/config.yaml',
    'dvc.yaml',
    'params.yaml',
    'requirement.txt',
    'setup.py',
    'research/potato_research.py',
    'research/potato_model.py',
    'research/tomato_research.py',
    'research/tomato_model.py',
]

for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)

    if file_dir != '':
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating Directory {file_dir} for the file {file_name}")
    
    if (not os.path.exists(file_path)):
        with open(file_path, "w") as f:
            logging.info(f"Creating File '{file_name}'")
    