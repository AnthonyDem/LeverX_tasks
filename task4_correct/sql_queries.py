class Queries:
    @staticmethod
    def create_queries():
        return [
            """CREATE TABLE IF NOT EXISTS rooms
                        (
                            id INT PRIMARY KEY,
                            name VARCHAR(50) NOT NULL
                        );"""
            ,
            """
                    CREATE TABLE IF NOT EXISTS students
                        (
                            id INT PRIMARY KEY,
                            name VARCHAR(50) NOT NULL,
                            birthday DATE NOT NULL,
                            room_id INT NOT NULL, 
                            sex ENUM("M","F") NOT NULL,
                            FOREIGN KEY (room_id) REFERENCES rooms(id) 
                                ON DELETE CASCADE
                        );"""

        ]





    @staticmethod
    def select_queries():
        return [

            """
            SELECT  rooms.id , rooms.name , COUNT (students.id)
            FROM rooms
            JOIN students ON rooms.id = students.room_id
            GROUP BY rooms.id  
            """,
            """
            SELECT rooms.id , rooms.name , AVG(TIMESTAMPDIFF(YEAR, students.birthday,NOW)) as avg_age
            FROM rooms
            JOIN students ON rooms.id = students.room_id
            GROUP BY rooms.id 
            ORDER BY avg_age
            LIMIT 5
            """,
            """
            SELECT rooms.id , rooms.name , TIMESTAMPDIFF(YEAR , MAX(students.birthday) , MIN(students.birthday)) as max_diff
            FROM rooms
            JOIN students ON rooms.id = students.room_id
            GROUP BY rooms.id
            ORDER BY max_diff DESC
            LIMIT 5
            """,
            """
            SELECT DISTINCT rooms.id , rooms.name , COUNT(DISTINCT students.sex) as sex
            FROM rooms
            JOIN students ON rooms.id = students.room_id
            GROUP BY rooms.id 
            HAVING sex = 2
    """,

        ]

    @staticmethod
    def idex_query():
        return "CREATE INDEX roomid ON students(room_id);",
