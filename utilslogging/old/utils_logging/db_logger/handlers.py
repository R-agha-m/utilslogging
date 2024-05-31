from logging import Handler
from traceback import print_exc
from utils_db import Crud


class DBHandler(Handler):
    backup_logger = None

    def __init__(self,
                 level=0,
                 crud_inputs=None,
                 log_table=None):

        super().__init__(level)

        self.log_table = log_table

        self.crud = Crud(**crud_inputs)
        self.crud.initiate()

    def emit(self, record):
        try:
            message = self.format(record)

            try:
                new_log = self.log_table(module=record.module,
                                         thread_name=record.threadName,
                                         file_name=record.filename,
                                         func_name=record.funcName,
                                         level_name=record.levelname,
                                         line_no=record.lineno,
                                         process_name=record.processName,
                                         message=message)

                self.crud.insert(instances=new_log)

            except Exception:
                print_exc()

        except Exception:
            print_exc()
