import logging
import uvicorn

log_config = uvicorn.config.LOGGING_CONFIG
LOG_FORMAT = "%(levelprefix)s - %(asctime)s - %(message)s"
log_config["formatters"]["access"]["fmt"] = LOG_FORMAT
log_config["formatters"]["default"]["fmt"] = LOG_FORMAT
log_config["disable_existing_loggers"] = False

logger = logging.getLogger("uvicorn")
