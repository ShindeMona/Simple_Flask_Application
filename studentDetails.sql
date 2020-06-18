CREATE DATABASE studentInfo;
USE studentInfo;
CREATE TABLE login(id integer AUTO_INCREMENT PRIMARY KEY NOT NULL,username varchar(30),password varchar(30));
CREATE TABLE student(rollId integer AUTO_INCREMENT PRIMARY KEY NOT NULL,name varchar(30) NOT NULL,username varchar(30),password varchar(30) NOT NULL,bdate text,s1 varchar(20),s2 varchar(20),s3 varchar(20),s4 varchar(20),s5 varchar(20));

