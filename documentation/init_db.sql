CREATE USER user_gestion_db PASSWORD 'pwd_gestion_db';
ALTER ROLE user_gestion_db WITH SUPERUSER;
CREATE DATABASE gestiondb WITH OWNER user_gestion_db;