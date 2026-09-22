from network_security.components.data_ingestion import DataIngestion
from network_security.components.data_validation import DataValidation
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging
from network_security.entity.config_entity import DataIngestionConfig, DataValidationConfig, TrainingPipelineConfig
import sys



if __name__ == "__main__":
    try:
        trainingPipelineConfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(training_pipeline_config=trainingPipelineConfig)
        dataingestion = DataIngestion(data_ingestion_config=dataingestionconfig)
        logging.info("initiate data ingestion")
        
        dataingestionartifacts = dataingestion.initiate_data_ingestion()
        print(dataingestionartifacts)
        datavalidationconfig = DataValidationConfig(training_pipeline_config=trainingPipelineConfig)
        data_validation = DataValidation(data_ingestion_artifact= dataingestionartifacts, data_validation_config= datavalidationconfig)
        logging.info("initiate data ingestion")
        data_validation_artifacts = data_validation.initiate_data_validation()
        print(data_validation_artifacts)
        logging.info("data validation completed")
        
        
    except Exception as e:
        raise NetworkSecurityException(e, sys)
