# ContentEnrichment 

## Indice 📑
- [Descripción del Proyecto](#descripción-del-proyecto-)
- [Funcionalidades](#funcionalidades-)
- [Tecnologías y Librerias Utilizadas](#tecnologías-y-librerias-utilizadas-)
- [Instalación](#instalación-)
- [Desarrolladoras](#desarrolladoras-)

## Descripción del Proyecto 📖

El proyecto **Content Enricher** tiene como propósito crear una herramienta que simplifique la investigación en Wikipedia. Esta herramienta permitirá a los usuarios buscar artículos en Wikipedia, enriquecer el contenido obtenido mediante la integración de una ia, traducirlo a diferentes idiomas y generar un informe final en formato PDF. De este modo, se facilitará el acceso a información relevante y se promoverá el aprendizaje multilingüe.

## Funcionalidades 📋

* Búsqueda en Wikipedia: Realiza una búsqueda según el tema proporcionado y extrae el título y los primeros cinco párrafos del artículo.


* Interacción del Usuario: Permite al usuario ingresar el tema y el idioma para la traducción, mostrando los resultados en la terminal.


* Enriquecimiento de Contenido: Envía el contenido original a la API de textcortex para mejorar el texto y muestra el resultado en la terminal.


* Traducción de Contenido: Traduce el contenido original con DeepTranslate al idioma elegido por el usuario y muestra la traducción en la terminal.


* Generación de Archivos: Ofrece la opción de guardar el contenido original, enriquecido y traducido en formato .txt o .pdf, permitiendo al usuario elegir el nombre del archivo.

## Tecnologías y Librerias Utilizadas 🛠️

* Python 3.8 +
* BeautifulSoup
* Requests
* Python dotenv
* ReportLab
* Pytest
* DeepTranslate

## Instalación ⚙️

Sigue los siguientes pasos para configurar el proyecto en tu entorno local y asi poder practicar. 

### Instrucciones

1. **Crea un fork del repositorio**

   Abre el repositorio [Content Enrichment](https://github.com/GabyRosas/ContentEnrichment) en GitHub y haz clic en el botón "Fork" en la esquina superior derecha de la página. Esto creará una copia del repositorio en tu propia cuenta de GitHub.


2. **Clona tu repositorio fork**

   Abre una terminal Git Bash y ejecuta el comando con el link de tu nuevo repositorio:

```bash
# Clonar 
git clone https://github.com/tu-usuario/ContentEnrichment.git
```

3. **Abre Pycharm y abre el archivo que acabas de clonar**


4. **Para iniciar hay que crear el entorno virtual por la terminal y luego activarlo**

```bash
# Crea el entorno virtual
python -m venv venv
# Activa el entorno virtual
venv\Scripts\activate
#Y si necesitas desactiva el entorno virtual
venv\Scripts\deactivate
```

5. **Realiza la otras intalaciones**
```bash
#Generará en la raíz del proyecto un fichero llamado requirements.txt
pip freeze > requirements.txt
#Instalación de los requerimientos
pip install -r requirements.txt
```

6. **Crea tu rama y comienza a trabajar!**

```bash
#Crea la rama
git checkout -b feature/nombreDeTuRama
```

## Desarrolladoras 🖥️
[**Helena López**](https://github.com/helopgom)


[**Carla Sanchez**](https://github.com/Carlassanchez24)


[**Angelina Bassano**](https://github.com/Angelinabassano)


[**Gabriela Rosas**](https://github.com/GabyRosas)


[**Angelica Perez**](https://github.com/Angelica2013)