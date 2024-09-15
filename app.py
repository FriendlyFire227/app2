import streamlit as st

st.title("Это сайт поп продаже дете, не бойтесь всё легально, наверное.")
tab1, tab2, tab3 = st.tabs(["Дорогой ребенок","Менее дорогой ребенок","Дешовый ребенок"])
with tab1:
    st.title("Дорогой")
    st.image("fedb30b299a3e2873af377e2cf46ad5a.jpg")
    if st.button("Купить1"):
        st.success("Успешно куплено, разрешено перепродать")
with tab2:
    st.title("Средний")
    st.image("0b8d922ba7be7c65717e084c7c544090.jpg")
    if st.button("Купить2"):
        st.success("Успешно куплено, разрешено перепродать")
with tab3:
    st.title("Дешовый")
    st.image("scale_1200.jpg")
    if st.button("Купить3"):
        st.success("Успешно куплено, разрешено перепродать")
