def create_tb_students():
    sql= """
        CREATE TABLE IF NOT EXISTS tb_students(
            generated_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_reference varchar(100) NOT NULL UNIQUE,
            student_index varchar(100) NOT NULL UNIQUE,
            student_firstname varchar(50) NOT NULL,
            student_lastname varchar(25) NOT NULL,
            student_program varchar(100) NOT NULL
            )
        """
    return sql

def create_tb_compute_face_value():
    sql= """
        CREATE TABLE IF NOT EXISTS tb_face_values(
            generated_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_reference varchar(100) NOT NULL UNIQUE,
            student_face_encoding TEXT NOT NULL,
            FOREIGN KEY(student_reference) REFERENCES tb_students(student_reference) ON DELETE CASCADE ON UPDATE CASCADE
            )
        """
    return sql