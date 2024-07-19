# ContentEnrichment 

## Indice 📑
- [Descripción del Proyecto](#descripción-del-proyecto-)
- [Funcionalidades](#funcionalidades-)
- [Tecnologías y Librerias Utilizadas](#tecnologías-y-librerias-utilizadas-)
- [Instalación](#instalación-)
- [Flujo](#flujo-)
- [Desarrolladoras](#desarrolladoras-)

## Descripción del Proyecto 📖

El proyecto **Content Enricher** tiene como propósito crear una herramienta que simplifique la investigación en Wikipedia. Esta herramienta permitirá a los usuarios buscar artículos en Wikipedia, enriquecer el contenido obtenido mediante la integración de una ia, traducirlo a diferentes idiomas y generar un informe final en formato PDF. De este modo, se facilitará el acceso a información relevante y se promoverá el aprendizaje multilingüe.

## Funcionalidades 📋

* Búsqueda en Wikipedia: Realiza una búsqueda según el tema proporcionado y extrae el título y los primeros cinco párrafos del artículo.


* Interacción del Usuario: Permite al usuario ingresar el tema y el idioma para la traducción, mostrando los resultados en la terminal.


* Enriquecimiento de Contenido: Envía el contenido a la API de textcortex para mejorar el texto y muestra el resultado en la terminal.


* Traducción de Contenido: Traduce el contenido usando la DeepTranslate al idioma elegido por el usuario y muestra la traducción en la terminal.


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

5. Realiza la otras intalaciones
```bash
#Generará en la raíz del proyecto un fichero llamado requirements.txt
pip freeze > requirements.txt
#Instalación de los requerimientos
pip install -r requirements.txt
```

6. Crea tu rama y comienza a trabajar!

```bash
#Crea la rama
git checkout -b feature/nombreDeTuRama
```

## Flujo ➡
#### 1. Inicio de la Aplicación

* El backend se inicializa y espera por solicitudes de los clientes (usuarios).
#### 2. Recepción de Datos de Entrada

* Se recibe una solicitud del cliente que incluye el tema de interés y el idioma de destino para la traducción.
#### 3. Búsqueda y Extracción de Datos desde Wikipedia

* Se utiliza la biblioteca Requests para enviar una solicitud a Wikipedia y obtener el contenido relevante del artículo basado en el tema proporcionado.
Se utiliza BeautifulSoup para extraer el título del artículo y los primeros cinco párrafos de contenido del HTML obtenido.


* Interacción con AI para Enriquecimiento de Contenido


* El contenido extraído se envía a la API de textcortex .


* Se procesa la respuesta de la API para obtener el contenido enriquecido.
#### 4. Traducción del Contenido

* Se utiliza la DeepTranslate para traducir el contenido enriquecido al idioma seleccionado por el usuario.
Se recibe la traducción y se prepara para su entrega al cliente.
#### 5. Generación de Archivos

* Se prepara el contenido original, enriquecido y/o traducido para ser guardado en archivos .txt o .pdf según la elección del usuario.


* Se utiliza ReportLab para generar archivos PDF si es necesario.


* Envío de Respuesta al Cliente


* Se envía la respuesta final al cliente, que puede incluir el contenido enriquecido, la traducción y/o la confirmación de la generación de archivos.
#### 6.Finalización del Proceso

* El backend concluye el procesamiento de la solicitud y queda a la espera de nuevas solicitudes.

## Desarrolladoras 🖥️
[**Helena López**](https://github.com/helopgom)


[**Carla Sanchez**](https://github.com/Carlassanchez24)


[**Angelina Bassano**](https://github.com/Angelinabassano)


[**Gabriela Rosas**](https://github.com/GabyRosas)


[**Angelica Perez**](https://github.com/Angelica2013)