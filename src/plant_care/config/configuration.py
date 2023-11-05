import os
from plant_care.constants import *
from plant_care.utils.main_utils import load_json
from plant_care.utils.main_utils import create_directories
from plant_care.components.training import TrainingConfig
from plant_care.components.data_ingestion import DataIngestionConfig
from plant_care.components.prepare_callback import PrepareCallbackConfig
from plant_care.components.prepare_base_model import PrepareBaseModelConfig

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
        data_dir = curr_config.data_dir
    )

    return data_ingestion_config

  def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
    curr_config = self.config.prepare_base_model
    curr_params = self.params
    create_directories([curr_config.root_dir])

    prepare_base_model_config = PrepareBaseModelConfig(
      root_dir = Path(curr_config.root_dir),
      model_dir = curr_config.model_dir,
      base_model_path = curr_config.base_model_path,
      updated_model_path = curr_config.updated_model_path,
      params_include_top = curr_params.INCLUDE_TOP,
      params_image_size = curr_params.IMAGE_SIZE,
      params_weights = curr_params.WEIGHTS,
      params_classes = curr_params.CLASSES
    )

    return prepare_base_model_config
  
  def get_prepare_callback_config(self) -> PrepareCallbackConfig:
    curr_config = self.config.prepare_callbacks
    model_ckpt_dir = []
    for model in curr_config.checkpoint_model_filepath:
      dir = curr_config.checkpoint_model_filepath[f"{model}"]
      dir = os.path.dirname(dir)
      model_ckpt_dir.append(dir)

    model_tb_dir = []
    for model in curr_config.tensorboard_root_log_dir:
      dir = curr_config.tensorboard_root_log_dir[f"{model}"]
      model_tb_dir.append(dir)

    create_directories(model_ckpt_dir)
    create_directories(model_tb_dir)

    prepare_callback_dir = PrepareCallbackConfig (
        root_dir = curr_config.root_dir,
        tensorboard_root_log_dir = curr_config.tensorboard_root_log_dir,
        checkpoint_model_filepath = curr_config.checkpoint_model_filepath
    )

    return prepare_callback_dir
  
  def get_training_config(self) -> TrainingConfig:
    training = self.config.training
    params = self.params
    create_directories([training.root_dir])

    training = TrainingConfig(
      root_dir = training.root_dir,
      trained_model_path = training.trained_model_path,
      updated_model_path = self.config.prepare_base_model.updated_model_path,
      trainning_data = self.config.data_ingestion.data_dir,
      params_epochs = params.EPOCHS,
      params_batch_size = params.BATCH_SIZE,
      params_target_size = params.TARGET_SIZE,
      params_class_mode = params.CLASS_MODE
    )

    return training