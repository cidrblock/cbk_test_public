""" This just a starter script
"""
from cbkutils.settings import Settings
from cbkutils.log import cbklogger
from cbkutils.utils import ppc, title
from cbkutils.status import Status
import time

SETTINGS = Settings('settings.yml')
LOGGER = cbklogger(SETTINGS)

def print_settings():
    """ Pretty print the settings
    """
    title("PRETTY PRINT OBJECTS")
    ppc(SETTINGS)

def individual_settings():
    """ Use some individual settings
    """
    title("REFERENCE NESTED SETTING")
    LOGGER.info("qua is %s" % SETTINGS.foo.bar.baz.qux.quux.garply.waldo.fred.plugh.xyzzy.thud )

def log_stuff():
    """ Log some information
    """
    title("LOG TO CONSOLE AND FILE")
    LOGGER.info("This is informational")
    LOGGER.warning("This is a warning")
    LOGGER.error("This is an error")
    LOGGER.critical("This is critical")
    something = {"foo": "bar"}
    message = "Debug something.  something is %s" % something
    LOGGER.debug(message)

def sample_comment(var_a, var_b, var_c="example"):
    """ The descirption goes here.

    If you need a bigger explaination, put it here.

    Args:
        var_a (list): A list of stuff
        var_b (dict): A dict of stuff
        var_c (string): An optional string

    Returns:
        dict: A dictionary combining all the vars

    """
    title("USE A FUNCTION")
    status = Status("Return value to caller")
    status.end("Pending", "pending")
    return {"var_a": var_a, "var_b": var_b, "var_c": var_c}

def feedback():
    """ Provide some realtime feedback to the user
    """
    title("GIVE FEEDBACK DURING EXECUTION")
    status = Status("Prepare to send feedback")
    time.sleep(2)
    status.end("pending", 'pending')
    status = Status("Doing some work")
    time.sleep(2)
    status.end("100/100", 'ok')
    status = Status("Doing some work")
    time.sleep(2)
    status.end("issue found", 'warning')
    status = Status("Doing some work")
    time.sleep(2)
    status.end("fatal error", 'fail')
    status = Status("Feedback sent")
    time.sleep(2)
    status.end("done", 'ok')

def main():
    """ This is the main entry point for our application
    """
    print_settings()
    individual_settings()
    log_stuff()
    var_a = [1, 2, 3, 4]
    var_b = {"foo": "bar"}
    ppc(sample_comment(var_a, var_b))
    status = Status("Returned value to caller")
    time.sleep(3)
    status.end("Done", "ok")
    feedback()


if __name__ == '__main__':
    main()
