import time
import os 
import keras
from dataclasses import dataclass
from pathlib import Path
from box import ConfigBox

@dataclass(frozen=True)
class PrepareCallbackConfig:
  root_dir: Path
  tensorboard_root_log_dir : ConfigBox
  checkpoint_model_filepath : ConfigBox

class PrepareCallback:
  def __init__(self, config: PrepareCallbackConfig):
    self.config = config
  

  def _create_tb_callback(self, names: list):
    timestamp = time.strftime("%H-%M-%S--[%d-%m-%Y]")
    tensorboard_callback = ConfigBox()
    for name in names:
      tb_running_log_dir = os.path.join(
        self.config.tensorboard_root_log_dir[f"{name}"],
        f"{timestamp}"
      )
      tensorboard_callback[f"{name}"] = keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)
    
    return tensorboard_callback
  

  def _create_ckpt_callback(self, names: list):
    checkpoint_callback = ConfigBox()
    
    for name in names:
      callback = keras.callbacks.ModelCheckpoint(
          filepath=self.config.checkpoint_model_filepath[f"{name}"],
          save_best_only = True,
      )

      checkpoint_callback[f"{name}"] = callback

    return checkpoint_callback
  
  def get_tb_ckpt_callbacks(self, name: list) :
    tensorboard_callback = self._create_tb_callback(name)
    checkpoint_callback = self._create_ckpt_callback(name)

    return ConfigBox({
        "tensorboard_callback" : tensorboard_callback,
        "checkpoint_callback" : checkpoint_callback
    })
      