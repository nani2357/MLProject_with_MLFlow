# Import necessary modules
import os
import sys
import logging

# Define a logging format string. This will determine the structure of the log messages.
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Define the directory where log files will be stored.
log_dir = "logs"

# Construct the full path to the log file within the log directory.
log_filepath = os.path.join(log_dir, "running_logs.log")

# Ensure the log directory exists. If it doesn't, create it.
os.makedirs(log_dir, exist_ok=True)

# Configure the logging settings.
logging.basicConfig(
    # Set the logging level to INFO. This means messages with level INFO and above will be logged.
    level=logging.INFO,
    
    # Apply the previously defined logging format.
    format=logging_str,

    # Define the logging handlers. 
    # FileHandler will write logs to a file, and StreamHandler will print logs to the console.
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

# Create a logger instance with a specific name.
logger = logging.getLogger("mlProjectLogger")
