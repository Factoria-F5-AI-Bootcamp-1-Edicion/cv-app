<p align = "center">
<img src="https://user-images.githubusercontent.com/109460138/229746780-a2aa950b-0870-4ee3-8b56-8e895cd43df6.png" height=”300”       width=850” style= "text-align: center"> 
</p>

### :busts_in_silhouette: Componentes
<b>David García,</b> (product owner) :arrow_right: https://github.com/DooFromash  
<b>Javier Inglés,</b> (scrum master) :arrow_right: https://github.com/Javingles  
<b>Begoña Ortíz,</b> (developer) :arrow_right: https://github.com/bego2022  
<b>Christian Cabrera,</b> (developer) :arrow_right: https://github.com/ChrisCabrera24 


### :notebook: Proyecto 
Por encargo de Simplon, empresa matriz de la Escuela Factoría F5, creamos un analizador de currículums de los alumnos para compararlos con ofertas de trabajo y, de esta manera, sacar su afinidad o match en forma de porcentaje. 

### :factory: Funcionalidades
- <b>Funcionalidad 1:</b> Extracción de textos de los CVs.
- <b>Funcionalidad 2:</b> Comparación de los CVs con ofertas de trabajo dadas por el cliente. 
- `El cuaderno válido para esta 1ª parte sería "ob_matching_demo.ipynb", guardado dentro de la carpeta Flask-app. Instalándose el archivo requirements.txt y ejecutando el código daría el resultado de ese match con la limpieza del texto ya realizada.`
#### Añadido de extras al proyecto requerido inicialmente
- <b>Funcionalidad 3:</b> Scraping de ofertas de trabajo de sitios web como p.e. Infojobs. 
- `El scraping se resolvería corriendo el cuaderno "infojobs.ipynb" devolviendo un archivo .csv`
- <b>Funcionalidad 4:</b> Activación del recurso Cognitive Service y Form Recognizer de Azure con OCR para extraer los textos de los pdfs.  
- <b>Funcionalidad 5:</b> Generación de un contenedor con Docker en Azure para posterior despliegue y acceso por parte del cliente.  
- `En esta segunda parte del proyecto, se le suministraría al cliente una "url" para que directamente pudiese subir el CV y automáticamente le aparecía el resultado de la afinidad entre el CV y las oferta de trabajo`. 

### :tickets: Azure
Se utiliza el Cognitive Service de Azure para activar el Form Recognicer y poder extraer el texto de las imágenes por medio de la técnica OCR (Optical Character Recognition). También se utiliza el servicio de Contenedores con Docker para su despliegue. 

### :key: Variables de Entorno requeridas
Las siguientes variables son necesarias para acceder a la conexión con los servicios de Azure y poder ejecutar el proyecto.

| Variable de entorno               |  Ejemplo                                                  |
|-----------------------------------|-----------------------------------------------------------|
| `AZURE_FORM_RECOGNIZER_ENDPOINT`  | `https://cv-recog-imagenes.cognitiveservices.azure.com`   | 
| `AZURE_FORM_RECOGNIZER_KEY`       | `b635ctertyh2c41d0bb1f8f612409fsdiifss7797`               | 

### :rocket: Resultado
Esta es la solución del trabajo realizado, donde se pueden apreciar las cajas para incluir el currículum a comparar y petición de subida, diversos campos como el puesto, la compañía y el match o afinidad. 
<p align = "center">
<img src="https://user-images.githubusercontent.com/109460138/229910463-839394d7-06e3-44fb-b5f8-40c6f1fc347b.png" height=”300”       width=1000” style= "text-align: center"> 
</p>
<p align = "center">
<img src="https://user-images.githubusercontent.com/109460138/229908683-c12a8415-1b4b-4f28-9e89-467395ecf050.png" height=”300”       width=1000” style= "text-align: center"> 
</p>

### :open_file_folder: Estructura de este repositorio

| Carpeta | Fichero         | Descripción                                            |
|---------|-----------------|--------------------------------------------------------|
| `main`  | `main`          | Se pasa el proyecto definitivo únicamente              |
|         | `ReadMe`        | Documentación y Resumen del proyecto                   |
| `dev`   | `flask-app`     | Ficheros necesarios para el despliegue con Flask api   |
|         | `Scraping`      | Método de scraping o raspado de las ofertas            |
|         | `Similitud_CV`  | Análisis de los CVs y similitud con ofertas            |


### :construction: Futuras modificaciones o implementaciones
En un futuro se pretende utilizar otros servicios que nos proporciona Azure, como son el analizador de textos y sus bases de datos o almacenamiento para mejorar y complementar lo desarrollado hasta el momento. 

### :computer: Tecnologías aplicadas
- <b>Organización:</b> Metodología SCRUM y Trello https://trello.com/b/y6roy7yV/analisiscv
- <b>Cloud:</b> Microsoft Azure
- <b>Lenguajes utilizados:</b> Python, HTML5 y CSS3.
- <b>Librerías utilizadas:</b> FlaskAPI, dotenv. SpaCy, NLTK, Selenium, Beautifulsoup
- <b>Documentación:</b> MarkDown y Swagger
- <b>Framework:</b> Boostrap
- <b>Presentación:</b> Canvas
- <b>Control de versiones:</b> Git/GitHub
- <b>Contenedor:</b> Docker
- <b>Editores:</b> Jupyter, Visual Studio Code

### Requerimientos
Estas son las librerías utilizadas en el desarrollo del proyecto. Se encuentran en el archivo "requirements.txt" con sus respectivas versiones.
- <b>azure_storage</b>
- <b>docx</b>
- <b>Flask</b>
- <b>ftfy</b>
- <b>nltk</b>
- <b>numpy</b>
- <b>pandas</b>
- <b>pyresparser</b>
- <b>python-dotenv</b>
- <b>python_docx</b>
- <b>scikit_learn</b>
- <b>Werkzeug</b>
