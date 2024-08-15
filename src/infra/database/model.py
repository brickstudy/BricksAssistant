from sqlalchemy import Integer, VARCHAR, Column
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Shortcut(Base):
    __tablename__ = 'shortcut'

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(100), nullable=True)
    url = Column(VARCHAR(500), nullable=True)
