from plant_care.constants import *
from plant_care.utils.main_utils import load_json
from plant_care.utils.main_utils import create_directories
from plant_care.components.data_ingestion import DataIngestionConfig

class ConfigurationManager:
  def __init__(self, config=CONFIG_FILE_PATH, params=PARAM_FILE_PATH):
    self.config = load_json(config)
    self.params = load_json(params)

    create_directories([self.config.artifact_root])
  
  def get_data_ingestion_config(self) -> DataIngestionConfig:
    curr_config = self.config.data_ingestion
    create_directories([curr_config.root_dir])

    data_ingestion_config = DataIngestionConfig(
        root_dir = curr_config.root_dir,
        source_data_dir = curr_config.source_data_dir,
        unzip_dir= curr_config.unzip_dir,
        data_dir = curr_config.data_dir
    )

    return data_ingestion_config