<h1 align ="center"> Analizador de Cvs  </h1> 
<p align = "center">
<img src="https://user-images.githubusercontent.com/109460138/229610424-d0c0fc5d-8103-4f9c-931c-d0d222027f93.jpg" height=”300”       width=1000” style= "text-align: center"> 
</p>

## Proyecto 
Por encargo de la empresa Simplon, creamos un analizador de currículums para compararlos con ofertas de trabajo que se publican en sitios webs como Infojobs y, de esta manera, sacar su afinidad o match en forma de porcentaje. 

## Azure
Se utiliza el Cognitive Service de Azure para activar el Form Recognicer y poder extraer el texto de las imágenes por medio de la técnica OCR, Optical Character Recognition. También se utiliza el servicio de Contenedores con Docker. 

## Variables de Entorno requeridas
Los siguientes parámetros con necesarios para acceder a la conexión

| Variable de entorno              | Ejemplo                                                   |
|----------------------------------|-----------------------------------------------------------|
| `AZURE_FORM_RECOGNIZER_ENDPOINT` | `https://cv-recog-imagenes.cognitiveservices.azure.com`   | 
| `AZURE_FORM_RECOGNIZER_KEY`      | `b635ctertyh2c41d0bb1f8f612409fsdiifss7797`               | 

## Resultado
Esta es la solución del trabajo realizado, donde se puede apreciar diversos campos como el puesto, 
<p align = "center">
<img src="https://user-images.githubusercontent.com/109460138/229618274-61312145-1a4f-40ab-b4a6-a00ff321dbc1.png" height=”300”       width=1000” style= "text-align: center"> 
</p>

## Estructura de este repositorio

| Carpeta   | Fichero            | Descripción                                                       |
|-----------|--------------------|-------------------------------------------------------------------|
| `main`    | `xxxxxxxx`         | xxxxxxxxxxxxxxxxxx                                                |
| `dev`     | `xxxxxxx`          | xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx              |
|           | `xxxxxxxx`         | xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx              |
|           | `xxxxxxxx`         | xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx              |
|           | `xxxxxxxx`         | xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx              |           
|           | `xxxxxxxx`         | xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx              |


## Futuras modificaciones o implementaciones
En un futuro se pretende utilizar más servicios que nos proporciona Azure, como son el analizador de textos y sus bases de datos. 

## Tecnologías aplicadas
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
