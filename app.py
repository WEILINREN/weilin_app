import streamlit as st

st.title("Hello, Streamlit!")
st.write("こんにちは、Streamlit!")

if st.checkbox("Show/Hide"):
    st.text("これは隠れているテキストです。")

st.markdown("### これはMarkdownです")

st.write("何か数字を入力してください：")
a = st.number_input("数字")
st.write("入力した数字は:", a)