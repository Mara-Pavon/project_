import streamlit as st
from backend import PreventivoAssistant

# Configuración de página
st.set_page_config(
    page_title="Catering Assistant",
    page_icon="🍽️",
    layout="centered"
)

# Contenedor para el título
with st.container():
    st.title("Catering Assistant🍽️ ")
    st.markdown("**Strumento AI per generare preventivi di catering in pochi istanti.**")
    st.caption("Puoi dirmi che tipo di evento stai organizzando: matrimonio, compleanno, battesimo, laurea o qualsiasi altra occasione.")

st.write("---")

# Inicialización del estado de la sesión
if "bot" not in st.session_state:
    st.session_state.bot = PreventivoAssistant()

if "messages" not in st.session_state:
    st.session_state.messages = [
        ("assistant", "Ciao! Sono qui per aiutarti a costruire un preventivo preciso e adatto al tuo evento. Dimmi cosa stai pianificando e procediamo insieme.")
    ]

# Mostrar mensajes existentes - SIN contenedores adicionales
for msg in st.session_state.messages:
    role, text = msg
    st.chat_message(role).write(text)

# Usar st.chat_input 
user_input = st.chat_input("Scrivi la tua richiesta qui...")

if user_input:
    # Agregar mensaje del usuario
    st.session_state.messages.append(("user", user_input))
    
    # Obtener respuesta del asistente
    with st.spinner("Sto elaborando la tua richiesta..."):
        response = st.session_state.bot.ask(user_input)
    
    # Agregar respuesta del asistente
    st.session_state.messages.append(("assistant", response))
    
    # Forzar recarga para mostrar los nuevos mensajes
    st.rerun()