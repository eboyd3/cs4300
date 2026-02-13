from src.task5 import favorite_books, first_three_books, student_database

def test_favorite_books_length():
    books = favorite_books()
    assert len(books) == 6

def test_first_three_books():
    first_three = first_three_books()
    expected = [
        ("The Way of Kings", "Brandon Sanderson"),
        ("Oathbringer", "Brandon Sanderson"),
        ("1984", "George Orwell"),
    ]
    assert first_three == expected

def test_student_database_keys():
    students = student_database()
    expected_keys = {"Luffy", "Jojo", "Illyana", "Kaladin"}
    assert set(students.keys()) == expected_keys


def test_student_database_values():
    students = student_database()
    expected_values = {1001, 1002, 1003, 1004}
    assert set(students.values()) == expected_values


def test_student_database_length():
    students = student_database()
    assert len(students) == 4
