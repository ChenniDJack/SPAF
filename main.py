# import logging
# import os
#
# # Create Logs directory if it doesn't exist
# log_dir = "Logs"
# if not os.path.exists(log_dir):
#     os.makedirs(log_dir)
#
# # Set up logging
# log_file = os.path.join(log_dir, "sample.log")
#
# logging.basicConfig(
#     filename=log_file,
#     level=logging.INFO,  # Log level
#     format='%(asctime)s - %(levelname)s - %(message)s',  # Log message format
#     datefmt='%Y-%m-%d %H:%M:%S'  # Date format in logs
# )
#
# # Create a logger instance
# logger = logging.getLogger()
#
# # Generate some logs
# logger.info("This is an info log message.")
# logger.warning("This is a warning log message.")
# logger.error("This is an error log message.")
#
# print(f"Logs have been written to {log_file}")
