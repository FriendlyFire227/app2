import streamlit as st

st.title("Калькулятор")
a = st.number_input("Введите первое число")
b = st.number_input("Введите второе число")
operation = st.text_input("Выберите операцию")
if st.button("Итого"):
    if operation == "+":
        st.info(a+b)
    elif operation == "-":
        st.info(a-b)
    elif operation == "*":
        st.info(a*b)
    elif operation == "/":
        st.info(a/b)


    