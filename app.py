import streamlit as st
from backend import PreventivoAssistant

st.set_page_config(page_title="Catering Assistant", page_icon="🍽️")

st.title("Catering Assistant")
st.write("Assistente AI per creare preventivi in modo automatico.")
st.write("Dimmi che tipo di evento vuoi organizzare 🎉: matrimonio, compleanno, battesimo, laurea…")

if "bot" not in st.session_state:
    st.session_state.bot = PreventivoAssistant()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar historial.

for msg in st.session_state.messages:
    role, text = msg
    if role == "user":
        st.chat_message("user").write(text)
    else:
        st.chat_message("assistant").write(text)

# Input del usuario
user_input = st.chat_input("Scrivi la tua richiesta...")

if user_input:
    # Mostrar mensaje utente
    st.session_state.messages.append(("user", user_input))
    st.chat_message("user").write(user_input)

    # Obtener respuesta del bot
    response = st.session_state.bot.ask(user_input)

    # Mostrar respuesta asistente
    st.session_state.messages.append(("assistant", response))
    st.chat_message("assistant").write(response)
