from plant_care.logger import logger
from plant_care.pipeline.stage01_data_ingestion import DataIngestionPipeline

STAGE_NAME = "Data Ingestion"
try:
    logger.info(f">>>>>>>>> Stage {STAGE_NAME} Started <<<<<<<<<<<<<< ")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>>>>> Stage {STAGE_NAME} Ended <<<<<<<<<<<<<< ")
    logger.info("x=============x")
except Exception as e:
    logger.error(e)
    raise e