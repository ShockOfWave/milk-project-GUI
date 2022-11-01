import os
from pathlib import Path

def get_project_path() -> str:
    """
    :return:
    project path
    """
    return Path(__file__).parent.parent.parent

def get_models_path() -> str:
    """
    :return:
    models path
    """
    path_to_model = os.path.join(Path(__file__).parent.parent, 'evaluation')
    return path_to_model

PATH_TO_UI_FILE = os.path.join(get_project_path(), 'MilkApp', 'GUI', 'GUI.ui')
PATH_TO_PROJECT = get_project_path()

PATH_TO_IVIUM_16_ANTIBIOTICS_MODELS = os.path.join(get_models_path(), 'IviumData_results_2022-09-09')
PATH_TO_IVIUM_5_ANTIBOITICS_MODELS = os.path.join(get_models_path(), 'ivium_new_data_results_2022-09-09')
