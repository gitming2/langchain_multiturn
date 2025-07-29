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
        ("placeholder", "{messages}"),
    ]
)

chain = prompt | chat

ai_msg = chain.invoke(
    {
        "messages": [ # 여기가 `placeholder`에서 참조하는 {messages} 변수!
            (
                "human", "내 이름은 A야",
            ),
            ("ai", "안녕 A"),
            ("human", "내 이름이 뭐라고?"),
        ],
    }
)
print(ai_msg.content)