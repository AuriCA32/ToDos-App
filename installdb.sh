# Crear la BD y el usuario con su password y demás configuracion
sudo -u postgres dropdb todoapp_db >> /dev/null
sudo -u postgres dropuser todoList >> /dev/null
sudo -u postgres createuser todoList
sudo -u postgres createdb todoapp_db
sudo -u postgres psql << EOF
alter user todoList with encrypted password 'todoList123';
alter role todoList set client_encoding to 'utf8';
alter role todoList set default_transaction_isolation to 'read committed';
alter role todoList set timezone to 'utc';
alter role todoList createdb;
grant all privileges on database todoapp_db to todoList ;\q
EOF

# Quitar migraciones pasadas e inicializar el manejador de la BD
rm -r tourappAPI/migrations >> /dev/null
