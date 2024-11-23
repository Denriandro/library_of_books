import json
import unittest

from library_of_books import Library, Book


class TestLibrary(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.books = [
            {'id': 1, 'title': 'test_title', 'author': 'test_author',
             'year': 'test_year', 'status': 'test_status'}]

    def setUp(self) -> None:
        """Перед каждым тестом загрузится список книг (self.library.books)."""
        self.library = Library(filename='test_library.json')

    def test_load_data(self):
        """Проверяет создан ли список для книг."""
        self.library.load_data()
        self.assertEqual(
            self.library.books, [], msg='Список словарей не создан')

    def test_save_data(self):
        """Проверяет сохраниться ли список книг."""
        self.library.save_data()
        with open('test_library.json', 'r') as f:
            data = json.load(f)
        self.assertEqual(self.library.books, data, 'save_data не сохраняет')

    def test_add_book(self):
        """Проверяет добавление книги по кол-ву,
        и соответствие названия, автора и года."""
        self.library.add_book('test_title, test_author, test_year')
        self.library.load_data()
        self.assertEqual(len(self.library.books), 1, 'Кол-во книг разное')
        self.assertEqual(self.library.books[0]['title'], 'test_title',
                         'Осутствует название книги')
        self.assertEqual(self.library.books[0]['author'], 'test_author',
                         'Осутствует автор книги')
        self.assertEqual(self.library.books[0]['year'], 'test_year',
                         'Осутствует год книги')

    def test_del_book(self):
        """Проверяет удаление по кол-ву книг в списке."""
        self.library.books = self.books
        self.library.del_book(1)
        self.library.load_data()
        self.assertEqual(len(self.library.books), 0, 'Книга не удалилась')

    def test_search_book(self):
        """
        Проверяет, что поиск выполняется без ошибок (не райзит эксепшены).
        """
        self.library.books = self.books
        self.assertIsNone(self.library.search_book('test_title'))
        self.assertIsNone(self.library.search_book('test_author'))
        self.assertIsNone(self.library.search_book('test_year'))

    def test_view_all(self):
        """Проверяет, что отображение выполняется без ошибок."""
        self.library.books = self.books
        self.assertIsNone(self.library.view_all())

    def test_change_book_status(self):
        """Проверяет изменение статуса."""
        self.library.books = self.books
        self.library.change_book_status('1, выдана')
        self.library.load_data()
        self.assertEqual(
            self.library.books[0]['status'], "выдана", 'Статус не изменяется')


if __name__ == '__main__':
    unittest.main(verbosity=2)
