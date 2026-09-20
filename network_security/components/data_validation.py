from network_security.entity.artifact_entity import DataIngestionArtifacts, DataValidationArtifact
from network_security.entity.config_entity import DataValidationConfig
from network_security.exception.exception import NetworkSecurityException
from network_security.constants.training_pipeline import SCHEMA_FILE_PATH
from network_security.logging.logger import logging
from scipy.stats import ks_2samp

import os,sys
import numpy as np
import pandas as pd


class DataValidation:
    def __init__(self, data_ingestion_artifact:DataIngestionArtifacts, data_validation_config:DataValidationConfig):

        try:
            self.data_ingestion_artifact=data_ingestion_artifact
            self.data_validation_config=data_validation_config
            self.schema_config = read_yaml_file(SCHEMA_FILE_PATH)

        except Exception as e:
            raise NetworkSecurityException(e, sys)    