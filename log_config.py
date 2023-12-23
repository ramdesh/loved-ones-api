import logging.config
import os


def get_logger():
    log_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "simple": {
                "format": "[%(asctime)s] [%(levelname)s] [%(name)s] "
                "[%(module)s:%(lineno)d] %(message)s"
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "simple",
                "stream": "ext://sys.stdout",
            }
        },
        "loggers": {
            "loved_ones": {
                "level": os.getenv("LOG_LEVEL", "INFO"),
                "handlers": ["console"],
            }
        },
    }
    logging.config.dictConfig(log_config)
    return logging.getLogger("loved_ones")
