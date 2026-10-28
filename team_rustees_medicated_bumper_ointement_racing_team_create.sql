CREATE TABLE Track_Info (
track_Type_ID INT PRIMARY KEY,
track_Type VARCHAR(50) NOT NULL);

CREATE TABLE Track (
track_ID INT PRIMARY KEY,
track_Name VARCHAR(100) NOT NULL,
track_Type_ID INT,
FOREIGN KEY (track_Type_ID) REFERENCES Track_Info(track_Type_ID));

CREATE TABLE Flag_Info (
flag_State INT PRIMARY KEY,
flag_Color VARCHAR(30) NOT NULL);

CREATE TABLE Team_Info (
team_ID INT PRIMARY KEY,
team_Name VARCHAR(100) NOT NULL);

CREATE TABLE Driver_Info (
driver_ID INT PRIMARY KEY,
first_Name VARCHAR(50) NOT NULL,
last_Name VARCHAR(50) NOT NULL,
team_ID INT,
FOREIGN KEY (team_ID) REFERENCES Team_Info(team_ID));

CREATE TABLE Race (
race_ID INT PRIMARY KEY
race_Date DATE NOT NULL
race_Name VARCHAR(100)
track_ID INT,
track_Type_ID INT
FOREIGN KEY (track_ID) REFERENCES Track(track_ID),
FOREIGN KEY (track_Type_ID) REFERENCES Track_Info(track_Type_ID));

CREATE TABLE Events (
event_ID INT PRIMARY KEY,
lap_Number INT, 
flag_State INT,
notes TEXT,
FOREIGN KEY (flag_State) REFERENCES Flag_Info(flag_State));

CREATE TABLE Race_Events (
race_ID INT,
event_ID INT,
PRIMARY KEY (race_ID, event_ID), 
FOREIGN KEY (race_ID) REFERENCES Race(race_ID),
FOREIGN KEY (event_ID) REFERENCES Events(event_ID));

CREATE TABLE Lap_Info (
driver_ID INT,
race_ID INT,
lap_Number INT,
position_Number INT,
lap_Speed DECIMAL(6,3),
PRIMARY KEY (driver_ID, race_ID, lap_Number),
FOREIGN KEY (driver_ID) REFERENCES Driver_Info(driver_ID),
FOREIGN KEY (race_ID) REFERENCES Race(race_ID));

CREATE TABLE Pitstop_Info (
race_ID INT,
driver_ID INT,
lap_Number INT,
duration DECIMAL(5,2),
position_Lost_Or_Gained INT,
PRIMARY KEY (race_ID, driver_ID, lap_Number),
FOREIGN KEY (race_ID) REFERENCES Race(race_ID),
FOREIGN KEY (driver_ID) REFERENCES Driver_Info(driver_ID) );

CREATE TABLE Results (
race_ID INT,
driver_ID INT,
start_Position INT,
finish_Position INT,
PRIMARY KEY (race_ID, driver_ID),
FOREIGN KEY (race_ID) REFERENCES Race(race_ID),
FOREIGN KEY (driver_ID) REFERENCES Driver_Info(driver_ID) );
