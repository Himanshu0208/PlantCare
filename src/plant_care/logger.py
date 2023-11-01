import logging
import os
import sys
from datetime import datetime


LOG_DIR = "logs"
LOG_FILE_PATH = os.path.join(LOG_DIR,"running_logs.log")
os.makedirs(LOG_DIR, exist_ok=True)

LOG_STR = "[%(asctime)s: %(levelname)s: %(module)s: %(lineno)d: %(message)s]"

logging.basicConfig(
  format=LOG_STR,
  level=logging.INFO,
  handlers=[
      logging.FileHandler(LOG_FILE_PATH),
      logging.StreamHandler(sys.stdout),
  ]
)

logger = logging.getLogger('PlantCareLogger')