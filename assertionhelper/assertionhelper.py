import logging
from typing import Any, Optional

def assert_type(x: Any, expected_class, msg: Optional[str]=None):
    """
    Asserts that x is of type expected_class, else rasies TypeError and
    logs an error msg.
    
    :param msg: can be used to additionally log a message at the
        logging.ERROR level. The message will also be added to the TypeError
        message.
        
    :example:
    
    ::
    
        def square_an_integer(x: int) -> int:
            assert_type(x, int)
            return x * x
            
        square_an_integer(4.5)
        
    will log
    
    ``ERROR:root:4.5 has unexpected type <class 'float'>: expected
    <class 'int'>``
    """
    if not isinstance(x, expected_class):
        error_msg = "{} has unexpected type {}: expected {}".format(
            x, type(x), expected_class)
        logging.error(error_msg)
        
        if msg is not None:
            error_msg += "\n" + msg
            logging.error(msg)
            
        raise TypeError(error_msg)
