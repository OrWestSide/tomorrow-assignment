CREATE DATABASE IF NOT EXISTS uber2;
use uber2;

-- Users
DROP TABLE IF EXISTS users;
CREATE TABLE users(
   id INT AUTO_INCREMENT PRIMARY KEY,
   username VARCHAR(255) NOT NULL,
   passwd VARCHAR(255) NOT NULL,
   survey_id INT
);
INSERT INTO users(username, passwd, survey_id) 
VALUES 
	('username1','passwd1', 1),
	('username2','passwd2', NULL),
	('username3','passwd3', NULL),
	('username4','passwd4', 2),
	('username5','passwd5', NULL);

-- Drivers
DROP TABLE IF EXISTS drivers;
CREATE TABLE drivers(
   id INT AUTO_INCREMENT PRIMARY KEY,
   name VARCHAR(255) NOT NULL
);

INSERT INTO drivers(name) 
VALUES 
	('name1'),
	('name2'),
	('name3');

-- Questions
DROP TABLE IF EXISTS questions;
CREATE TABLE questions(
   id INT AUTO_INCREMENT PRIMARY KEY,
   question_type ENUM ('single','multiple','free') NOT NULL,
   question_text VARCHAR(255) NOT NULL
);
INSERT INTO questions(question_type, question_text) 
VALUES 
	('single', 'Gender:'),
	('multiple', 'What did you enjoy in your ride?'),
	('multiple', 'What extras would you add to the vehicle?'),
	('free', 'Describe your ride');

-- Answers
DROP TABLE IF EXISTS answers;
CREATE TABLE answers(
   id INT AUTO_INCREMENT PRIMARY KEY,
   question_id INT NOT NULL,
   answer_text VARCHAR(255) NOT NULL
);
INSERT INTO answers(question_id, answer_text) 
VALUES 
	(1, 'Male'),
	(1, 'Female'),
	(2, 'It was a fast ride'),
	(2, 'Driver was friendly'),
	(2, 'Vehicle was air conditioned'),
	(3, 'Wifi'),
	(3, 'Tissues'),
	(3, 'Refreshments');

-- Surveys
DROP TABLE IF EXISTS surveys;
CREATE TABLE surveys(
   id INT AUTO_INCREMENT PRIMARY KEY,
   survey_name VARCHAR(255) NOT NULL
);
INSERT INTO surveys(survey_name) 
VALUES 
	('Ride'),
	('Extras');

-- Survey questions
DROP TABLE IF EXISTS survey_questions;
CREATE TABLE survey_questions(
   id INT AUTO_INCREMENT PRIMARY KEY,
   survey_id INT NOT NULL,
   question_id INT NOT NULL
);
INSERT INTO survey_questions(survey_id, question_id) 
VALUES 
	(1, 1),
	(1, 2),
	(1, 4),
	(2, 1),
	(2, 3),
	(2, 4);

-- Ratings
DROP TABLE IF EXISTS ratings;
CREATE TABLE ratings(
   id INT AUTO_INCREMENT PRIMARY KEY,
   user_id INT NOT NULL,
   driver_id INT NOT NULL,
   rating ENUM ('1', '2', '3', '4', '5') NOT NULL,
   rated_at TIMESTAMP NOT NULL
);

-- User answers
DROP TABLE IF EXISTS user_answers;
CREATE TABLE user_answers(
   id INT AUTO_INCREMENT PRIMARY KEY,
   user_id INT NOT NULL,
   driver_id INT NOT NULL,
   survey_id INT NOT NULL,
   question_id INT NOT NULL,
   answer_text VARCHAR(255),
   answered_at TIMESTAMP NOT NULL
);

-- Apply constraints and foreign key references
ALTER TABLE users ADD FOREIGN KEY (survey_id) REFERENCES surveys(id);
ALTER TABLE answers ADD FOREIGN KEY (question_id) REFERENCES questions(id);
ALTER TABLE survey_questions ADD FOREIGN KEY (survey_id) REFERENCES surveys(id);
ALTER TABLE survey_questions ADD FOREIGN KEY (question_id) REFERENCES questions(id);
ALTER TABLE ratings ADD FOREIGN KEY (user_id) REFERENCES users(id);
ALTER TABLE ratings ADD FOREIGN KEY (driver_id) REFERENCES drivers(id);
ALTER TABLE user_answers ADD FOREIGN KEY (user_id) REFERENCES users(id);
ALTER TABLE user_answers ADD FOREIGN KEY (driver_id) REFERENCES drivers(id);
ALTER TABLE user_answers ADD FOREIGN KEY (survey_id) REFERENCES surveys(id);
ALTER TABLE user_answers ADD FOREIGN KEY (question_id) REFERENCES questions(id);

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root';
