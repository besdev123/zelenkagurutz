import sqlite3


def add_newBook(title: str, author: str, description: str, genre_id: int) -> None:
    """Database func to add new book into books table

    Args:
        title (str): title of book
        author (str): author of book
        description (str): description of book
        genre_id (int): id of genre from genres table
    """
    with sqlite3.connect("data/db.db") as db:
        db.execute("INSERT INTO books (title, author, description, genre_id) VALUES (?, ?, ?, ?)", 
                   (title, author, description, genre_id,))
        db.commit()



def del_book(book_id: int) -> None:
    """Func to delete book

    Args:
        book_id (int): _description_
    """
    with sqlite3.connect("data/db.db") as db:
        db.execute("DELETE FROM books WHERE id = ?", 
                   (book_id,))
        db.commit()



def get_books() -> list:
    """Database func to get all books from books table

    Returns:
        list: [(id, title, author, description, genre_id)]
    """
    with sqlite3.connect("data/db.db") as db:
        cursor = db.execute("SELECT * FROM books")
        result = cursor.fetchall()
        return result
    


def get_booksByWord(word: str) -> list:
    """Database func to get all books from books table

    Args:
        word (str): _description_

    Returns:
        list: [(id, title, author, description, genre_id)]

    """
    with sqlite3.connect("data/db.db") as db:
        cursor = db.execute("SELECT * FROM books WHERE author LIKE ? OR title LIKE ?",
                            ("%" + word + "%", "%" + word + "%",))
        result = cursor.fetchall()
        return result



def get_booksByGenre(genre_id: int) -> list:
    """Get books from books by genre

    Args:
        genre_id (int): _description_

    Returns:
        list: [(id, title, author, description, genre_id)]
    """
    with sqlite3.connect("data/db.db") as db:
        cursor = db.execute("SELECT * FROM books WHERE genre_id = ?",
                            (genre_id,))
        result = cursor.fetchall()
        return result



def get_book(book_id: int) -> tuple:
    """Get book from books by book id

    Args:
        book_id (int): _description_

    Returns:
        tuple: (id, title, author, description, genre_id)
    """
    with sqlite3.connect("data/db.db") as db:
        cursor = db.execute("SELECT * FROM books WHERE id = ?",
                            (book_id,))
        result = cursor.fetchone()
        return result



def get_genres() -> list:
    """Database func to get all genres from genres table

    Returns:
        list: [(genre_id, genre_title)]
    """
    with sqlite3.connect("data/db.db") as db:
        cursor = db.execute("SELECT * FROM genres")
        result = cursor.fetchall()
        return result



def get_genreByID(genre_id: int) -> tuple:
    """Database func to get genre from genres table

    Args:
        g_id (int): genre title

    Returns:
        tuple: (genre_id, genre_title)
    """
    with sqlite3.connect("data/db.db") as db:
        cursor = db.execute("SELECT * FROM genres WHERE g_id = ?",
                            (genre_id,))
        result = cursor.fetchone()
        return result



def get_genreByTitle(genre_title: str) -> tuple:
    """Database func to get genre from genres table

    Args:
        g_id (int): genre title

    Returns:
        tuple: (genre_id, genre_title)
    """
    with sqlite3.connect("data/db.db") as db:
        cursor = db.execute("SELECT * FROM genres WHERE genre_title = ?",
                            (genre_title,))
        result = cursor.fetchone()
        return result
    


def add_newGenre(genre_title: str) -> None:
    """Database func to add new genre into genres table

    Args:
        genre_title (str): title of genre
    """
    with sqlite3.connect("data/db.db") as db:
        db.execute("INSERT INTO genres (genre_title) VALUES (?)", 
                   (genre_title,))
        db.commit()