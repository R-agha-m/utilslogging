from logging import getLogger, FileHandler, StreamHandler
from sys import stdout
from os.path import normpath, realpath, dirname
from os import makedirs

try:
    from .custom_formatter import CustomFormatter
    from .db_logger.handlers import DBHandler
except ImportError:
    from custom_formatter import CustomFormatter
    from db_logger.handlers import DBHandler


# todo: use dic config formatter and other logging handlers

class CreateLogger:

    def __init__(self,
                 name: str = 'log',
                 loggers_data=({"format": '%(asctime)s: %(funcName)s: \t\t%(message)s',
                                "destinations": "console",
                                "level": 10,
                                "handler_args": tuple(),
                                "handler_kwargs": dict()},

                               {"format": '%(asctime)s: %(funcName)s: \t\t%(message)s',
                                "destinations": "log.log",
                                "level": 10,
                                "handler_args": tuple(),
                                "handler_kwargs": dict()},

                               {"format": '%(asctime)s: %(funcName)s: \t\t%(message)s',
                                "destinations": "db",
                                "level": 10,
                                "handler_args": tuple(),
                                "handler_kwargs": dict()})):

        self.name = name
        self.loggers_data = loggers_data

        self.logger = None
        self.format = None
        self.destination = None
        self.level = None
        self.handler_args = None
        self.handler_kwargs = None

    def perform(self):
        self.logger = getLogger(self.name)

        for loggers_data_i in self.loggers_data:
            self.format = loggers_data_i["format"]
            self.destination = loggers_data_i["destinations"]
            self.level = loggers_data_i["level"]
            self.handler_args = loggers_data_i["handler_args"]
            self.handler_kwargs = loggers_data_i["handler_kwargs"]

            self._add_handler()

            self.logger.setLevel(self.level)

        return self.logger

    def _add_handler(self):
        if self.destination in ('stdout', 'console',):
            self._add_console_handler()
        elif self.destination in ('db_handler', 'db',):
            self._add_db_handler()
        else:
            self._add_file_handler()

    def _add_file_handler(self):
        self._create_logger_folder()
        file_handler = FileHandler(self.destination,
                                   encoding="utf-8")
        file_handler.setFormatter(CustomFormatter(self.format))
        self.logger.addHandler(file_handler)

    def _add_console_handler(self):
        console_handler = StreamHandler(stdout)
        console_handler.setFormatter(CustomFormatter(self.format))
        self.logger.addHandler(console_handler)

    def _add_db_handler(self):
        self.logger.addHandler(DBHandler(*self.handler_args,
                                         level=self.level,
                                         **self.handler_kwargs))

    def _create_logger_folder(self):
        destination_name = dirname(self.destination)
        makedirs(destination_name, exist_ok=True)
