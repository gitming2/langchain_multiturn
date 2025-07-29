from langchain_upstage import ChatUpstage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import streamlit as st
from transformers import pipeline

st.set_page_config(
         page_title="중간평가 챗봇",
         page_icon="🤖",
     )
st.title("랭체인 멀티턴 챗봇")

#-------------- 초기 세팅
if "chain" not in st.session_state:
    api_key = st.secrets["UPSTAGE_API_KEY"]
    
    if "UPSTAGE_API_KEY" not in st.secrets:
        st.error("UPSTAGE_API_KEY 환경변수를 설정해주세요.")
        st.stop()
        
    chat = ChatUpstage(api_key=api_key, model="solar-mini")

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
    st.session_state.chain = prompt | chat # 랭체인에서 사용되는 문법
    # 메세지 없으면 메세지 초기화(chain이 없으면 message도 없으니)
    st.session_state.messages = []
#-----------------    

# 기존 메세지 표시 # 질문할 때마다 이전 메세지 사라지고 새로운 답 뜨는 거 방지
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])
        

# 파이프라인 캐시화(최초 한 번만 로드) -> 감정분석 모델을 계속 로드하는 걸 방지
# 허깅페이스 감정분석 파이프라인
@st.cache_resource
def sentimental_pipeline():
    return pipeline("sentiment-analysis",model="monologg/koelectra-base-finetuned-nsmc")

if user_prompt := st.chat_input("질문을 입력하세요."):
    st.session_state.messages.append({"role": "user","content": user_prompt})
    
    with st.chat_message("user"):
        st.markdown(user_prompt)
          
    with st.chat_message("assistant"):
        try:
            result = st.session_state.chain.stream({
                "messages": st.session_state.messages
            })
    
            # st.write_stream 주어진 시퀀스를 반복하며 모든 청크를 앱에 씀
            # -> 문자열 청크는 타자기 효과를 사용하여 작성됨
            full_response = st.write_stream(result)
            
            try:
            # 감정 분석
                sentiment_analysis = sentimental_pipeline() # 캐시된 파이프라인 가져옴
                senti_result = sentiment_analysis(full_response)
                # 분석한 감정 사용자에게 보여줌
                st.info(f"위 답변의 감정은: {senti_result[0]['label']}")
            except Exception as e:
                st.error(f"감정 분석 중 에러: {e}")
            
            st.session_state.messages.append({"role": "assistant","content": full_response})
            
        except Exception as e:
            st.error(f"답변 생성 중 에러: {e}")