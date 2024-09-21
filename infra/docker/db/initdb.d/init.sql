-- .env, .env.example, .env.testing など、DB_DATABASEの値に合わせること
CREATE DATABASE IF NOT EXISTS python_stations_4;
CREATE DATABASE IF NOT EXISTS python_stations_4_test;
GRANT ALL ON python_stations_4.* TO 'dev'@'%';
GRANT ALL ON python_stations_4_test.* TO 'dev'@'%';