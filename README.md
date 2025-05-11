# Asistente Virtual Azure AI con Flask

## Descripción

Aplicación web construida con **Flask** que conecta a un modelo **Azure AI (ChatCompletionsClient)** para ofrecer respuestas en español a preguntas ingresadas por el usuario. Este repositorio está diseñado para que puedas clonar el proyecto, configurarlo con tu Azure AI, probarlo localmente, personalizarlo, subirlo a tu propio GitHub y finalmente desplegarlo como Web App en Azure.

RECUERDA APOYAR EL CANAL Y AYUDARME A LLEGAR A LOS 10K SUSCRIPTORES ESTE AÑO.
O APOYAR CON UNA PEQUEÑA DONACION.

## Requisitos previos

* **Cuenta de Azure** con acceso a **Azure OpenAI Service**.
* Un **deployment** activo de un modelo (por ejemplo, `gpt-4o`, `gpt-4.1`, etc.).
* **Clave de API** y **URL del Endpoint** de Azure AI Inference.
* **Python 3.9 o superior** instalado en tu equipo.
* Tener instalado **Visual Studio Code (VS Code)**.
* Tener instalada la **extensión de Python** en Visual Studio Code.
* Tener instalada la **extensión de Azure App Service** en Visual Studio Code.

## Flujo de trabajo sugerido

1. Clonar este repositorio.
2. Configurar las variables de Azure en `app.py`.
3. Actualizar URL de formularios en `templates/index.html` si es necesario.
4. Probar localmente.
5. Crear tu propio repositorio en GitHub.
6. Subir los cambios a GitHub.
7. Publicar la app en Azure como Web App.

## Instalación local

1. Clona el repositorio:

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
```

2. Crea y activa un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate    -> Si usas Linux/Mac
venv\Scripts\activate       -> si Usas Windows
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Configuración de Azure

Edita las siguientes variables en `app.py` (opcional, si no quieres usar variables de ambiente):

```python
import os

AZURE_ENDPOINT = "AZURE_ENDPOINT"
AZURE_KEY = "AZURE_KEY"
DEPLOYMENT_NAME = "DEPLOYMENT_NAME"
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

2. Inicializa el repositorio localmente:

```bash
git init
git add .
git commit -m "Primer commit"
git branch -M main
git remote add origin https://github.com/tu_usuario/tu_repositorio.git
git push -u origin main
```

## Despliegue como Azure Web App desde Visual Studio Code

1. Abre el proyecto en **Visual Studio Code**.
2. Asegúrate de tener instaladas las extensiones de **Python** y **Azure App Service**.
3. Inicia sesión en tu cuenta de Azure desde VS Code.
4. Haz clic en "+" para crear una nueva Web App en Azure.

   * Selecciona **Runtime Stack**: `Python 3.9` o superior.
   * Selecciona tu plan de hosting o crea uno nuevo.
5. Publica la aplicación en Azure:

   * Clic derecho en tu carpeta del proyecto -> **Deploy to Web App**.
6. Configura las variables de ambiente en Azure:

   * Entra al **Portal de Azure**.
   * Busca tu **Web App**.
   * Navega a **Configuración > Configuración de Aplicación**.
   * Agrega:

     * `AZURE_ENDPOINT` con tu endpoint.
     * `AZURE_KEY` con tu clave de API.
     * `DEPLOYMENT_NAME` con el nombre de tu modelo desplegado.

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