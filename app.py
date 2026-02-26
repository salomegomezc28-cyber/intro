import streamlit as st

st.title("mi primera app")

st.header("aqui empiezo a desarrollar la app")
st.write("backend y frotend")
image = Image.open('imagen.jpg')
st.image(image, caption='interfaces')

texto = st.text_input('escribe algo','este es el texto')
st.write('El texto escrito es', texto)
