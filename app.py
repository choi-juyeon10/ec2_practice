import streamlit as st

st.title("EC2 Streamlit 배포 실습")

st.write("### 202220409 정보융합학부 최주연")

st.write("AWS Learner Lab EC2에서 실행 중인 Streamlit 앱입니다.")

name = st.text_input("이름을 입력하세요")

if st.button("확인"):
    st.success(f"{name}님, Streamlit 앱이 정상적으로 실행되었습니다!")