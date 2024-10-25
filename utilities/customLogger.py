import logging
import os
from venv import logger


class LogGen:

    def loggen(self):
        curr_dir_path = os.path.dirname(os.path.realpath(__file__)) +"\\Logs\\"
        print(curr_dir_path)
        if os.access(curr_dir_path, os.W_OK):
            print(f"Directory '{curr_dir_path}' is writable.")
        else:
            print(f"Directory '{curr_dir_path}' is NOT writable.")

        # log_dir = "Logs"
        # if not os.path.exists(log_dir):
        #     os.makedirs(log_dir)

        print("wokring ")

        # Set up logging
        log_file = os.path.join("D:/python workspace/Python_selenium_Framework/SPAF/Logs", "automation.log")
        print(log_file)

        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,  # Log level
            format='%(asctime)s - %(levelname)s - %(message)s',  # Log message format
            datefmt='%Y-%m-%d %H:%M:%S'  # Date format in logs
        )


        logger = logging.getLogger()
        # Generate some logs
        logger.info("This is an info log message.")
        logger.warning("This is a warning log message.")
        logger.error("This is an error log message.")

        print(f"Logs have been written to {log_file}")
        return logger


# l = LogGen()
# l.loggen()
