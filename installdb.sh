# Crear la BD y el usuario con su password y demás configuracion
sudo -u postgres dropdb todoapp_db >> /dev/null
sudo -u postgres dropuser todoList >> /dev/null
sudo -u postgres createuser todoList
sudo -u postgres createdb todoapp_db
echo "Created database and management user in postgres"
sudo -u postgres psql << EOF
alter user todoList with encrypted password 'todolist';
grant all privileges on database todoapp_db to todoList ;\q
EOF
echo "Granted privileges on database to user"

echo "Eliminating past migrations, if any"
# Quitar migraciones pasadas e inicializar el manejador de la BD
rm -r todoListApp/migrations >> /dev/null
