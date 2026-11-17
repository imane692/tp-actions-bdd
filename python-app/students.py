
import psycopg2


def add_student(conn, name, grade):
    """Ajouter un étudiant dans la base de données."""
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO students (name, grade) VALUES (%s, %s) RETURNING id",
            (name, grade)
        )
        student_id = cur.fetchone()[0]

    conn.commit()
    return student_id


def get_student(conn, student_id):
    """Lire un étudiant à partir de son identifiant."""
    with conn.cursor() as cur:
        cur.execute(
            "SELECT name, grade FROM students WHERE id = %s",
            (student_id,)
        )
        student = cur.fetchone()

    if student is None:
        return None

    return (student[0], float(student[1]))



def average_grade(conn):
    """Calculer la moyenne des notes."""
    with conn.cursor() as cur:
        cur.execute("SELECT AVG(grade) FROM students")
        result = cur.fetchone()

    return float(result[0]) if result[0] is not None else None

