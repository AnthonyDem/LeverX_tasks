CREATE_TABLE = [

    """"
    CREATE TABLE IF NOT EXISTS rooms(
            id INT PRIMARY KEY,
            name VARCHAR(100) NOT NULL
    );
    """,
    """   
    CREATE TABLE IF NOT EXISTS students(
            id INT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            birthday DATE NOT NULL,
            room INT NOT NULL, 
            sex ENUM("M","F") NOT NULL,
            FOREIGN KEY (room_id) REFERENCES rooms(id) ON DELETE CASCADE
    );
    """

]

SELECT_DATA = [
    """
    SELECT  rooms.id , rooms.name , COUNT (students.id)
    FROM rooms
    JOIN students ON rooms.id = students.room_id
    GROUP BY rooms.id , rooms.name
    """,
    """
    SELECT rooms.id , rooms.name , AVG(TIMESTAMPDIFF(YEAR, students.birthday,NOW)) as avg_age
    FROM rooms
    JOIN students ON rooms.id = students.room_id
    GROUP BY rooms.id , rooms.name
    ORDER BY avg_age
    LIMIT 5
    """,
    """
    SELECT rooms.id , rooms.name , TIMESTAMPDIFF(YEAR , MAX(students.birthday) , MIN(students.birthday)) as max_diff
    FROM rooms
    JOIN students ON rooms.id = students.room_id
    GROUP BY rooms.id , rooms.name
    ORDER BY max_diff DESC
    LIMIT 5
    """,
    """
    SELECT DISTINCT rooms.id , rooms.name , COUNT(DISTINCT students.sex) as sex
    FROM rooms
    JOIN students ON rooms.id = students.room_id
    GROUP BY rooms.id , rooms.name
    HAVING sex = 2
    """,

]

CREATE_INDEX = [
    "CREATE INDEX roomid ON students(room_id);",
]
