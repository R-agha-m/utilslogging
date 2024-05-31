from logging import Formatter


class CustomFormatter(Formatter):
    """Custom formatter, overrides funcName with value of name_override if it exists"""
    def format(self, record):
        if hasattr(record, 'func_name_override'):
            record.funcName = record.func_name_override
        return super(CustomFormatter, self).format(record)
