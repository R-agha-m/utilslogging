from os import environ

# todo: This utils is too complicated. Make it simple.


class Setting:
    _container_name = None
    _app_name = None
    _debug_mode = None
    _report = None
    _time_out = None
    _max_try = None
    _poll_frequency = None
    _implicit_wait_time = None
    _log_db = None

    @property
    def CONTAINER_NAME(self):
        if self._container_name is None:
            self._container_name = environ.get("CONTAINER_NAME",
                                               "localhost")
        return self._container_name

    @property
    def APP_NAME(self):
        if self._app_name is None:
            self._app_name = environ.get("APP_NAME",
                                         "utils_logging")
        return self._app_name

    @property
    def DEBUG_MODE(self):
        if self._debug_mode is None:
            from utils_common.detect_boolean import detect_boolean
            self._debug_mode = detect_boolean(
                environ.get("DEBUG_MODE",
                            True))
        return self._debug_mode

    @property
    def report(self):
        if self._debug_mode is None:
            try:
                from .get_or_create_logger import get_or_create_logger
            except ImportError:
                from get_or_create_logger import get_or_create_logger

            self._report = get_or_create_logger(
                destinations=("console", "reports.log", "db_handler"),  # "reports.log", "db_handler"
                level=10 if self.DEBUG_MODE else 20
            )
        return self._report

    @property
    def LOG_DB(self):
        if self._log_db is None:
            from utils_db import create_connection_string
            self._log_db = {
                'CONNECTION_STRING':
                    create_connection_string(type_='sqlite',
                                             name=f"{STG.APP_NAME}_{STG.CONTAINER_NAME}_log"),
                "ENCODING": 'utf-8',
                "POOL_SIZE": 10,
                "MAX_OVERFLOW": 20,
                "POOL_RECYCLE": 3600
            }
        return self._log_db


STG = Setting()
report = STG.report

if __name__ == "__main__":
    print(STG.DEBUG_MODE)
    print(STG.report)
