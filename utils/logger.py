import logging
import os

# Ensure the logs directory exists
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Configure logging
LOG_FILE = os.path.join(LOG_DIR, "test_execution.log")
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_logger():
    return logging.getLogger(__name__)
