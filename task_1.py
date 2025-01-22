from typing import Union

class Bottle:
    """ Документация на класс. Класс описывает модель бутылки. """
    def __init__(self, quantity: int, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        """
        Инициализация экземпляра класса с валидацией всех аргументов.
        :param quantity: количество бутылок
        :param capacity_volume: объем одной бутылки
        :param occupied_volume: объем жидкости в одной бутылке
        Example:
        >>> bottle_ = Bottle (1, 200, 100)  # корректный пример
        >>> bottle_1 = Bottle (1, 200, 300)  # некорректный пример
        Traceback (most recent call last):
        ...
        ValueError: Объем жидкости в бутылке должен быть меньше или равен объему бутылки
        >>> bottle_1 = Bottle (0, 200, 100)  # некорректный пример
        Traceback (most recent call last):
        ...
        ValueError: Нет бутылок, которым можно задать объем
        >>> bottle_1 = Bottle ("1", 200, 100)  # некорректный пример
        Traceback (most recent call last):
        ...
        TypeError: Значение количества бутылок должно быть типа int
        """
        if not isinstance(quantity, int): # количество бутылок
            raise TypeError("Значение количества бутылок должно быть типа int")
        if quantity < 0:
            raise ValueError("Значение количества бутылок должно быть положительным числом")
        self.quantity = quantity

        if not isinstance(capacity_volume, (int, float)):  # объем одной бутылки
            raise TypeError("Объем бутылки должен быть типа int, float")
        if capacity_volume < 0:
            raise ValueError("Объем бутылки должен быть положительным числом")
        if quantity <= 0:
            raise ValueError("Нет бутылок, которым можно задать объем")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):  # объем жидкости в одной бутылке
            raise TypeError("Объем жидкости в бутылке должен быть типа int, float")
        if occupied_volume < 0:
            raise ValueError("Объем жидкости в бутылке должен быть положительным числом")
        if self.capacity_volume <= 0:
            raise ValueError("У бутылки нет объема")
        if occupied_volume > self.capacity_volume:
            raise ValueError("Объем жидкости в бутылке должен быть меньше или равен объему бутылки")
        self.occupied_volume = occupied_volume

    def increment_water_in_bottle (self, additional_liquid: Union[int, float]):
        """
        Метод доливает жидкость в бутылку.

        Зачем? У нас есть бутылка с жидкостью, например с соком, и дополнительная жидкость, например оставшийся сок из вскрытого пакета с соком.
        Мы хотим оставшийся сок перелить в бутылку. Для этого нам сначала нужно определить если там свободное место.

        :param additional_liquid: объем жидкости, которую мы хотим долить в бутылку.
        :raise TypeError: Если additional_liquid не int или float.
        :raise ValueError: Если additional_liquid отрицательный или превышает оставшийся объем.
        :return: добавляет к нынешнему количеству жидкости в бутылке дополнительную жидкость

        Example:
        >>> b = Bottle (2, 200, 100)
        >>> b.increment_water_in_bottle(100)  # корректный пример
        >>> b.increment_water_in_bottle(200)  # некорректный пример
        Traceback (most recent call last):
        ...
        ValueError: объем жидкости, которую мы хотим долить в бутылку должен быть меньше или равен оставшемуся в бутылке объему
        >>> b.increment_water_in_bottle("100")  # некорректный пример
        Traceback (most recent call last):
        ...
        TypeError: объем жидкости, которую мы хотим долить в бутылку должен быть типа int или float
        >>> b.increment_water_in_bottle(-100)  # некорректный пример
        Traceback (most recent call last):
        ...
        ValueError: объем жидкости, которую мы хотим долить в бутылку должен быть положительным числом
        """

        if not isinstance(additional_liquid, (int, float)):
            raise TypeError("объем жидкости, которую мы хотим долить в бутылку должен быть типа int или float")

        if additional_liquid < 0:
            raise ValueError("объем жидкости, которую мы хотим долить в бутылку должен быть положительным числом")

        if additional_liquid > self.capacity_volume - self.occupied_volume:
            raise ValueError("объем жидкости, которую мы хотим долить в бутылку должен быть меньше или равен оставшемуся в бутылке объему")
        # И только после всех проверок:
        self.occupied_volume += additional_liquid  # добавляем жидкость в бутылку

    def number_of_bottles_per_person (self, number_of_people: int):
        """
        У нас есть некоторое количество бутылок и людей.
        Нам нужно определить сколько бутылок сможет получить каждый человек в группе.
        Если кому-то не хватает бутылки, то результат будет в виде 0.

        :param number_of_people: количество людей
        :return: количество целых бутылок на одного человека

        Example:
        >>> b = Bottle (100, 500, 450)
        >>> b.number_of_bottles_per_person(5)  # корректный пример
        20
        >>> b.number_of_bottles_per_person("6")  # некорректный пример
        Traceback (most recent call last):
        ...
        TypeError: Количество людей должно быть типа int
        >>> b.number_of_bottles_per_person(-20)  # некорректный пример
        Traceback (most recent call last):
        ...
        ValueError: Количество людей не может быть отрицательным или равным 0
        """
        if not isinstance(number_of_people, int):
            raise TypeError("Количество людей должно быть типа int")

        if number_of_people <= 0:
            raise ValueError("Количество людей не может быть отрицательным или равным 0")

        number_of_bottles = self.quantity // number_of_people
        # после всех проверок
        return number_of_bottles

class People:
    """ Документация на класс. Класс описывает модель людей. """
    def __init__(self, men_number: int, women_number: int, children_number: int):
        """
        Инициализация экземпляра класса с валидацией аргументов. Таже как и в классе "бутылка" проверяем тип и значение аргументов
        :param men_number: количество мужчин
        :param women_number: количество женщин
        :param children_number: количество детей
        Example:
        >>> p_ = People (1, 2, 3)  # корректный пример
        >>> p_ = People (1, "2", 2)  # некорректный пример
        Traceback (most recent call last):
        ...
        TypeError: Значение количества женщин должно быть типом int
        >>> p_ = People (-1, 2, 0)  # некорректный пример
        Traceback (most recent call last):
        ...
        ValueError: Значение количества мужчин должно быть положительным числом
        """
        if not isinstance(men_number, int):  # количество мужчин
            raise TypeError("Значение количества мужчин должно быть типом int")
        if men_number < 0:
            raise ValueError("Значение количества мужчин должно быть положительным числом")
        self.men_number = men_number

        if not isinstance(women_number, int):  # количество женщин
            raise TypeError("Значение количества женщин должно быть типом int")
        if women_number < 0:
            raise ValueError("Значение количества женщин должно быть положительным числом")
        self.women_number = women_number

        if not isinstance(children_number, int):  # количество детей
            raise TypeError("Значение количества детей должно быть типом int")

        if children_number < 0:
            raise ValueError("Значение количества детей должно быть положительным числом")
        self.children_number = children_number

    def the_number_of_people_after_a_while (self, additional_men: int, additional_women: int, additional_children: int):
        """
        Метод добавляет или убирает людей из уже имеющихся.

        Предположим в комнате находится некоторое количество мужчин, женщин и детей. Через время кто-то выходит из помещения, а кто-то заходит.
        Нам нужно узнать сколько людей осталось в помещении.

        :param additional_men: количество пришедших или ушедших мужчин.
        :param additional_women: количество пришедших или ушедших женщиин.
        :param additional_children: количество пришедших или ушедших детей.
        :return: добавляет к изначальному количеству людей в помещении количество пришедших или ушедших людей.

        Example:
        >>> p = People (1, 2, 1)
        >>> p.the_number_of_people_after_a_while(3, 1, -1)  # корректный пример
        >>> p.the_number_of_people_after_a_while(3, "1", -1)  # некорректный пример
        Traceback (most recent call last):
        ...
        TypeError: Количество пришедших или ушедших женщин должно быть типом int
        >>> p.the_number_of_people_after_a_while(3, 1, -2)  # некорректный пример
        Traceback (most recent call last):
        ...
        ValueError: Ушедших людей должно быть меньше или столько же, сколько находящихся в помещении
        """
        if not isinstance(additional_men, int):
            raise TypeError("Количество пришедших или ушедших мужчин должно быть типом int")

        if not isinstance(additional_women, int):
            raise TypeError("Количество пришедших или ушедших женщин должно быть типом int")

        if not isinstance(additional_children, int):
            raise TypeError("Количество пришедших или ушедших детей должно быть типом int")

        if self.men_number + additional_men < 0 or self.women_number + additional_women < 0 or self.children_number + additional_children < 0:
            raise ValueError("Ушедших людей должно быть меньше или столько же, сколько находящихся в помещении")
        # После всех проверок
        self.men_number = self.men_number + additional_men
        self.women_number = self.women_number + additional_women
        self.children_number = self.children_number + additional_children

    def counting_the_total_number_of_people(self):
        """
        Метод подсчитывает общеее количество людей.
        Мы знаем сколько в некотором месте мужчин, женщин и детей. Но сколько людей всего?
        А если кто-то пришел или ушел? Сколько теперь людей?

        :total_number_of_people: общее количество людей
        :return: возвращает total_number_of_people - общее количество людей, находящихся в каком-либо месте

        Example:
        >>> p_ = People (2, 1, 0)
        >>> p_.counting_the_total_number_of_people()
        3
        >>> p_.the_number_of_people_after_a_while(-1, 5, 3)
        >>> p_.counting_the_total_number_of_people()
        10
        """
        total_number_of_people = self.men_number + self.women_number + self.children_number
        if not isinstance(total_number_of_people, int):
            raise TypeError("Общее количество людей должно быть типа int")

        if total_number_of_people < 0:
            raise ValueError("общее количество людей не может быть отрицательным")
        # И только после проверок
        return total_number_of_people  # общее количество людей

class Copybook:
    """ Документация на класс. Класс описывает модель тетради. """
    def __init__(self, color_of_copybooks: str, number_of_copybooks: int, number_of_pages: int):
        """
        Инициализация экземпляра класса с валидацией аргументов.
        :param color_of_copybooks: цвет тетрадей
        :param number_of_copybooks: количество тетрадей
        :param number_of_pages: количество страниц в одной тетради

        Example:
        >>> c = Copybook ("green", 2, 60)  # корректный пример
        >>> c = Copybook (3, 2, 60)  # некорректный пример
        Traceback (most recent call last):
        ...
        TypeError: Цвет тетрадей должен быть типа str
        >>> c = Copybook ("black", -1, 60)  # некорректный пример
        Traceback (most recent call last):
        ...
        ValueError: Количество тетрадей должно быть положительным числом или равным нулю
        >>> c = Copybook ("black", 0, 60)  # некорректный пример
        Traceback (most recent call last):
        ...
        ValueError: Тетрадей нет, значит и страниц быть не должно
        """
        if not isinstance(color_of_copybooks, str):
            raise TypeError("Цвет тетрадей должен быть типа str")

        if not isinstance(number_of_copybooks, int):
            raise TypeError("Количество тетрадей должно быть типа int")
        if number_of_copybooks < 0:
            raise ValueError("Количество тетрадей должно быть положительным числом или равным нулю")
        self.number_of_copybooks = number_of_copybooks  # количество тетрадей

        if not isinstance(number_of_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if number_of_pages < 0:
            raise ValueError("Количество страниц должно быть положительным числом или равным 0")
        if number_of_copybooks == 0:
            if number_of_pages > 0:
                raise ValueError("Тетрадей нет, значит и страниц быть не должно")
        self.number_of_pages = number_of_pages  # количество страниц

    def ripping_out_pages (self, number_of_pages_to_extract: int):
        """
        Метод для определения количества оставшихся в тетради страниц после вырывания оттуда нескольких.
        Представим что мы пришли на контрольную и нам нужен чистый листик, и даже не один.

        :param number_of_pages_to_extract: количество вырываемых страниц
        :return: удаляет из аргумента "количество страниц" количество вырываемых страниц

        Example:
        >>> c = Copybook ("red", 1, 34)
        >>> c.ripping_out_pages(23)  # корректный пример
        >>> c.ripping_out_pages(35)  # некорректный пример
        Traceback (most recent call last):
        ...
        ValueError: Количество вырываемых страниц должно быть меньше или равно количеству страниц в тетради
        >>> c.ripping_out_pages("2")  # некорректный пример
        Traceback (most recent call last):
        ...
        TypeError: Количество вырываемых страниц должно быть типа int
        >>> c.ripping_out_pages(-14)  # некорректный пример
        Traceback (most recent call last):
        ...
        ValueError: Количество вырываемых страниц должно быть положительным числом или равным 0
        """

        if not isinstance(number_of_pages_to_extract, int):
            raise TypeError("Количество вырываемых страниц должно быть типа int")
        if number_of_pages_to_extract < 0:
            raise ValueError("Количество вырываемых страниц должно быть положительным числом или равным 0")
        if number_of_pages_to_extract > self.number_of_pages:
            raise ValueError("Количество вырываемых страниц должно быть меньше или равно количеству страниц в тетради")
        # И только после проверок
        self.number_of_pages -= number_of_pages_to_extract

    def buying_copybooks (self, required_number_of_copybooks: int):
        """
        Метод, помогающий определить сколько тетрадей необходимо докупить.

        :param required_number_of_copybooks: необходимое количество тетрадей
        :required_buy: Необходимо купить n тетрадей
        :return: возвращает required_buy

        Example:
        >>> c = Copybook ("yellow", 3, 36)
        >>> c.buying_copybooks(15)  # корректный пример
        12
        >>> c.buying_copybooks("15")  # некорректный пример
        Traceback (most recent call last):
        ...
        TypeError: Значение необходимого количества тетрадей должно быть типа int
        >>> c.buying_copybooks(-2)  # некорректный пример
        Traceback (most recent call last):
        ...
        ValueError: Значение необходимого количества тетрадей должно быть положительным числом или равно 0
        """
        if not isinstance(required_number_of_copybooks, int):
            raise TypeError("Значение необходимого количества тетрадей должно быть типа int")
        if required_number_of_copybooks < 0:
            raise ValueError("Значение необходимого количества тетрадей должно быть положительным числом или равно 0")

        if self.number_of_copybooks < required_number_of_copybooks:
            required_buy = required_number_of_copybooks - self.number_of_copybooks
        else:
            required_buy = 0
        return  required_buy


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print("Примеры работы некоторых методов:")
    print()

    print("1. Метод, доливающий жидкость в бутылку:")
    bottle1 = Bottle(1, 200, 100)
    print(f'количество бутылок: {bottle1.quantity}, объем одной бутылки в мл: {bottle1.capacity_volume}, количество жидкости в бутылке в мл {bottle1.occupied_volume}.')
    liquid_volume = 100
    print(f'Доливаем в бутылку {liquid_volume} мл жидкости...')
    bottle1.increment_water_in_bottle(liquid_volume)
    print(f'Теперь в бутылке {bottle1.occupied_volume} мл воды.')
    print()

    print("2. Метод, подсчитывающий общеее количество людей:")
    people1 = People (45, 20, 34)
    print(f'В помещении было {people1.men_number} мужчин, {people1.women_number} женщин и {people1.children_number} детей.'
          f' Итого было {people1.counting_the_total_number_of_people()} людей')
    people1.the_number_of_people_after_a_while(-1, 5, 3)
    print(f'За некоторое время в помещении поменялось количество людей. Кто-то вышел, кто-то зашел.')
    print(f'Теперь в помещении {people1.men_number} мужчин, {people1.women_number} женщин и {people1.children_number} детей. '
          f'Всего {people1.counting_the_total_number_of_people()} человек.')
    print()

    print("3. Метод для определения оставшихся после вырывания страниц в тетради:")
    copybook1 = Copybook ("orange", 1, 36)
    print(f'В тетради было {copybook1.number_of_pages} страниц.')
    number_of_pages_to_extract = 10
    copybook1.ripping_out_pages(number_of_pages_to_extract)
    print(f'Мы вырвали из тетради {number_of_pages_to_extract} страниц. Теперь в тетради {copybook1.number_of_pages} страниц.')
    print()

    print("Также можно попробовать использовать метод с задаваемым нами значением.")
    print("Выполним метод, определяющий сколько тетрадей нам необходимо докупить")
    print("Введите количество тетрадей, которые у вас есть в виде целого числа. Примеры: 3, 10")
    number_of_copybooks = input()
    try:
        number_of_copybooks = int(number_of_copybooks)
    except ValueError:
        print("Error: Введенное вами значение не является целым числом")
    else:
        copybook2 = Copybook("red", number_of_copybooks, 36)
        print("Теперь введите необходимое вам количество тетрадей в виде числа:")
        need_copybook = input()
        try:
            need_copybook = int(need_copybook)
        except ValueError:
            print("Error: Введенное вами значение не является целым числом")
        else:
            print(f'Вам нужно докупить {copybook2.buying_copybooks(need_copybook)} тетрадей.')