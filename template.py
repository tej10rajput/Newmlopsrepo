import os
import logging
from pathlib import Path

list_of_files = [".github/workflows",
"src/__init__.py",
"src/compomemts/__init__.py",
"src/components/data_ingestion.py",
"src/components/data_transformation.py",
"src/components/model_trainer.py",
"src/components/model_eavaluation.py",
"src/pipeline/__init__.py",
"src/pipeline/training_pipeline.py",
"src/pipeline/prediction_pipeline.py",
"src/utils/utils.py",
"src/logger/logging.py",
"src/exception/exception.py",
"tests/unit/__init__.py",
"tests/integration/__init__.py",
"init_setup.bat",
"requirements.txt",
"requirements_dev.txt",
"setup.py",
"setup.cfg",
"pyproject.toml",
"tox.ini",
"experiments/experimets.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory:{filedir}for file:{filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass # creates empty file