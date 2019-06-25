
# Actualizar la BD
python3 manage.py makemigrations todoListApp

# Hacer las migraciones de los cambios realizados
python3 manage.py migrate
python3 manage.py migrate --database=todolist-app