import os
from openai import OpenAI
import pytest
from dotenv import load_dotenv


load_dotenv()


@pytest.fixture()
def client():
    yield OpenAI(
        api_key=os.getenv("OPENAI_TOKEN")
        )


@pytest.mark.order(1)
def test_gpt_get_new_answer(client):
    # given : 사용자 첫 질문
    content = "Hello GPT, My name is Minjun."

    # when : gpt 응답요청
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are ChatGPT, a large language model trained by OpenAI."},
            {"role": "user", "content": content}
        ]
    )

    # then : 응답 확인
    assert response.model.startswith("gpt-4o-mini")
    assert response.choices[0].message


@pytest.mark.order(2)
def test_gpt_get_continue_nswer(client):
    # given : 사용자 첫 질문 후 응답을 이어 재 질문
    # when : gpt 응답 요청
    name = "민준"
    first_content = f"안녕 BrickAssitant. 나는 {name}이야"
    second_content = "내 이름이 머야?"
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "너의 이름은 brickAssistant 이야. 답변은 한국어를 기본으로 해줘."},
            {"role": "assistant", "content": first_content},
            {"role": "user", "content": second_content}
        ]
    )

    # then : 응답 확인
    print(response)
    assert response.model.startswith("gpt-4o-mini")
    assert name in response.choices[0].message.content
