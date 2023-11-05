
from plant_care import logger
from plant_care.components.training import Training
from plant_care.components.prepare_callback import PrepareCallback
from plant_care.config.configuration import ConfigurationManager

STAGE_NAME = "Training Model"
class TrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
          config1 = ConfigurationManager()
          
          prepare_callback_config = config1.get_prepare_callback_config()
          prepare_callback = PrepareCallback(config = prepare_callback_config)
          callbacks = prepare_callback.get_tb_ckpt_callbacks(['potato','tomato'])
        
          training_config = config1.get_training_config()
          training = Training(config=training_config)
          training.get_base_model(['potato', 'tomato'])
          training.train_valid_generator(['potato', 'tomato'])
          training.train(
            callbacks = callbacks,
            names = ['potato', 'tomato']
          )
        except Exception as e:
          raise e
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>> Stage {STAGE_NAME} Started <<<<<<<<<<<<<< ")
        obj = TrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>> Stage {STAGE_NAME} Ended <<<<<<<<<<<<<< ")
        logger.info("x=============x")
    except Exception as e:
        raise e  