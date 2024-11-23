import json
import re
from pprint import pprint
from typing import Union


class Book:
    """Класс для книги."""

    def __init__(
            self,
            title: str,
            author: str,
            year: str,
            status: str = 'в наличии'
    ):
        self.id = id(self)
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __json__(self):
        """Для сериализации/десериализации в JSON."""
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status
        }


class Library:
    """Класс управления книгами."""

    def __init__(self, filename="library.json"):
        self.filename = filename
        self.load_data()

    def load_data(self):
        """
        Вызывается перед каждой функцией.
        Загружает список словарей с книгами из JSON-файла.
        """
        try:
            with open(self.filename, "r") as f:
                self.books = json.load(f)
        except FileNotFoundError:
            self.books = []
        except json.decoder.JSONDecodeError:
            self.books = []
        except Exception as e:
            print(f'{e}')

    def save_data(self):
        """Сохраняет список словарей с книгами в JSON-файл."""
        with open(self.filename, "w") as f:
            json.dump(self.books, f)

    def add_book(self, book_string: str) -> None:
        """
        Создаёт объект книги и закидывает его в рабочий список словарей книг.
        """
        try:
            title, author, year = re.split(r"[\,|\s]\s", book_string)
            new_book = Book(title=title, author=author, year=year)
            self.books.append(new_book.__json__())
            self.save_data()
            print(f'Книга {title} добавлена')
        except ValueError:
            print('Некорректный ввод')
        except Exception as e:
            print(f'Ошибка: {e}, попробуй иначе')

    def del_book(self, book_id: int) -> None:
        """
        Перебирает список словарей с книгами по id и удаляет.
        """
        for index, book in enumerate(self.books):
            if book['id'] == book_id:
                del self.books[index]
                print(f'Книга с id {book_id} удалена')
                break
        else:
            print('Такой книги нет')
        self.save_data()

    def search_book(self, query: Union[int, str]) -> None:
        """
        Фильтрует список книг по названию или автору или году.
        """
        founded = list(filter(lambda d: query in d.values(), self.books))
        if founded:
            pprint(founded)
        else:
            print('Такой книги нет')

    def view_all(self) -> None:
        """
        Выводит список всех книг с их id, title, author, year и status.
        """
        pprint(self.books)

    def change_book_status(self, query: Union[int, str]) -> None:
        """
        Фильтрует список книг по id, меняет у подходящей статус.
        """
        book_id, status = re.split(r"[\,|\s]\s", query)
        changed = list(filter(
            lambda dict_book: dict_book['id'] == int(book_id), self.books))
        if changed:
            changed[0]['status'] = status
            print(f'Статус {book_id} изменён')
        else:
            print('Такой книги нет')
        self.save_data()
