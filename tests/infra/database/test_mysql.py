import os
import pytest

from sqlalchemy import create_engine, Integer, VARCHAR, Column
from sqlalchemy.orm import sessionmaker, declarative_base


Base = declarative_base()


class Shortcut(Base):
    __tablename__ = 'shortcut'

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(100), nullable=True)
    url = Column(VARCHAR(500), nullable=True)


@pytest.fixture
def mysql():
    MYSQL_HOST = os.getenv("MYSQL_HOST")
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_PORT = os.getenv("MYSQL_PORT")
    MYSQL_DB = os.getenv("MYSQL_DB")
    database_url = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}'
    print(database_url)
    engine = create_engine(database_url, echo=False)
    Session = sessionmaker(bind=engine)

    yield Session()


def test_can_get_shortcut_data(mysql):
    # given : 유효한 mysql 정보
    # when : shortcut 요청
    result = mysql.query(Shortcut).all()

    # then : 응답
    assert len(result) > 1
