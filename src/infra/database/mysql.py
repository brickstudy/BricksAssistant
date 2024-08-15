import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.infra.database.model import Shortcut
from src.infra.database.abs_database import AbstractDatabaseBrickas


class MySQL(AbstractDatabaseBrickas):
    def __init__(self) -> None:
        MYSQL_HOST = os.getenv("MYSQL_HOST")
        MYSQL_USER = os.getenv("MYSQL_USER")
        MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
        MYSQL_PORT = os.getenv("MYSQL_PORT")
        MYSQL_DB = os.getenv("MYSQL_DB")
        database_url = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}'
        engine = create_engine(database_url, echo=False)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def get_items(self):
        return self.session.query(Shortcut).all()
