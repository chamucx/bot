# Asistente Virtual Azure AI con Flask

## Descripción

Aplicación web construida con **Flask** que conecta a un modelo **Azure AI (ChatCompletionsClient)** para ofrecer respuestas en español a preguntas ingresadas por el usuario. Este repositorio está diseñado para que puedas clonar el proyecto, configurarlo con tu Azure AI, probarlo localmente, personalizarlo, subirlo a tu propio GitHub y finalmente desplegarlo en Render.

## Requisitos previos

* Cuenta de **Azure** con acceso a **Azure OpenAI Service**.
* Un **deployment** activo de un modelo (por ejemplo, `gpt-4o`, `gpt-4.1`, etc.).
* Clave de API y URL del Endpoint de Azure AI Inference.
* Python 3.9 o superior instalado.

## Flujo de trabajo sugerido

1. Clonar este repositorio.
2. Configurar las variables de Azure en `app.py`.
3. Actualizar URL de formularios en `templates/index.html` si es necesario.
4. Probar localmente.
5. Crear tu propio repositorio en GitHub.
6. Subir los cambios a GitHub.
7. Desplegar en Render.

## Instalación local

1. Clona el repositorio:

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
```

2. Crea y activa un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Configuración de Azure

Edita las siguientes variables en `app.py`:

```python
AZURE_ENDPOINT = "https://<tu-endpoint>.openai.azure.com/openai/deployments/<tu-deployment>/chat/completions?api-version=2025-01-01-preview"
AZURE_KEY = "<tu-clave-api>"
DEPLOYMENT_NAME = "<nombre-de-tu-deployment>"
```

## Modificación del `index.html`

Si cambias la ruta de la aplicación o despliegas en otro dominio, asegúrate de actualizar el atributo `action` del formulario en `templates/index.html`:

```html
<form method="POST" action="/">
```

Si la app estará en un subdominio o ruta distinta, actualízala en consecuencia.

## Ejecución local

Corre la aplicación:

```bash
python app.py
```

Abre tu navegador en:

```
http://127.0.0.1:5000/
```

## Crear y subir tu propio repositorio GitHub

1. Crea un nuevo repositorio en [GitHub](https://github.com/new).

2. Inicializa el repositorio localmente (si no está inicializado):

```bash
git init
```

3. Agrega todos los archivos y haz tu primer commit:

```bash
git add .
git commit -m "Primer commit"
```

4. Crea la rama principal:

```bash
git branch -M main
```

5. Agrega el remoto de tu nuevo repositorio:

```bash
git remote add origin https://github.com/tu_usuario/tu_repositorio.git
```

6. Sube tus cambios a GitHub:

```bash
git push -u origin main
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

## Estructura del Proyecto

```
/tu_repositorio
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
