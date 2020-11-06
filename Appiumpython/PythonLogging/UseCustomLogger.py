import logging
import  PythonLogging.CustomLogger as cl

class CustomLoggerDemo():
    log = cl.customLogger()

    def methodOne(self):

        self.log.critical("This is a critical message.")
        self.log.error("This is an error message.")
        self.log.info("This is an info message.")
        self.log.warning("This is a warning message.")
        self.log.debug("This is a debug message.")

    def methodTwo(self):

        m2 = cl.customLogger()
        m2.critical("This is a critical message.")
        m2.error("This is an error message.")
        m2.info("This is an info message.")
        m2.warning("This is a warning message.")
        m2.debug("This is a debug message.")

runlog = CustomLoggerDemo()
runlog.methodOne()
runlog.methodTwo()