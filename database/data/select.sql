SELECT * FROM User;
SELECT * FROM UserDayLog;
SELECT * FROM UserGoals;
SELECT * FROM UserInfo;

SELECT User.user_id,user_name,email,created_date FROM User
    INNER JOIN UserInfo on User.user_id=UserInfo.user_id;

SELECT * FROM User
    INNER JOIN UserGoals on User.user_id=UserGoals.user_id;

SELECT * FROM User
    INNER JOIN UserDayLog on User.user_id=UserDayLog.user_id;