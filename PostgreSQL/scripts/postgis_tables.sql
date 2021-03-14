
SET temp_file_limit  = 37050832 ; 

CREATE USER test;

CREATE DATABASE postgres WITH OWNER postgres;

GRANT ALL PRIVILEGES ON DATABASE postgres TO postgres,test,docker;

\connect postgres;


SET temp_file_limit  = 37050832 ; 

CREATE EXTENSION postgis VERSION "2.3.3";
--	CREATE EXTENSION postgis_raster VERSION "2.3.3";
--	CREATE EXTENSION postgis_sfcgal;
--	CREATE EXTENSION address_standardizer;
--	CREATE EXTENSION fuzzystrmatch;
--	CREATE EXTENSION postgis_topology;
--	CREATE EXTENSION postgis_tiger_geocoder;


CREATE TABLE IF NOT EXISTS products (
    product_no integer,
    name varchar(10),
    price numeric
);

INSERT INTO products (product_no, name, price) VALUES (1, 'Cheese', 9.99);
INSERT INTO products (name, price, product_no) VALUES ('Butter', 10.08, 2);
INSERT INTO products (product_no, name, price) VALUES (3, 'Jam', 19.99);
INSERT INTO products (product_no, name, price) VALUES (4, 'Bread', 9.88);
INSERT INTO products (product_no, name, price) VALUES (5, 'Toast', 3.99);
INSERT INTO products (product_no, name, price) VALUES (6, 'Sandwitch', 8.5);
INSERT INTO products (product_no, name, price) VALUES (7, 'Dosa', 30.4);
INSERT INTO products (product_no, name, price) VALUES (8, 'Idli', 9.43);


COMMIT;

