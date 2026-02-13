def favorite_books():
    books = [
        ("The Way of Kings", "Brandon Sanderson"),
        ("Oathbringer", "Brandon Sanderson"),
        ("1984", "George Orwell"),
        ("One Piece", "Eiichiro Oda"),
        ("The Hobbit", "J.R.R. Tolkien"),
        ("The Mark of Athena", "Rick Riordan"),
    ]
    return books


def first_three_books():
    books = favorite_books()
    return books[:3]

def student_database():

    students = {
        "Luffy": 1001,
        "Jojo": 1002,
        "Illyana": 1003,
        "Kaladin": 1004
    }
    return students
