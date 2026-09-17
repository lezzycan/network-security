from network_security.components.data_ingestion import DataIngestion
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging
from network_security.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
import sys



if __name__ == "__main__":
    try:
        trainingPipelineConfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(training_pipeline_config=trainingPipelineConfig)
        dataingestion = DataIngestion(data_ingestion_config=dataingestionconfig)
        logging.info("initiate data ingestion")
        dataingestionartifacts = dataingestion.initiate_data_ingestion()
        print(dataingestionartifacts)
    except Exception as e:
        raise NetworkSecurityException(e, sys)
