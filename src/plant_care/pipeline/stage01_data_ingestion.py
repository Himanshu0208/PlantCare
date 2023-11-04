
from plant_care.components.data_ingestion import DataIngestion
from plant_care.logger import logger
from plant_care.config.configuration import ConfigurationManager
from plant_care.components.data_ingestion import DataIngestionConfig

STAGE_NAME = "Data Ingestion"

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        config1 = ConfigurationManager()
        data_ingestion_config = config1.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.extrct_zip_file()

    
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>> Stage {STAGE_NAME} Started <<<<<<<<<<<<<< ")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>>>>> Stage {STAGE_NAME} Ended <<<<<<<<<<<<<< ")
        logger.info("x=============x")
    except Exception as e:
        logger.error(e)
        raise e