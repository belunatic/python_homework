def logger_decorator(func):
    import logging
    # Creates (or retrieves) a named logger.
    # The name is built from the module’s name (__name__) plus "_parameter_log".
    # in our case it is "log_decorator_parameter_log"
    logger = logging.getLogger(__name__ + "_parameter_log") 
    logger.setLevel(logging.INFO)
    # All log messages will be written to the file decorator.log
    # logger.handlers tells you how many output channels your logger is using, and checking it prevents duplicate logging.
    ## next line we checking to see if a handler is already registered
    ## preventing duplication in the decorator.log
    if not logger.handlers:
        logger.addHandler(logging.FileHandler("./decorator.log","a"))

    def wrapper(*args,**kwargs):
        #write to the log records
        logger.log(logging.INFO, f"function: {func.__name__}")
        if args:
            logger.info(f"positional parameters: {list(args)}")
        else:
            logger.info("positional parameters: none")

        if kwargs:
            logger.info(f"keyword parameters: {dict(kwargs)}")
        else:
            logger.info("keyword parameters: none")

        result = func(*args,**kwargs)
        logger.log(logging.INFO, f"return: {result}")
        
        return result

    return wrapper

@logger_decorator
def print_hello():
    print('Hello World')

@logger_decorator
def args_func(*args):
    return True

@logger_decorator
def keyword_func(**kwargs):
    return logger_decorator

print_hello()
args_func(1,2,3,4,5)
keyword_func(name='Abel',neck='wide',age=30)