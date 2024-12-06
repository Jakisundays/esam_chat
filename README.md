

---

# 🏥 Asistente de Cuidado de Ancianos

Este proyecto es una aplicación basada en **Streamlit** que actúa como un asistente especializado en el cuidado de adultos mayores. Utiliza la API de **Together** para integrar un modelo de IA avanzado que responde preguntas relacionadas con salud, nutrición, y bienestar para personas mayores. La aplicación está diseñada para ser amable, precisa y práctica, ofreciendo apoyo tanto a los cuidadores como a los interesados en mejorar la calidad de vida de los ancianos.

---

## 🚀 Funcionalidades

- **Interacción amigable:** La interfaz permite a los usuarios interactuar con el asistente escribiendo preguntas relacionadas con el cuidado de personas mayores.
- **Asistencia experta:** El modelo responde consultas sobre:
  - Dietas adecuadas para adultos mayores.
  - Manejo de condiciones de salud comunes.
  - Bienestar emocional.
  - Rutinas de ejercicio seguras.
- **Respuestas en tiempo real:** El asistente genera respuestas en streaming para ofrecer una experiencia interactiva y dinámica.
- **Historial de mensajes:** Conserva el historial de conversación durante la sesión.

---

## 🛠️ Requisitos Previos

Antes de ejecutar esta aplicación, asegúrate de tener:

1. **Python 3.8 o superior.**
2. Las siguientes bibliotecas instaladas:
   - `streamlit`
   - `together`
3. Una clave API válida para la plataforma **Together**, configurada como variable de entorno:
   ```bash
   export TOGETHER_APIKEY=tu_clave_api
   ```

---

## 📦 Instalación

Sigue estos pasos para configurar el proyecto:

1. **Clona este repositorio**:

   ```bash
   git clone https://github.com/tuusuario/asistente-cuidado-ancianos.git
   cd asistente-cuidado-ancianos
   ```

2. **Instala las dependencias**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configura tu clave API**:
   Asegúrate de haber configurado la variable de entorno `TOGETHER_APIKEY` con tu clave API de Together.

---

## ▶️ Uso

1. **Ejecuta la aplicación**:

   ```bash
   streamlit run app.py
   ```

2. Abre el navegador en la URL proporcionada, usualmente [http://localhost:8501](http://localhost:8501).

3. Escribe tus preguntas en el cuadro de entrada y obtén respuestas especializadas relacionadas con el cuidado de adultos mayores.

---

## 📂 Estructura del Código

- **`get_ai_stream(messages)`**  
  Llama a la API de Together para generar respuestas del modelo de IA en streaming.

- **`stream_view(stream)`**  
  Procesa los datos del stream para enviar las respuestas en tiempo real a la interfaz.

- **`main()`**  
  Configura la interfaz de usuario de Streamlit, gestiona el historial de mensajes y maneja la interacción del usuario con el asistente.

---

## 🌟 Contribuciones

Las contribuciones son bienvenidas. Si tienes sugerencias o encuentras problemas, no dudes en abrir un **issue** o enviar un **pull request**.

---

## ⚠️ Notas

- La aplicación está diseñada exclusivamente para responder preguntas sobre el cuidado de ancianos. Si un tema está fuera de su alcance, el modelo responderá amablemente indicando que no puede ayudar con esa consulta.
- Esta aplicación no reemplaza la consulta médica profesional.

---

¡Gracias por usar el Asistente de Cuidado de Ancianos! 😊
# esam_chat
