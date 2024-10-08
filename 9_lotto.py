import streamlit as st
import random

st.title("✨로또 생성기✨")

if st.button("로또를 생성해주세요!"):
    lotto_numbers = []
    
    for i in range(5):
        numbers = sorted(random.sample(range(1, 46), 6))
        lotto_numbers.append(numbers)

    for i, numbers in enumerate(lotto_numbers, start=1):
        st.subheader(f"{i}. 행운의 번호: :green[{numbers}]")