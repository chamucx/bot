# Demo Asistente Virtual Azure AI con Flask

## Descripción

Aplicación web sencilla construida con **Flask** que conecta a un modelo **Azure AI (ChatCompletionsClient)** para ofrecer respuestas en español a preguntas ingresadas por el usuario.

## Requisitos previos

* Cuenta de **Azure** con acceso a **Azure OpenAI Service**.
* Un **deployment** activo de un modelo (por ejemplo, `gpt-4o`, `gpt-4.1`, etc.).
* Clave de API y URL del Endpoint de Azure AI Inference.
* Python 3.9 o superior instalado.

## Instalación

1. Clona el repositorio o descarga los archivos:

```bash
git clone https://github.com/tu_usuario/demo-azure-ai-flask.git
cd demo-azure-ai-flask
```

2. Crea y activa un entorno virtual (opcional pero recomendado):

```bash
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Configuración

Edita las variables siguientes en `app.py`:

```python
AZURE_ENDPOINT = "https://<tu-endpoint>.openai.azure.com/openai/deployments/<tu-deployment>/chat/completions?api-version=2025-01-01-preview"
AZURE_KEY = "<tu-clave-api>"
DEPLOYMENT_NAME = "<nombre-de-tu-deployment>"
```

## Ejecución local

Corre la aplicación:

```bash
python app.py
```

Accede en tu navegador a:

```
http://127.0.0.1:5000/
```

## Despliegue en Render

1. Crea una nueva Web Service en [Render](https://render.com/).

2. Configura:

* **Build Command**: `pip install -r requirements.txt`
* **Start Command**: `gunicorn app:app`
* **Environment Variables**:

  * `AZURE_ENDPOINT`
  * `AZURE_KEY`
  * `DEPLOYMENT_NAME`

3. (Opcional) Crea un `render.yaml`:

```yaml
services:
  - type: web
    name: azure-ai-assistant
    env: python
    plan: free
    buildCommand: "pip install -r requirements.txt"
    startCommand: "gunicorn app:app"
    envVars:
      - key: AZURE_ENDPOINT
        value: "<tu-endpoint>"
      - key: AZURE_KEY
        value: "<tu-api-key>"
      - key: DEPLOYMENT_NAME
        value: "<tu-deployment-name>"
```

## Estructura del Proyecto

```
/demo-azure-ai-flask
|├── templates/
|   └── index.html
|├── app.py
|├── requirements.txt
└── README.md
```

## requirements.txt

```
Flask
azure-ai-inference
azure-core
gunicorn
```

## Licencia

Proyecto educativo y de demostración. Uso libre bajo licencia MIT.
