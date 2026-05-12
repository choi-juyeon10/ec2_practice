import streamlit as st
from datetime import datetime

st.title("EC2 Streamlit 배포 실습")

st.write("### 202220409 정보융합학부 최주연")

st.write("AWS Learner Lab EC2에서 실행 중인 Streamlit 앱입니다.")

name = st.text_input("이름을 입력하세요")

if st.button("확인"):
    print(f"[LOG] {datetime.now()} - 확인 버튼 클릭, 입력값: {name}", flush=True)
    st.success(f"{name}님, Streamlit 앱이 정상적으로 실행되었습니다!")