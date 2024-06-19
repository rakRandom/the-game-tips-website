-- MySQL database
-- Create before run 'app.py'

CREATE DATABASE IF NOT EXISTS `flask`;
USE `flask`;

CREATE TABLE IF NOT EXISTS `user` (
    `id` INT NOT NULL,
    `name` VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

