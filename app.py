import os
import streamlit as st
from together import Together


def get_ai_stream(messages):
    try:
        client = Together(api_key=os.getenv("TOGETHER_APIKEY"))
        stream = client.chat.completions.create(
            model="meta-llama/Llama-3-8b-chat-hf",
            messages=[
                {
                    "role": "system",
                    "content": "Usted es un experto en el cuidado de ancianos, con un profundo énfasis en salud y nutrición. Su misión es proporcionar consejos especializados, información precisa y apoyo práctico a los cuidadores de ancianos. Se especializa en temas como la dieta adecuada para los mayores, el manejo de condiciones de salud comunes, el bienestar emocional de los ancianos, y la implementación de rutinas de ejercicio seguras y efectivas. Si recibe una pregunta fuera de estos temas, por favor indique amablemente que no puede ayudar con ese tema y ofrezca a orientar al usuario hacia recursos o temas relevantes en su área de experticia. Si el usuario pregunta algo que no está claro, sientase libre de pedir aclaraciones para proporcionar una respuesta más precisa y útil. Su enfoque debe ser amable, compasivo y paciente, reflejando una profunda preocupación por el bienestar de los ancianos y aquellos que los cuidan.",
                },
            ]
            + messages,
            stream=True,
        )
        return stream
    except Exception as e:
        return f"Ocurrió un error: {str(e)}"


def stream_view(stream):
    for chunk in stream:
        yield chunk.choices[0].delta.content


def main():
    # Configure the page
    st.set_page_config(page_title="Asistente de Cuidado de Ancianos", page_icon="👵")

    # Title
    st.title("🏥 Experto en Cuidado de Ancianos")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User input
    if prompt := st.chat_input(
        "¿Cómo puedo ayudarte con el cuidado de personas mayores?"
    ):
        # Append user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get assistant response stream
        api_messages = [
            {"role": msg["role"], "content": msg["content"]}
            for msg in st.session_state.messages
        ]

        ai_response_stream = get_ai_stream(api_messages)

        # Display assistant message with streaming
        with st.chat_message("assistant"):
            placeholder = st.empty()
            full_response = ""
            try:
                for chunk in stream_view(ai_response_stream):
                    full_response += chunk
                    placeholder.markdown(full_response)
            except Exception as e:
                placeholder.markdown(f"Error during streaming: {e}")

        # Append assistant message to chat history with the full response
        st.session_state.messages.append(
            {"role": "assistant", "content": full_response}
        )


if __name__ == "__main__":
    # Check for Together API key
    if not os.getenv("TOGETHER_APIKEY"):
        st.error("Por favor, configura la variable de entorno TOGETHER_APIKEY.")
    else:
        main()
