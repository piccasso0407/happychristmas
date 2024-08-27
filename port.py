import streamlit as st

st.title('How to Build a RAG System')

# 사이드바에 임의의 스타일 적용
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background-color: #FFFFFF;
    }
    </style>
    """,
    unsafe_allow_html=True
)
import streamlit as st

col1, col2= st.columns(2)

with col1:
st.image("C:/Users/CAWCAW/강의자료/KGBD_WEEK08/WEEK08_02_PDF추출/새 폴더/메타라마.jpg", caption="여러가지 LLM 모델", use_column_width=True)

with col2:
 
    st.image("챗지피티.jpg", use_column_width=True)



import streamlit as st

# 사이드바에 메인 페이지의 헤더를 표시하기 위한 함수
def display_header_in_sidebar(header):
    st.sidebar.markdown(f"### {header}")

# 현재 페이지의 헤더를 설정
st.title("|프로젝트 개요")

current_header = " 프로젝트 개요"
# 메인 페이지에 헤더 표시

# 사이드바에 현재 페이지의 헤더 표시
display_header_in_sidebar(current_header)

# 메인 페이지 내용

st.write('''RAG(Retrieval-Augmented Generation)는 LLM이 응답을 생성하기 전에 신뢰할 수 있는 외부 지식 베이스를 참조하도록 하여, 
         최신 정보 및 사용자가 원하는 도메인 정보를 반영하여 답변합니다. 아울러 참조할 수 있는 문서를 명확하게 지정해 주어
         답변의 부정확성이나 환각(hallucination)을 줄일 수 있습니다.
''')


st.write("""우리 프로그램을 효과적으로 사용하기 위해서 챗봇의 필요성을 느끼고 있었는데 
         rag 시스템을 이용하면 좋은 결과가 나올 것 같다는 생각에 이 프로젝트를 시작했습니다.""")


st.markdown("* * *")

# 이미지 표시
st.subheader("|만드는 방법")
current_subheader = "만드는 방법"
display_header_in_sidebar(current_subheader)

image_path = "랭체인시스템.jpg"

st.image(image_path, caption="RAG system 흐름도.", use_column_width=True)

st.markdown("* * *")
