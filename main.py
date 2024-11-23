from library_of_books import Library


def main():
    library = Library()
    while True:
        match input(
                'Выберите номер действия:\n'
                ' 1: Добавить книгу\n'
                ' 2: Удалить книгу\n'
                ' 3: Поиск книги\n'
                ' 4: Отобразить все книги\n'
                ' 5: Изменение статуса книги\n'
                ' e или q: для выхода из программы\n'):
            case '1':
                library.add_book(input(
                    'Введите название, автора и год книги через запятую'
                    ' (например: Гарри Поттер и филосовский камень,'
                    ' Джоан Роулинг, 1997):\n'))
            case '2':
                library.del_book(int(input(
                    'Введите id книги, которую хотите удалить:\n')))
            case '3':
                library.search_book(input(
                    'Введите название или автора или год для поиска книг\n:'))
            case '4':
                library.view_all()
            case '5':
                library.change_book_status(input(
                    'Введите id и новый статус книги (в наличии или выдана)'
                    ' через запятую:\n'))
            case 'e' | 'q' | 'у' | 'й':
                break
            case _:
                print('Неверный номер')


if __name__ == '__main__':
    main()
