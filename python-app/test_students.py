
import pytest
import psycopg2

from students import add_student, get_student, average_grade


@pytest.fixture
def conn():
    """Créer une connexion et préparer une table vide avant chaque test."""
    connection = psycopg2.connect(
        host="localhost",
        database="tp",
        user="postgres",
        password="postgres"
    )

    with connection.cursor() as cur:
        cur.execute("TRUNCATE TABLE students RESTART IDENTITY")

    connection.commit()

    yield connection

    connection.close()


def test_add_and_get(conn):
    student_id = add_student(conn, "Amel", 15)

    student = get_student(conn, student_id)

    assert student is not None
    assert student[0] == "Amel"
    assert student[1] == 15.0


def test_get_missing(conn):
    student = get_student(conn, 999)

    assert student is None


def test_moyenne(conn):
    add_student(conn, "Amel", 10)
    add_student(conn, "Karim", 14)

    assert average_grade(conn) == 12.0
