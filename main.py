# from dotenv import load_dotenv
# import os

# # 환경 변수 로드
# load_dotenv()

# OpenAI API 키가 제대로 설정되어 있는지 확인
# if not os.getenv("OPENAI_API_KEY"):
#     raise ValueError("OPENAI_API_KEY가 설정되지 않았습니다.")

# from langchain_openai import OpenAI

# # 온도(temperature) 설정을 추가하여 응답의 일관성 확보
# llm = OpenAI(temperature=0.3)

# # 더 구체적인 프롬프트 작성
# prompt = "안녕하세요"
# result = llm.invoke(prompt)
# print(result)

# 새로운 방식으로 import
# from langchain_openai import ChatOpenAI

# #chat_model = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
# chat_model = ChatOpenAI()
# result = chat_model.invoke("안녕하세요")
# print(result.content)  # .content를 추가하여 실제 메시지 내용만 출력

# from langchain_core.prompts import ChatPromptTemplate

# prompt = ChatPromptTemplate.from_template("안녕하세요")
# result = prompt.invoke("안녕하세요")
# print(result)

import streamlit as st

st.title("소설 쓰기")
title = st.text_input("장르를 입력하세요")
st.write(f"{title} 소설 쓰기")

if st.button("작성"):
    with st.spinner("작성 중...."):
        st.success("완료되었습니다.")
