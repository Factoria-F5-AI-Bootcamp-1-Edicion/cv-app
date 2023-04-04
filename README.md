<p align = "center">
<img src="https://user-images.githubusercontent.com/109460138/229746780-a2aa950b-0870-4ee3-8b56-8e895cd43df6.png" height=”300”       width=1000” style= "text-align: center"> 
</p>

## :notebook: Proyecto 
Por encargo de la empresa Simplon, empresa matriz de la Escuela Factoría F5, creamos un analizador de currículums de los alumnos para compararlos con ofertas de trabajo que se publican en sitios webs como Infojobs y, de esta manera, sacar su afinidad o match en forma de porcentaje. 

## :tickets: Azure
Se utiliza el Cognitive Service de Azure para activar el Form Recognicer y poder extraer el texto de las imágenes por medio de la técnica OCR (Optical Character Recognition). También se utiliza el servicio de Contenedores con Docker. 

## :factory: Funcionalidades
- `Funcionalidad 1`: Extracción de textos de los CVs.
- `Funcionalidad 2`: Comparación de los CVs con ofertas de trabajo dadas por el cliente. 
#### Añadido de extras al proyecto requerido inicialmente
- `Funcionalidad 3`: Scraping de ofertas de trabajo de sitios web como p.e. Infojobs. 
- `Funcionalidad 4`: Activación del recurso Cognitive Service y Form Recognizer de Azure con OCR para extraer los textos de los pdfs.  
- `Funcionalidad 5`: Generación de un contenedor con Docker en Azure para posterior despliegue y acceso por parte del cliente.  

## :key: Variables de Entorno requeridas
Las siguientes variables son necesarias para acceder a la conexión con los servicios de Azure

| Variable de entorno               |  Ejemplo                                                  |
|-----------------------------------|-----------------------------------------------------------|
| `AZURE_FORM_RECOGNIZER_ENDPOINT`  | `https://cv-recog-imagenes.cognitiveservices.azure.com`   | 
| `AZURE_FORM_RECOGNIZER_KEY`       | `b635ctertyh2c41d0bb1f8f612409fsdiifss7797`               | 

## :rocket: Resultado
Esta es la solución del trabajo realizado, donde se pueden apreciar diversos campos como el puesto, la compañía y el match o afinadad. 
<p align = "center">
<img src="https://user-images.githubusercontent.com/109460138/229618274-61312145-1a4f-40ab-b4a6-a00ff321dbc1.png" height=”300”       width=1000” style= "text-align: center"> 
</p>

## :open_file_folder: Estructura de este repositorio

| Carpeta | Fichero            | Descripción                                            |
|---------|--------------------|--------------------------------------------------------|
| `main`  | `Proyecto`         | Se pasa todo la rama dev al main                      |
|         | `ReadMe`           | Documentación y Resumen del proyecto                   |
| `dev`   | `flask-app`        | Ficheros necesarios para el despliegue con Flask api   |
|         | `Scraping`         | Método de scraping o raspado de las ofertas            |
|         | `Similitud_CV`     | Análisis de los CVs y similitud con ofertas            |


## :construction: Futuras modificaciones o implementaciones
En un futuro se pretende utilizar otros servicios que nos proporciona Azure, como son el analizador de textos y sus bases de datos o almacenamiento para mejorar y complementar lo desarrollado hasta el momento. 

## :computer: Tecnologías aplicadas
- FlaskAPI
- Microsoft Azure
- Trello
- Canvas
- GitHub
- Docker
- Python (Selenium, Beautifulsoup)
- Jupyter
- Visual Studio Code
- SpaCy
- NLTK
- Boostrap (HTML5, CSS3)


Para mayor información sobre las versiones de cada librería utilizada en el desarrollo del presente proyecto, se puede consultar el fichero `requirements.txt`
