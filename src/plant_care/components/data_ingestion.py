from dataclasses import dataclass
from pathlib import Path
import zipfile
from box import ConfigBox

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_data_dir: Path
    unzip_dir: Path
    data_dir : ConfigBox

class DataIngestion:
    def __init__(self, config):
        self.config = config
    
    def extrct_zip_file(self):
        unzip_path = self.config.unzip_dir
        with zipfile.ZipFile(file=self.config.source_data_dir, mode='r') as zip:
            zip.extractall(unzip_path)
