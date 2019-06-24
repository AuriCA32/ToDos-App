# Crear la BD y el usuario con su password y demás configuracion
sudo -u postgres dropdb todoapp_db >> /dev/null
sudo -u postgres dropuser todolist >> /dev/null
#sudo -u postgres createuser todolist
sudo -u postgres createdb todoapp_db
echo "Created database and management user in postgres"
sudo -u postgres psql << EOF
create role todolist with password 'todolist';
alter role todolist with login; 
alter user todolist with password 'todolist';
alter role todolist set client_encoding to 'utf8';
alter role todolist set default_transaction_isolation to 'read committed';
alter role todolist set timezone to 'utc';
alter role todolist createdb;
grant all privileges on database todoapp_db to todolist ;\q
EOF
echo "Granted privileges on database to user"

echo "Eliminating past migrations, if any"
# Quitar migraciones pasadas e inicializar el manejador de la BD
rm -r todoListApp/migrations >> /dev/null
