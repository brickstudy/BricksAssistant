
<img src="https://github.com/user-attachments/assets/4a46114c-4c4d-4741-8bfc-fb89c278545d" alt="Image description" width="500" height="500">


# BricksAssistant

This project is a chatbot service that leverages generative AI to interact with users on Discord.

<br>

## Introduction

BricksAssistant is designed to enhance your Discord experience by providing intelligent and responsive interactions through a generative AI chatbot.

This project aims to integrate seamlessly with your Discord server, offering advanced conversational capabilities.

<br>

## Features
- Generative AI: Uses state-of-the-art AI to generate human-like responses.
- Customizable: Tailor the bot's responses and behavior to fit your community's needs.
- Real-time Interaction: Immediate responses to user queries and commands.
- Project-Specific Chatbots: Provides specialized chatbots tailored for different projects.

![image](https://github.com/user-attachments/assets/4e2cdee9-444e-47ba-aef7-9979c8c8708d)

<br>


## Installation

### 1/ Chatbot setting

- 아래 정리된 문서 참고

[[BricksAssistant] 디스코드 AI 챗봇 구축기 - (2) 디스코드 연동하기](https://brickstudy.tistory.com/8)

### 2/ Clone the repository && requirements.txt

```bash
git clone https://github.com/brickstudy/BricksAssistant.git

cd BricksAssistant

pip install -r requirements.txt
```


### 3/ config setting

- 경로 : ./src/.env

```sh
# DISCORD
DISCORD_TOKEN=

# OPENAI
OPENAI_TOKEN=

# AWS(Document DB)
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_DEFAULT_REGION=
```

### 4/ run bot

```sh
python app.py
```

<br>

## Contributing
We welcome contributions to BricksAssistant!

To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch with your feature or bugfix.
3. Make your changes and commit them with clear messages.
4. Push your changes to your fork.
5. Open a pull request to the main repository.
6. Please ensure your code adheres to the project's coding standards and includes relevant tests.


