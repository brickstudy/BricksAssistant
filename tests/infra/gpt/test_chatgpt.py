import pytest
from dotenv import load_dotenv

from src.adapter.gpt import GPTFactory


load_dotenv()


@pytest.fixture
def client():
    yield GPTFactory.create_client(gpt_type="chatgpt")


@pytest.mark.order(1)
def test_gpt_get_new_answer(client):
    # given : 사용자 첫 질문
    content = "Hello GPT, My name is Minjun."

    # when : gpt 응답요청
    response = client.request_gpt(content)
    print(response)

    # then : 응답 확인
    assert response.choices[0].message


@pytest.mark.order(2)
def test_gpt_get_continue_nswer(client):
    # given : 사용자 첫 질문 후 응답을 이어 재 질문
    # when : gpt 응답 요청
    name = "민준"
    first_content = f"안녕 BrickAssitant. 나는 {name}이야"
    second_content = "내 이름이 머야?"
    response = client.request_gpt(second_content, [first_content])

    # then : 응답 확인
    print(response)
    assert name in response.choices[0].message.content
