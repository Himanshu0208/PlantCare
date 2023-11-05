import os
import keras
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator, load_img

from dataclasses import dataclass
from box import ConfigBox
from pathlib import Path

@dataclass(frozen=True)
class TrainingConfig:
  root_dir: Path
  trained_model_path: ConfigBox
  updated_model_path: ConfigBox
  trainning_data: ConfigBox
  params_epochs: int
  params_batch_size: int
  params_target_size: ConfigBox
  params_class_mode: ConfigBox


class Training:
  def __init__(self, config: TrainingConfig) :
    self.config = config
  
  def get_base_model(self, names: list) :
    self.model = ConfigBox()
    for name in names:
      self.model[f"{name}"] = keras.models.load_model(
          self.config.updated_model_path[f"{name}"]
      )
    
  def train_valid_generator(self, names: list) :
    self.valid_set = ConfigBox()
    self.train_set = ConfigBox()
    self.test_set = ConfigBox()

    train_datagen = ImageDataGenerator(
      rescale=1./255,
      shear_range=0.2,
      zoom_range=0.2,
      horizontal_flip=True
    )

    valid_datagen = ImageDataGenerator(rescale=1./255)

    test_datagen = ImageDataGenerator(rescale=1./255)

    for name in names:
      print(os.path.join(self.config.trainning_data[f"{name}"], "train"))
      print(os.path.join(self.config.trainning_data[f"{name}"], "valid"))
      print(os.path.join(self.config.trainning_data[f"{name}"], "test"))


      self.train_set[f"{name}"] = train_datagen.flow_from_directory(
          os.path.join(self.config.trainning_data[f"{name}"], "train"),
          target_size = tuple(self.config.params_target_size[f"{name}"]),
          batch_size = self.config.params_batch_size,
          class_mode = self.config.params_class_mode[f"{name}"]
      )

      self.valid_set[f"{name}"] = valid_datagen.flow_from_directory(
          os.path.join(self.config.trainning_data[f"{name}"], "valid"),
          target_size = tuple(self.config.params_target_size[f"{name}"]),
          batch_size = self.config.params_batch_size,
          class_mode = self.config.params_class_mode[f"{name}"]         
      )

      self.valid_set[f"{name}"] = test_datagen.flow_from_directory(
          os.path.join(self.config.trainning_data[f"{name}"], "test"),
          target_size = tuple(self.config.params_target_size[f"{name}"]),
          batch_size = self.config.params_batch_size,
          class_mode = self.config.params_class_mode[f"{name}"]                
      )
    
  def train(self, callbacks: ConfigBox, names: list):
    self.callbacks = ConfigBox()
    
    for name in names:
      self.callbacks[f"{name}"] = [callbacks.tensorboard_callback[f"{name}"], callbacks.checkpoint_callback[f"{name}"]]

    for name in names:
      self.model[f"{name}"].fit(
          self.train_set[f"{name}"],
          validation_data=self.valid_set[f"{name}"],
          epochs=self.config.params_epochs,
          steps_per_epoch=len(self.train_set[f"{name}"]),
          validation_steps=len(self.valid_set[f"{name}"]),
          callbacks=self.callbacks[f"{name}"]
      )

      self.save_model(path=self.config.trained_model_path[f"{name}"] , model=self.model[f"{name}"])
    
  @staticmethod
  def save_model(path: Path, model: keras.Model) :
    model.save(path)