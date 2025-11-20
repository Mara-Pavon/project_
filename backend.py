import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from prompt import SYSTEM_PROMPT

load_dotenv()

class PreventivoAssistant:
    def __init__(self):
        api_key = os.getenv("key")

        if not api_key:
            raise ValueError("archivo .env")

        # Inicializamos el modelo correctamente
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash-lite",
            google_api_key=api_key,
            temperature=0.7
        )

        # Historial real compatible con LangChain Core
        self.history = [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content="Inizia la conversazione.")
        ]

    def ask(self, user_text):
        # Agregamos el mensaje del usuario
        self.history.append(HumanMessage(content=user_text))

        # LangChain ahora usa invoke, no llamada directa
        response = self.llm.invoke(self.history)

        # Guardamos respuesta en historial
        self.history.append(AIMessage(content=response.content))

        return response.content
