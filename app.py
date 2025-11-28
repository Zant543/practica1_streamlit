import streamlit as st

st.title("Hola mundo en Streamlit")
st.write("Esta es mi primera aplicacion web creada en python usando Streamlit.")

st.subheader("¿Que hace esta aplicacion?")
st.write(
    """
    - Muestra un titulo en la parte superior.
    - Muestra un texto de bienvenida
    - Corre como una aplicacion web en el navegador.
    """
)

st.success("¡Felicidades! Ya tienes tu primera app web en funcionamiento")
