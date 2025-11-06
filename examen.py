import streamlit as st

st.title("Formulario de Evaluación")
respuesta = st.text_input("¿Cuánto es 2 + 2?")

if st.button("Enviar"):
    if respuesta.strip() == "4":
        st.success("✅ Correcto — Calificación: 100")
    else:
        st.error("❌ Incorrecto — Calificación: 0")
