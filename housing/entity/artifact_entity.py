from collections import namedtuple


# this is output file
DataIngestionArtifact = namedtuple("DataIngestionArtifact",["train_file_path","test_file_path","is_ingested","message"])
