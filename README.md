# 🦜⛓️ 랭체인과 감정 분석을 활용한 AI 챗봇
Streamlit으로 만든 대화형 AI 챗봇입니다. 

LangChain 프레임워크와 Upstage의 Solar-mini 모델을 사용하여 이전 대화를 기억하는 멀티턴(multi-turn) 대화가 가능합니다. 또한, Hugging Face의 감정 분석 모델을 통해 AI 답변의 감정을 실시간으로 분석하여 보여줍니다.

<img width="1045" height="852" alt="Image" src="https://github.com/user-attachments/assets/caff892f-d997-4614-9203-a2c230ac5f98" />

<br />

## ✨ 주요 기능
**멀티턴 대화**: st.session_state를 활용해 이전 대화 내용을 기억하고 문맥에 맞는 답변을 생성합니다.

**실시간 스트리밍 응답**: st.write_stream을 사용하여 AI의 답변을 타자기를 치는 것처럼 실시간으로 보여줍니다.

**AI 답변 감정 분석**: Hugging Face의 transformers 라이브러리를 통해 AI 답변의 감정(긍정/부정)을 분석하고 그 결과를 UI에 표시합니다.

**안전하고 효율적인 설계**:

@st.cache_resource를 사용해 무거운 AI 모델은 최초 한 번만 로드하여 성능을 최적화했습니다.

st.secrets를 통해 API 키를 안전하게 관리하며, 로컬 테스트와 실제 배포를 모두 지원합니다.

try-except 구문으로 안정적인 에러 처리를 구현했습니다.

<br />


## 🛠️ 기술 스택
**Frontend**: Streamlit

**LLM & Framework**: Upstage Solar-mini, LangChain

**Sentiment Analysis**: Hugging Face Transformers (monologg/koelectra-base-finetuned-nsmc)

**Deployment**: Streamlit Community Cloud

<br />

