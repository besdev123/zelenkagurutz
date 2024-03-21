import os, time

from data import database


def main() -> None:
    """Main script func
    """
    os.system("cls")
    action = input("Выберите действие: \n\n"
                   "1. Добавить книгу \n"
                   "2. Список книг \n"
                   "3. Поиск книги \n"
                   "4. Удалить книгу \n\n")
    
    try:
        match int(action):
            case 1: add_book()

            case 2: all_books()

            case 3: search_book()

            case 4: delete_book()

            case _: 
                print("Введите цифру в диапазоне 1-4")
                time.sleep(2)
                return
    
    except ValueError:
        print("Введите цифру, не строку")
        time.sleep(2)
        return



def add_book() -> None:
    """Handler to add book
    """
    os.system("cls")

    title = input("Введите название книги: \n\n")
    author = input("Введите автора книги: \n\n")
    description = input("Введите описание книги: \n\n")

    text = ""
    genres = database.get_genres()
    for i in genres:
        text += f"{i[0]} | {i[1]} \n"

    genre = input("Введите жанр книги: \n\n"
                  + text
                  + "\nВы так же можете создать новый жанр. \n"
                  "Для этого введите название нового жанра \n\n")
    
    if (database.get_genreByTitle(genre)) is None:
        database.add_newGenre(genre)
        print(f"Создан новый жанр {genre}")

    genre_db = database.get_genreByTitle(genre) 
    database.add_newBook(title, author, description, genre_db[0])

    print("Книга создана!")
    time.sleep(2)
    return



def all_books() -> None:
    """Handler to view all books
    """
    os.system("cls")

    text = ""
    books = database.get_books()
    for i in books:
        genre = database.get_genreByID(i[-1])
        text += f"{i[0]} | {i[1]} | {genre[1]} \n"

    action = input(text +
                   "\nВведите идентификатор книги для ее открытия \n"
                   "Либо, введите жанр, в котором нужно вывести книги: \n\n")
    
    if action.isdigit():
        open_book(action)
    
    else:
        genre_db = database.get_genreByTitle(action)

        if genre_db is None:
            print("Жанр не найден")
            time.sleep(2)
            return

        books = database.get_booksByGenre(genre[0])

        for i in books:
            input(f"{i[0]} | {i[1]} | {i[2]} | {i[3]} | {genre_db[1]} \n\n"
                    "Для возврата меню, введите любой символ: \n\n")
        return



def open_book(book_id: int) -> None:
    """Func to open book by id

    Args:
        book_id (int): _description_
    """
    os.system("cls")

    book = database.get_book(book_id)

    if book is None:
        print("Введён неверный идентификатор книги")
        time.sleep(2)
        return
    
    genre = database.get_genreByID(book[-1])

    input(f"{book[0]} | {book[1]} | {book[2]} | {book[3]} | {genre[1]} \n\n"
                    "Для возврата меню, введите любой символ: \n\n")
    return



def search_book() -> None:
    """Handler to search book
    """
    os.system("cls")
    action = input("Введите ключевое слово или фразу для поиска: \n\n")

    books = database.get_booksByWord(action)
    if len(books) == 0:
        print("Ничего не найдено..")
        time.sleep(2)
        return

    text = ""
    for i in books:
        genre = database.get_genreByID(i[-1])
        text += f"{i[0]} | {i[1]} | {i[2]} | {i[3]} | {genre[0]} \n"
    input(text +
        "\nДля возврата меню, введите любой символ: \n\n")



def delete_book() -> None:
    """Handler to delete book
    """
    os.system("cls")

    text = ""
    books = database.get_books()
    for i in books:
        genre = database.get_genreByID(i[-1])
        text += f"{i[0]} | {i[1]} | {genre[1]} \n"

    book_id = input(text +
                   "\nВведите идентификатор книги для ее удаления \n")
    database.del_book(book_id)
    print("Удалено")

    time.sleep(2)
    return



while True:
    main()
