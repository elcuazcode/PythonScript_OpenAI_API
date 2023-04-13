# Chatbot con OpenAI
Este es un script en Python que utiliza la API de OpenAI para implementar un chatbot.

## Requisitos previos
Para ejecutar el script, necesitarás los siguientes requisitos previos:
- Una cuenta en OpenAI
- Una API key válida de OpenAI
- Python 3.6 o superior
- El paquete openai de Python

Para instalar el paquete openai, puedes utilizar el administrador de paquetes pip. Simplemente ejecuta el siguiente comando en tu terminal:


`
pip3 install openai
`

## Uso
Para utilizar el chatbot, sigue estos pasos:

1. Clona o descarga el repositorio en tu máquina local
2. Obtén tu API key de OpenAI y configúrala en el archivo `config.py`
3. Abre tu terminal y navega hasta la ubicación del archivo `main.py`
4. Ejecuta el comando `python main.py`
5. Ingresa el tema de la conversación cuando se te solicite
6. Interactúa con el chatbot y disfruta de las respuestas generadas por el modelo de lenguaje GPT-3.5 Turbo de OpenAI

## Cómo funciona el script
El script `main.py` implementa un chatbot que utiliza la API de OpenAI para generar respuestas en función del contexto de la conversación. El modelo de lenguaje utilizado es GPT-3.5 Turbo.

El chatbot funciona mediante un bucle while que solicita al usuario el tema de la conversación y utiliza la API de OpenAI para generar una respuesta en función del contexto. La conversación se almacena en una lista de mensajes que se actualiza con cada interacción.

¡Gracias por utilizar este chatbot!
