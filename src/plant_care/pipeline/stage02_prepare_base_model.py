from plant_care.logger import logger
from plant_care.config.configuration import ConfigurationManager
from plant_care.components.prepare_base_model import PrepareBaseModel
from plant_care.components.prepare_base_model import PrepareBaseModelConfig

STAGE_NAME = "Prepare Base Model"

class PrepareBaseModelPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config1 = ConfigurationManager()
            prepare_base_model_config = config1.get_prepare_base_model_config()
            prepare_base_model = PrepareBaseModel(config = prepare_base_model_config)
            prepare_base_model.get_base_model(['potato', 'tomato'])
            prepare_base_model.updated_base_model(['potato', 'tomato'])
        except Exception as e:
            raise e      


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>> Stage {STAGE_NAME} Started <<<<<<<<<<<<<< ")
        obj = PrepareBaseModelPipeline()
        obj.main()
        logger.info(f">>>>>>>>> Stage {STAGE_NAME} Ended <<<<<<<<<<<<<< ")
        logger.info("x=============x")
    except Exception as e:
        raise e    