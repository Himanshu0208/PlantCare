
from plant_care import logger
from plant_care.components.model_evaluation import ModelEvaluation
from plant_care.config.configuration import ConfigurationManager

STAGE_NAME = "Model Evaluation Model"
class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config1 = ConfigurationManager()
            val_config = config1.get_model_evaluation_config()
            evaluation = ModelEvaluation(config=val_config)
            evaluation.evaluation(['potato', 'tomato'])
        except Exception as e:
           raise e
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>> Stage {STAGE_NAME} Started <<<<<<<<<<<<<< ")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>>> Stage {STAGE_NAME} Ended <<<<<<<<<<<<<< ")
        logger.info("x=============x")
    except Exception as e:
        raise e  