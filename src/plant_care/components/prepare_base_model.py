import tensorflow as tf
import keras
from keras.layers import Flatten, Dense
from keras.models import Model
from pathlib import Path
from box import config_box

from dataclasses import dataclass
from pathlib import Path
from box import ConfigBox

@dataclass(frozen=True)
class PrepareBaseModelConfig:
  root_dir: Path
  base_model_path: ConfigBox
  model_dir: ConfigBox
  updated_model_path: ConfigBox
  params_image_size: ConfigBox
  params_classes: ConfigBox
  params_include_top: bool
  params_weights: str

class PrepareBaseModel:
  def __init__(self, config: PrepareBaseModelConfig):
    self.config = config
  
  def get_base_model(self, names) :
    self.base_model = ConfigBox()
    for name in names:
      model = keras.applications.InceptionV3(
        input_shape = self.config.params_image_size[f"{name}"],
        include_top = self.config.params_include_top,
        weights =  self.config.params_weights
      )
      self.base_model[f'{name}'] = model
      # self.save_model(path=self.config.base_model_path[f"{name}"], model=model)
    
  @staticmethod
  def save_model(path: Path, model: keras.Model) :
    model.save(path)
    
  @staticmethod
  def _prepare_base_model(model, classes) :
    for layer in model.layers:
      layer.trainable=False
      
    x = Flatten()(model.output)
    pred = Dense(classes, activation='softmax')(x)
    full_model = Model(inputs=model.input, outputs=pred)

    full_model.compile(
      loss='categorical_crossentropy',
      optimizer='adam',
      metrics=['accuracy']
    )

    full_model.summary()
    return full_model
    
  def updated_base_model(self, name: list) :
    self.updated_models = ConfigBox()
    for i in name:
      model = self._prepare_base_model(
        model = self.base_model[f"{i}"],
        classes = self.config.params_classes[f"{i}"]
      )

      self.updated_models[f"{i}"] = model
      self.save_model(path = self.config.updated_model_path[f"{i}"], model=model)