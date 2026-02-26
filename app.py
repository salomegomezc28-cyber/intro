import streamlit as st
from PIL import Image

st.title("mi primera app")

st.header("aqui empiezo a desarrollar la app")
st.write("backend y frotend")
image = Image.open('imagen.jpg')
st.image(image, caption='interfaces')

texto = st.text_input('escribe algo','este es el texto')
st.write('El texto escrito es', texto)



st.subheader("ahora son 2 columnas")

col1, col2 = st.colum(2)
with col1:
  st.subheader("Esta es la primera columna")
  st.write("mas texto")
  resp = st.checkbox("todavia mas texto")
  if resp:
    st.write('correcto')

with col2:
  st.subheader("esta es la segunda columna")
  modo = st.radio("modalidad de tu interfaz")
  if modo == 'visual':
    st.write('factor visual en tu interfaz')
  if modo == 'auditivo':
    st.write('factor auditivo en tu interfaz')
  if modo == 'tactil':
    st.write('factor tactil en tu interfaz')
  
      
