class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author = author

    def __str__(self):
        return f"Книга {self.__name}. Автор {self.__author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r})"


class PaperBook(Book):
    def __init__(self, name, author, pages:int):
        super().__init__(name=name, author=author)
        if pages < 0:
            raise ValueError("Количество страниц не может быть отрицательным")
        if not isinstance(pages, int):
            raise TypeError("Атрибут pages должен быть типа int")
        self.pages = pages


class AudioBook(Book):
    def __init__(self, name, author, duration: float):
        super().__init__(name=name, author=author)
        if duration < 0:
            raise ValueError("Продолжительность аудио не может быть отрицательным")
        if not isinstance(duration, float):
            raise TypeError("Атрибут duration должен быть типа float")
        self.duration = duration


if __name__ == '__main__':
    book = Book('book_name', 'book_author1')
    paper_book = PaperBook('paper_book_name', 'paper_book_author', 3)
    audio_book = AudioBook('audio_book_name', 'audio_book_author', 3.14)
    print(book.__str__(), book.__repr__(), '', sep = '\n')
    print(paper_book.__str__(), paper_book.__repr__(), '', sep = '\n')
    print(audio_book.__str__(), audio_book.__repr__(), '', sep = '\n')
    '''Получаем:
    Книга book_name. Автор book_author1
    Book(name='book_name', author='book_author1')

    Книга paper_book_name. Автор paper_book_author 
    PaperBook(name='paper_book_name', author='paper_book_author')

    Книга audio_book_name. Автор audio_book_author
    AudioBook(name='audio_book_name', author='audio_book_author')'''
