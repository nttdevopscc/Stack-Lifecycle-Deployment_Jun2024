import datetime

from config.database import Base
from sqlalchemy import (JSON, Column, DateTime, Integer, String, Text)


class Stack(Base):
    __tablename__ = "stacks"
    id = Column(Integer, primary_key=True, index=True)
    stack_name = Column(String(50), unique=True)
    git_repo = Column(String(200))
    branch = Column(String(50))
    task_id = Column(String(200))
    var_json = Column(JSON)
    var_list = Column(JSON)
    squad_access = Column(JSON)
    tf_version = Column(String(30))
    created_at = Column(DateTime, default=datetime.datetime.now())
    description = Column(Text())
    user_id = Column(Integer)
    # owner = relationship("User", back_populates="stacks")