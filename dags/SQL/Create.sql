CREATE TABLE IF NOT EXISTS pet (
    pet_id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    pet_type VARCHAR NOT NULL,
    birth_date DATE NOT NULL,
    OWNER VARCHAR NOT NULL);

CREATE TABLE IF NOT EXISTS Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);