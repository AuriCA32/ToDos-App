### django postgresql heroku
# To-Dos App

## Descripción

To-Dos App se trata de una mini-aplicación desarrollada en Django 2.1 para el manejo de tareas (*TODOs*) por un conjunto de usuarios. Se incluyen las siguientes funcionalidades:

* Registrar un usuario.
* Ingresar con un usuario existente.
* Mostrar mensaje de errores en el login/signup.
* Cerrar sesión.
* Obtener la lista de tareas y su estado actual.
* Agregar tareas a la lista de TODOs.
* Marcar una tarea como resuelta.
* Editar los campos de una tarea.
* Eliminar una tarea.


## Setup

### Prólogo

Asegurarse de tener instalado lo siguiente (las versiones utilizadas también se indican):
* PostgreSQL(v. 9.5.17)
* Virtualenv(v.15.0.1)
* pip(19.1.1) para python 3.7

### Configuración del entorno

Cree un virtual environment con python3 como python por defecto en la carpeta del proyecto con:

        virtualenv env --python=$(which python3)

Active el environment:

        source env/bin/bash/activate

Para salir del entorno, puede hacer:

        deactivate

Ahora, se deben instalar los paquetes necesarios:

        pip install -r requirements.txt


### Inicialización de la BD / Migraciones

Se proporcionan scripts para realizar las operaciones. Antes que nada, se deben otorgar a los mismos permisos de ejecución:

        chmod +x installdb.sh migrate.sh

El primer script sirve para *crear* la BD y el usuario para manejarla con su clave. Para ejecutarlo:

        ./installdb.sh

El segundo script se encarga de *hacer las migraciones y actualizar la BD*.

        ./migrate.sh
