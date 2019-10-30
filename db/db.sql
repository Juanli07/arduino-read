CREATE DATABASE acdb;
USE acdb;

CREATE TABLE users(
    email VARCHAR(30) PRIMARY KEY,    
    name VARCHAR(30),
    password VARCHAR(30)
);

CREATE TABLE ac(
    id_ac VARCHAR(3) PRIMARY KEY,
    temp INT(3),
    status INT(1)
);

CREATE TABLE regforhour(
    id_ac VARCHAR(3),
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, --TIMESTAMP is YYYY-MM-DD HH:MM:SS
    status INT(1),
    motionsen INT(2),
    FOREIGN KEY(id_ac) REFERENCES ac(id_ac)
);

CREATE TABLE regforday(
    date DATE, ---date is YYYY-MM-DD
    average_temp INT(4),
    time_on INT(6)
);