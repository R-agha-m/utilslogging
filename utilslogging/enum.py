from enum import Enum


class EnumLogLevel(str, Enum):  # TODO: Make this case-insensitive
    CRITICAL = 'CRITICAL'
    FATAL = CRITICAL
    ERROR = 'ERROR'
    WARNING = 'WARNING'
    WARN = WARNING
    INFO = 'INFO'
    DEBUG = 'DEBUG'
    NOTSET = 'NOTSET'


class EnumLogHandler(str, Enum):
    file = "file"
    console = "console"
    syslog = "syslog"


class EnumLogRotatingWhen(str, Enum):
    S = "S"  # Seconds
    M = "M"  # Minutes
    H = "H"  # Hours
    D = "D"  # Days
    midnight = "MIDNIGHT"  # midnight
    W0 = "W0"  # roll over on a certain day; 0 - Monday
    W1 = "W1"  # roll over on a certain day; 0 - Monday
    W2 = "W2"  # roll over on a certain day; 0 - Monday
    W3 = "W3"  # roll over on a certain day; 0 - Monday
    W4 = "W4"  # roll over on a certain day; 0 - Monday
    W5 = "W5"  # roll over on a certain day; 0 - Monday
    W6 = "W6"  # roll over on a certain day; 0 - Monday


class EnumLogFacilityCode(str, Enum):
    LOG_KERN = "LOG_KERN"  # kernel messages
    LOG_USER = "LOG_USER"  # random user-level messages
    LOG_MAIL = "LOG_MAIL"  # mail system
    LOG_DAEMON = "LOG_DAEMON"  # system daemons
    LOG_AUTH = "LOG_AUTH"  # security/authorization messages
    LOG_SYSLOG = "LOG_SYSLOG"  # messages generated internally by syslogd
    LOG_LPR = "LOG_LPR"  # line printer subsystem
    LOG_NEWS = "LOG_NEWS"  # network news subsystem
    LOG_UUCP = "LOG_UUCP"  # UUCP subsystem
    LOG_CRON = "LOG_CRON"  # clock daemon
    LOG_AUTHPRIV = "LOG_AUTHPRIV"  # security/authorization messages (private)
    LOG_FTP = "LOG_FTP"  # FTP daemon
    LOG_NTP = "LOG_NTP"  # NTP subsystem
    LOG_SECURITY = "LOG_SECURITY"  # Log audit
    LOG_CONSOLE = "LOG_CONSOLE"  # Log alert
    LOG_SOLCRON = "LOG_SOLCRON"  # Scheduling daemon (Solaris)


class EnumLogSocketType(str, Enum):
    SOCK_STREAM: "SOCK_STREAM"
    SOCK_DGRAM: "SOCK_DGRAM"


class EnumLogStream(str, Enum):
    stderr: "stderr"
    stdout: "stdout"


class EnumOrderBy(str, Enum):
    ascending = "A"
    descending = "D"


class EnumRunMode(str, Enum):
    test = "test"
    production = "production"
    development = "development"


class EnumHashAlgorithm(str, Enum):
    HS256 = "HS256"
