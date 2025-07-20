import logging

def get_logger(source_name):
    logger = logging.getLogger(source_name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '[%(asctime)s] [%(levelname)s] [%(source)s] [%(module)s.%(funcName)s] '
            '[user_id=%(user_id)s req_id=%(req_id)s] [status=%(status)s] duration=%(duration)sms - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.propagate = False
    return logger
