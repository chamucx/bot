from flask import Flask, render_template, request
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

app = Flask(__name__)

# Parámetros de Azure AI (para DEMO, hardcoded)
###-------------------------------------------####
### PASO 1 -> en azure ai foundry seleccionar el modelo, Abrir en el area de juegos y click en ver codigo
###
### PASO 2 -> seleccionar autenticacion de clave y SDK de inferencia Azure AI (si el modelo lo posee)
###
### PASO 3  -> seleccionar endpoint  o Punto de conexión y copiar el valor, 
### ejemplo: "https://myproductodeazureabc.services.ai.azure.com/models"
###
### PASO 4  -> seleccionar model_name y copiar el valor, ejemplo: "gpt-4o"
###
### PASO 5 -> seleccionar el key o Clave de API y copiarlo ejemplo "ab123c45d67f89"
###
### PASO 6 -> ejecutar la aplicacion
###
###-------------------------------------------####


AZURE_ENDPOINT =""
AZURE_KEY = ""
DEPLOYMENT_NAME = ""

client = ChatCompletionsClient(
    endpoint=AZURE_ENDPOINT,
    credential=AzureKeyCredential(AZURE_KEY)
)

@app.route("/", methods=["GET", "POST"])
def index():
    response_text = None

    if request.method == "POST":
        user_prompt = request.form.get("prompt")

        try:
            response = client.complete(
                messages=[
                    SystemMessage(content="Eres un asistente útil. Siempre responde en español, sin importar el idioma de la pregunta."),
                    UserMessage(content=user_prompt)
                ],
                model=DEPLOYMENT_NAME,
                max_tokens=1000
            )
            response_text = response.choices[0].message.content

        except Exception as e:
            response_text = f"⚠️ Error: {str(e)}"

    return render_template("index.html", response=response_text)

if __name__ == "__main__":
    app.run(debug=True)
