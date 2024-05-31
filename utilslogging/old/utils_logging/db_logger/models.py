from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from stg import STG


base = declarative_base()


class Log(base):
    __tablename__ = f"{STG.APP_NAME}_{STG.CONTAINER_NAME}_log"

    id = Column(Integer,
                primary_key=True,
                autoincrement=True)

    time = Column(DateTime,
                  nullable=False,
                  default=datetime.now)

    level_name = Column(String(10),
                        nullable=True)

    module = Column(String(200),
                    nullable=True)

    thread_name = Column(String(200),
                         nullable=True)

    file_name = Column(String(200),
                       nullable=True)

    func_name = Column(String(200),
                       nullable=True)

    line_no = Column(Integer,
                     nullable=True)

    process_name = Column(String(200),
                          nullable=True)

    message = Column(Text)
    # last_line = Column(Text)
