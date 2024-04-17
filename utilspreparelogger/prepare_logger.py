from os import makedirs
from pathlib import Path
from logging import (
    getLogger,
    Formatter,
    StreamHandler,
    Logger,
)
from logging.handlers import (
    SysLogHandler,
    TimedRotatingFileHandler,
)

from .enum import EnumLogLevel, EnumLogHandler


class PrepareLogger:
    """
    A class that sets up a logger with customizable handlers for logging purposes.

    The `PrepareLogger` class allows you to configure and prepare a logger with various handlers for logging events.
    It provides flexibility in defining the logger's name, log level, log handlers, log format, and other settings.

    Args:
        name (str): The name of the logger.
        level (EnumLogLevel): The log level to set for the logger.
        handlers (list[EnumLogHandler]): A list of log handlers to attach to the logger.
        format_ (str, optional): The desired log message format. Defaults to a JSON format.

        timed_rotating_file_handler_input (dict, optional): Configuration for the TimedRotatingFileHandler.
        sys_log_handler (dict, optional): Configuration for the SysLogHandler.
        stream_handler (dict, optional): Configuration for the StreamHandler.

    Methods:
        perform(): Performs the logger setup and returns the configured logger.

    """

    def __init__(
            self,
            name: str,
            level: EnumLogLevel,
            handlers: list[EnumLogHandler],
            format_: str = '{"time":"%(asctime)s", "name": "%(name)s", "level": "%(levelname)s", '
                           '"function": "%(funcName)s", "message": "%(message)s"}',

            timed_rotating_file_handler_input: dict = None,
            sys_log_handler: dict = None,
            stream_handler: dict = None,
    ) -> None:
        self.name = name
        self.level = level.value.upper()
        self.handlers = handlers

        self.format = format_

        self.timed_rotating_file_handler_input = timed_rotating_file_handler_input or dict()
        self.sys_log_handler = sys_log_handler or dict()
        self.stream_handler = stream_handler or dict()

        self.app_logger = None
        self.prepared_handlers = list()

    def perform(self) -> Logger:
        """
        Performs the logger setup and returns the configured logger.

        This method performs the necessary steps to set up the logger according to the provided configurations.
        It initializes the logger, sets the log level, prepares the specified log handlers,
        sets the log formatter, adds the handlers to the logger, and returns the configured logger.

        Returns:
            app_logger: The configured logger object.

        """
        self._get_logger()
        self._set_level()
        self._prepare_handlers()
        self._set_formatter()
        self._add_handler_2_logger()
        return self.app_logger

    def _get_logger(self):
        """
        Initializes the logger object.

        This method initializes the logger object with the specified name.

        """
        self.app_logger = getLogger(self.name)

    def _set_level(self):
        """
        Sets the log level for the logger.

        This method sets the log level of the logger to the specified level.

        """
        self.app_logger.setLevel(self.level)

    def _prepare_handlers(self):
        """
        Prepares the specified log handlers.

        This method prepares the log handlers based on the specified list of handlers.
        It checks for specific handlers, such as file, syslog, and console, and prepares them accordingly.

        """
        if EnumLogHandler.file in self.handlers:
            self._prepare_file_handler()

        if EnumLogHandler.syslog in self.handlers:
            self._prepare_syslog_handler()

        if EnumLogHandler.console in self.handlers:
            self._prepare_console_handler()

    def _prepare_file_handler(self):
        """
        Prepares the TimedRotatingFileHandler.

        This method prepares the TimedRotatingFileHandler based on the provided configuration.
        It creates the necessary parent folders for the log file and adds the handler to the prepared handlers list.

        """
        self._create_parent_folders()

        handler = TimedRotatingFileHandler(**self.timed_rotating_file_handler_input)
        self.prepared_handlers.append(handler)

    def _create_parent_folders(self):
        """
        Creates parent folders for the log file.

        This method creates the necessary parent folders for the log file specified in the configuration.

        """
        log_dir = Path(self.timed_rotating_file_handler_input["filename"]).resolve().parent

        makedirs(
            log_dir,
            exist_ok=True,
        )

    def _prepare_syslog_handler(self):
        """
        Prepares the SysLogHandler.

        This method prepares the SysLogHandler based on the provided configuration.
        It adds the handler to the prepared handlers list.

        """
        handler = SysLogHandler(**self.sys_log_handler)
        self.prepared_handlers.append(handler)

    def _prepare_console_handler(self):
        """
        Prepares the StreamHandlerThis method prepares the StreamHandler based on the provided configuration.
        It adds the handler to the prepared handlers list.

        """
        handler = StreamHandler(**self.stream_handler)
        self.prepared_handlers.append(handler)

    def _set_formatter(self):
        """
        Sets the log formatter for the prepared handlers.

        This method sets the log formatter for each prepared handler based on the specified log format.

        """
        for handler in self.prepared_handlers:
            handler.setFormatter(Formatter(fmt=self.format))

    def _add_handler_2_logger(self):
        """
        Adds the prepared handlers to the logger.

        This method adds each prepared handler to the logger.

        """
        for handler in self.prepared_handlers:
            self.app_logger.addHandler(handler)