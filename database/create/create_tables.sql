CREATE TABLE User (
    user_id INT NOT NULL AUTO_INCREMENT,
    user_name VARCHAR(25),
    email VARCHAR(40),
    pass_word VARCHAR(40),
    first_name VARCHAR(25),
    last_name VARCHAR(30),
    PRIMARY KEY (user_id)
);

CREATE TABLE UserDayLog (
    user_log_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    excercise_cals INT,
    food_cals INT,
    daily_cal INT,
    current_weight INT,
    c_date DATETIME,
    PRIMARY KEY (user_log_id),
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);


CREATE TABLE UserGoals (
    user_goal_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    goal_weight INT,
    daily_cal_goal INT,
    PRIMARY KEY (user_goal_id),
    FOREIGN KEY (user_id) REFERENCES User(user_id)

);

CREATE TABLE UserInfo (
    user_info_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    profile_bio VARCHAR(150),
    profile_picture VARCHAR(200),
    modified_date DATETIME,
    created_date DATETIME,
    PRIMARY KEY (user_info_id),
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

