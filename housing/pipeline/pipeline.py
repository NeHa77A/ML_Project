from housing.config.configuration import Configuration
from housing.logger import logging
from housing.exception import HousingException
from housing.entity.artifact_entity import DataIngestionArtifact
from housing.entity.config_entity import DataIngestionConfig
import os, sys
from housing.component.data_ingestion import DataIngestion


class Pipeline:
    def __init__(self,config: Configuration=Configuration()) -> None:
        try:
            self.config = config
        except Exception as e:
            raise HousingException(e,sys) from e
        
    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise HousingException(e, sys) from e 