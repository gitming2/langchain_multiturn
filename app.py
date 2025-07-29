from langchain_upstage import ChatUpstage
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import streamlit as st

# 환경변수에 키 불러오기
load_dotenv()
api_key = os.getenv("UPSTAGE_API_KEY")

chat = ChatUpstage(api_key=os.getenv("UPSTAGE_API_KEY"))

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Answer all questions to the best of your ability. You must anwer with Korean.",
        ),
        MessagesPlaceholder("messages"), # 이전에 나눴던 대화 불러오기
    ]
)

# prompt와 chat(언어 모델)을 연결하여 하나의 처리 흐름(chain)을 만드는 pipe(|)
chain = prompt | chat # 랭체인에서 사용되는 문법

# 연속적인 대화를 위해 이전 대화를 list에 저장하기 위한 초기화
chat_history = []

while True:
    user_input = input("질문(종료하려면 '끝' 입력): ")
    if user_input == '끝':
        break
    
    # 현재 질문을 chat_history에 저장
    chat_history.append(("user", user_input))

    ai_msg = chain.invoke(
        {
            "messages": chat_history
        }
    )
    print(ai_msg.content)
    
    # 현재 ai의 답변 chat_history에 저장
    chat_history.append(("ai", ai_msg.content))
