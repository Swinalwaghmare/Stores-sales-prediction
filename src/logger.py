import logging
from datetime import datetime
import os

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

LOG_DIR = os.path.join(os.getcwd(),'logs')

os.makedirs(LOG_DIR,exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    filemode='w',
    format="[%(asctime)s] %(lineno)d %(name)s %(levelname)s %(message)s",
    level=logging.INFO
)









































