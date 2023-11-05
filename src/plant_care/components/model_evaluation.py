import os
from dataclasses import dataclass
from pathlib import Path
import tensorflow as tf
from box import ConfigBox

from plant_care.logger import logger
from plant_care.utils.main_utils import save_json
from keras.preprocessing.image import ImageDataGenerator

@dataclass(frozen=True)
class ModelEvaluationConfig:
  path_of_model: ConfigBox
  data_dir: ConfigBox
  params_target_size: ConfigBox
  params_class_mode: ConfigBox
  params_batch_size: int

class ModelEvaluation:
  def __init__(self, config: ModelEvaluationConfig):
    self.config = config
  
  @staticmethod
  def load_model(path: Path) -> tf.keras.Model:
    return tf.keras.models.load_model(path)
  
  def test_generator(self, names: list) :
    self.test_set = ConfigBox()
    test_datagen = ImageDataGenerator(rescale=1./255)

    for name in names:
      self.test_set[f"{name}"] = test_datagen.flow_from_directory(
        os.path.join(self.config.data_dir[f"{name}"], "test"),
        target_size = self.config.params_target_size[f"{name}"],
        batch_size = self.config.params_batch_size,
        class_mode = self.config.params_class_mode[f"{name}"]                
      )
    
  def evaluation(self, names: list) :
    self.test_generator(names)
    self.model = ConfigBox()
    self.score = ConfigBox()
    for name in names:
      model = self.load_model(self.config.path_of_model[f"{name}"])
      score = model.evaluate(self.test_set[f"{name}"])
      self.score[f"{name}"] = {"loss": score[0], "accuracy": score[1]}
      self.model[f"{name}"] = model
    
    logger.info(self.score)
    save_json(path=Path("scores.json"), data=self.score)

