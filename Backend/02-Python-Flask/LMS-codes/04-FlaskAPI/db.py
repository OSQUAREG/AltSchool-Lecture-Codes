from sqlalchemy import create_engine, Integer, String, DateTime, Boolean, Column
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

engine = create_engine("sqlite:///tasks.db", connect_args={"check_same_thread": False})

session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()

"""
    class Task:
        id int
        content str
        date_added datetime
        is_completed Boolean
"""

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer(), primary_key=True)
    content = Column(String(500), nullable=False)
    date_added = Column(DateTime(), default=datetime.utcnow)
    is_completed = Column(Boolean(), default=False)

    def __repr__(self):
        return f"<Task {self.id}>"
    
Base.metadata.create_all(bind=engine)