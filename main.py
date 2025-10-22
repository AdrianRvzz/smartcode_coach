import streamlit as st
import random
import time
import os
from dotenv import load_dotenv
from google import genai
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


if "genai_client" not in st.session_state:
    st.session_state.genai_client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

client = st.session_state.genai_client


def stream_data(TEXT):
    for word in TEXT.split(" "):
        yield word + " "
        time.sleep(0.02)

def response_generator():
    response = random.choice(
        [
            "¡Hola! Envíame tu código y te doy algunas recomendaciones.",
            "¿Tienes código? Mándamelo y te ayudo a mejorarlo.",
            "Pásame tu código para revisarlo y darte sugerencias.",
            "¿Quieres que te dé consejos sobre tu código? Envíamelo.",
            "Compárteme tu código y te diré cómo optimizarlo."
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


if "messages" not in st.session_state:
    st.session_state.messages = []

    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
    st.session_state.messages.append({"role": "assistant", "content": response})

else:
    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


if prompt := st.chat_input("Ingresa el código", ):

    # Display user message in chat message container
    with st.chat_message("user"):
        st.code(prompt, language="python")
    st.session_state.messages.append({"role": "user", "content": prompt})


    full_prompt = f"""
    Evalúa la siguiente función de Python según estas buenas prácticas:
    Mantenibilidad: máximo 3 parámetros (CleanCode Cap 3)
    Modularidad: máximo 20 líneas (CleanCode Cap 3)
    Consistencia: snake_case para funciones y variables (PEP8)
    Legibilidad: comentarios completos, mayúscula inicial, <72 caracteres, separación de 2 espacios (PEP8)
    Para cada incumplimiento, genera una recomendación concreta indicando qué cambiar, basado en qué y qué buena práctica mejora.
    
    Devuelve la respuesta en **Markdown**, usando:
    - Encabezados (###) para secciones
    - Bloques de código ```python``` para ejemplos
    - Listas con * para bullets

    
    Función a evaluar:


    {prompt}
    """
    response_obj = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=full_prompt,
    )


    text = response_obj.text
        
    with st.chat_message("assistant"):
        st.write_stream(stream_data(text))

        


    

    # Guardar en historial
    st.session_state.messages.append({"role": "assistant", "content": text})


