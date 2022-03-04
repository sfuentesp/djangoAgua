## Nombre del proyecto
Tomate el agua en serio

## Decripción "tomate el agua en serio"
EL proyecto es una iniciativa que consiste en tomar conciencia sobre la problema 
de la escasez hidrica, con el objetivo de regsitrar los consumo de agua mes a mes a travez 
de una plataforma web

## Autor
Simón Fuentes

## Instalación
Debe instalar python 3.9
una ves instalado python debe iniciar un entorno virtual para poder instalar las dependencias necesarias,
puede instalar los componentes desde el archivo requirements.txt o ejecutar el comando pip install "nombre de app"
asgiref==3.5.0
Django==4.0.2
django-crispy-forms==1.14.0
gunicorn==20.1.0
Pillow==9.0.1
psycopg2==2.9.3
sqlparse==0.4.2

El sistema trabaja con un motor de base de datos postgresql por ende debe instalar aquel motor de base de datos

despues en el settigns.py debes moficar el nombre de usuario y password en en la parte de base de datos por los valore que dejaste al momento de instalar postgresql

Por ultimos debes ejecutar el comando de python manage.py migrate para generar las tablas en el motor segun los modelos 
que estan creados en el proyecto

## Estructura del proyecto
### App
  - boleta
  - contacto
  - usuario
### Formularios
  - FormBoleta: despliega formulario para ingresar registro de las boletas
  - VoluntarioForm: Ingresar nuevos voluntarios
  - ResponsabilidadForm: Ingresar responsabilidad para nutrir el form de voluntario
  - PostForm: sirve para postear segun usuario 
  - UserForm2: crear usuario v2
  - UserForm: crear usuario
## Funcionalidad
  Sistema cuena con un login y link de registro
  al registrarse podra ingresar post en relacion al tema y tambien podra ingresarsus boletas y un listado y resumen 
  de sus ingresos