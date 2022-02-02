# **Pasantic Backend - Django Rest Framework**
Backend administrador de la aplicación móvil para búsqueda de pasantías.

# Guía de instalación
## Entorno Virtual
Se necesita un entorno virtual, en el caso de contar con más de una versión de python especificar python3:
```
python -m venv <env-name>
```
Activar dicho entorno creado:
### Windows
```
<env-name>\Scripts\activate
```
### Linux
```
source <env-name>/bin/activate
```
Debe aparecer en el terminal/consola el nombre del entorno virtual entre paréntesis:
```
(<env-name>)
```
## Dependencias
Las dependencias están reunidas en el archivo [requirements](requirements.txt), basta con ejecutar:
```
(<env-name>) pip install -r requirements.txt
```
## Migraciones
Las migraciones corresponden a la creación de las tablas en la base de datos trabajada con *PostgreSQL*, primero se debe crear la base *DB_LOCAL_NAME* especificada en el .env  y luego se ejecuta:
```
(<env-name>) python manage.py migrate
```
## Configuración final
Solicitar el archivo .env a los colaboradores.
# Despliegue
**Luego** de instalar el proyecto se puede desplegar al ejecutar: 
```
python manage.py runserver
```
# Colaboradores
```
Xavier Carlier
Jeffrey Prado
Douglas Sabando
```