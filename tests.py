# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
# class TestBooksCollector:


# пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    # def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        # collector = BooksCollector()

        # добавляем две книги
        # collector.add_new_book('Гордость и предубеждение и зомби')
        # collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        # assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
# class TestBooksCollector:


# пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    # def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        # collector = BooksCollector()

        # добавляем две книги
        # collector.add_new_book('Гордость и предубеждение и зомби')
        # collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        # assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


# Мои тесты

import pytest
class TestBooksCollector:

# Проверка получения книги
    @pytest.mark.parametrize('name',["The Great Gatsby", "To Kill a Mockingbird", 'Fight Club', 'Idiot', 'Three Comrades','Of Mice and Men'])
    def test_add_new_book(self,collector,name):
        collector.add_new_book(name)
        assert collector.books_rating == {name: 1}
# Нельзя добавить одну и ту же книгу дважды
    def test_add_existing_book(self,collector,new_book):
        collector.add_new_book("The Great Gatsby")
        assert collector.books_rating == {"The Great Gatsby": 1}

# Проверка добавления рейтинга книг
    @pytest.mark.parametrize('name, rating',[["The Great Gatsby",7],["To Kill a Mockingbird",6],['Fight Club',7],['Idiot',9],['Three Comrades',8],['Of Mice and Men',7]])
    def test_set_book_rating(self,collector, name, rating):
        collector.add_new_book(name)
        collector.set_book_rating(name, rating)
        assert collector.books_rating == {name: rating}

# Нельзя выставить рейтинг книге, которой нет в списке
    def test_set_book_rating_with_invalid_rating_1(self, collector, new_book):
        collector.set_book_rating('Fight Club', 9)
        assert collector.books_rating == {"The Great Gatsby": 1}

# Нельзя выставить рейтинг больше 10.
    def test_set_book_rating_with_invalid_rating_2(self, collector, new_book):
        collector.set_book_rating("The Great Gatsby", 11)
        assert collector.books_rating == {"The Great Gatsby": 1}

# Нельзя выставить рейтинг меньше 1
    def test_set_book_rating_with_invalid_rating_3(self, collector, new_book):
        collector.set_book_rating('Of Mice and Men', 0)
        assert collector.books_rating == {"The Great Gatsby": 1}

# Проверка получения рейтинга книги по ее имени
    def test_get_book_rating(self, collector, new_book):
        collector.set_book_rating("The Great Gatsby", 8)
        assert collector.get_book_rating("The Great Gatsby") == 8

# Проверка вывода списка книг с определенным рейтингом

    def test_get_books_with_specific_rating(self, collector, new_books, set_new_books):
        assert collector.get_books_with_specific_rating(8) == ['Idiot', 'Three Comrades']

    def test_get_books_with_specific_rating_2(self, collector, new_books, set_new_books):
        assert collector.get_books_with_specific_rating(7) == ["The Great Gatsby",'Fight Club','Of Mice and Men']

    def test_get_books_with_specific_rating_3(self, collector, new_books, set_new_books):
        assert collector.get_books_with_specific_rating(3) == []

# Проверка получения словаря books_rating
    @pytest.mark.parametrize('name, rating',[["The Great Gatsby",7],["To Kill a Mockingbird",6],['Fight Club',7],['Idiot',9],['Three Comrades',8],['Of Mice and Men',7]])
    def test_get_books_rating(self, collector, name, rating):
        collector.add_new_book(name)
        collector.set_book_rating(name, rating)
        assert collector.get_books_rating() == {name: rating}

# Проверка добавления книги в избранное
    def test_add_book_in_favorites(self, collector, add_to_favorite):
        assert collector.get_list_of_favorites_books() == ["The Great Gatsby"]

# Нельзя добавить книгу в избранное, если её нет в словаре books_rating
    def test_add_book_in_favorites_negative(self, collector, new_book_2):
        collector.set_book_rating("To Kill a Mockingbird", 7)
        collector.add_book_in_favorites("The Great Gatsby")
        assert collector.get_list_of_favorites_books() == []

# Проверка удаления книги из избранного
    def test_delete_book_from_favorites(self, collector, new_book):
        collector.delete_book_from_favorites("The Great Gatsby")
        assert collector.get_list_of_favorites_books() == []

# Проверка получения списка Избранных книг
    def test_get_list_of_favorites_books(self, collector,new_books,favorite_books):
        assert collector.get_list_of_favorites_books() == ["The Great Gatsby",'To Kill a Mockingbird','Fight Club','Idiot','Three Comrades','Of Mice and Men']

