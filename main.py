from plant_care.logger import logger
from plant_care.pipeline.stage01_data_ingestion import DataIngestionPipeline
from plant_care.pipeline.stage02_prepare_base_model import PrepareBaseModelPipeline
from plant_care.pipeline.stage03_prepare_callback import PrepareCallbackPipeline

# STAGE_NAME = "Data Ingestion"
# try:
#     logger.info(f">>>>>>>>> Stage {STAGE_NAME} Started <<<<<<<<<<<<<< ")
#     obj = DataIngestionPipeline()
#     obj.main()
#     logger.info(f">>>>>>>>> Stage {STAGE_NAME} Ended <<<<<<<<<<<<<< ")
#     logger.info("x=============x")
# except Exception as e:
#     logger.error(e)
#     raise e

# STAGE_NAME = "Preapare Base Model"
# try:
#     logger.info(f">>>>>>>>> Stage {STAGE_NAME} Started <<<<<<<<<<<<<< ")
#     obj = PrepareBaseModelPipeline()
#     obj.main()
#     logger.info(f">>>>>>>>> Stage {STAGE_NAME} Ended <<<<<<<<<<<<<< ")
#     logger.info("x=============x")
# except Exception as e:
#     logger.error(e)
#     raise e

STAGE_NAME = "Preapare Callback"
try:
    logger.info(f">>>>>>>>> Stage {STAGE_NAME} Started <<<<<<<<<<<<<< ")
    obj = PrepareCallbackPipeline()
    obj.main()
    logger.info(f">>>>>>>>> Stage {STAGE_NAME} Ended <<<<<<<<<<<<<< ")
    logger.info("x=============x")
except Exception as e:
    logger.error(e)
    raise e


