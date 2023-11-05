from plant_care import logger
from plant_care.components.prepare_callback import PrepareCallback
from plant_care.config.configuration import ConfigurationManager

STAGE_NAME = "Prepare Callback"
class PrepareCallbackPipeline:
    def __init__(self):
        pass

    def main(self) :
        try:
          config1 = ConfigurationManager()
          prepare_callback_config = config1.get_prepare_callback_config()
          prepare_callback = PrepareCallback(config = prepare_callback_config)
          prepare_callback.get_tb_ckpt_callbacks(['potato','tomato'])
        except Exception as e:
          raise e
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>> Stage {STAGE_NAME} Started <<<<<<<<<<<<<< ")
        obj = PrepareCallbackPipeline()
        obj.main()
        logger.info(f">>>>>>>>> Stage {STAGE_NAME} Ended <<<<<<<<<<<<<< ")
        logger.info("x=============x")
    except Exception as e:
        raise e   
        
