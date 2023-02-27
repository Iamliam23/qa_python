import pytest
from main import BooksCollector

@pytest.fixture
def collector(scope='class'):
    return BooksCollector()

@pytest.fixture(scope='function')
def new_book(collector):
    collector.add_new_book("The Great Gatsby")

@pytest.fixture(scope='function')
def new_book_2(collector):
    collector.add_new_book('To Kill a Mockingbird')

@pytest.fixture(scope='function')
def new_books(collector):
    collector.add_new_book("The Great Gatsby")
    collector.add_new_book('To Kill a Mockingbird')
    collector.add_new_book('Fight Club')
    collector.add_new_book('Idiot')
    collector.add_new_book('Three Comrades')
    collector.add_new_book('Of Mice and Men')
    return collector.books_rating
@pytest.fixture(scope='function')
def set_new_books(collector):
    collector.set_book_rating("The Great Gatsby",7)
    collector.set_book_rating('To Kill a Mockingbird',6)
    collector.set_book_rating('Fight Club',7)
    collector.set_book_rating('Idiot',8)
    collector.set_book_rating('Three Comrades',8)
    collector.set_book_rating('Of Mice and Men', 7)
    return collector.get_books_rating()

@pytest.fixture(scope='function')
def add_to_favorite(collector):
    collector.add_new_book("The Great Gatsby")
    collector.add_book_in_favorites("The Great Gatsby")

@pytest.fixture(scope='function')
def favorite_books(collector):
    collector.add_book_in_favorites('The Great Gatsby')
    collector.add_book_in_favorites('To Kill a Mockingbird')
    collector.add_book_in_favorites('Fight Club')
    collector.add_book_in_favorites('Idiot')
    collector.add_book_in_favorites('Three Comrades')
    collector.add_book_in_favorites('Of Mice and Men')








