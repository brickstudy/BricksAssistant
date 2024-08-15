import pytest

from src.adapter.database import DatabaseFactory


@pytest.fixture
def session():
    db = DatabaseFactory.create_database_brickas("mysql")
    yield db


def test_can_get_shortcut_data(session):
    # given : 유효한 mysql 정보
    # when : shortcut 요청
    result = session.get_items()

    # then : 응답
    # for r in result:
    #     print(r.id)
    #     print(r.name)
    #     break
    assert len(result) > 1
