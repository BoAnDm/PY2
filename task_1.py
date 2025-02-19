from typing import Union


class Conifers:
    """Базовый класс хвойные деревья"""
    def __init__(self, average_height: Union[int, float], quantity:int):
        """Инициализация экземпляра класса с валидацией всех аргументов.
        :param average_height: Средняя высота деревьев.
        :param quantity: Количество деревьев.

        Example:
        >>> сonifers_1 = Conifers (200, 1) # корректный пример
        >>> сonifers_2 = Conifers (-200, 2) # некорректный пример
        Traceback (most recent call last):
        ...
        ValueError: Значение средней высоты деревьев не может быть отрицательным
        >>> сonifers_3 = Conifers (0, 2) # некорректный пример
        Traceback (most recent call last):
        ...
        ValueError: Значение средней высоты деревьев не может быть равным 0, если есть деревья
        >>> сonifers_4 = Conifers (10, -2) # некорректный пример
        Traceback (most recent call last):
        ...
        ValueError: Количество деревьев не может быть отрицательным числом
        >>> сonifers_5 = Conifers (10, "2") # некорректный пример
        Traceback (most recent call last):
        ...
        TypeError: Количество деревьев должно быть типа int"""
        if not isinstance(average_height, (int, float)):  # проверка типа
            raise TypeError("Значение средней высоты деревьев должно быть типа int или float")
        if average_height < 0:  # проверка значения
            raise ValueError("Значение средней высоты деревьев не может быть отрицательным")
        if quantity != 0 and average_height == 0:
            raise ValueError("Значение средней высоты деревьев не может быть равным 0, если есть деревья")
        self.average_height = average_height

        if not isinstance(quantity, int):
            raise TypeError("Количество деревьев должно быть типа int")
        if quantity < 0:
            raise ValueError("Количество деревьев не может быть отрицательным числом")
        self.quantity = quantity

    def purchase(self, required_quantity:int):
        """Метод для определения необходимости закупки. Если закупка нужна, то определяет
        сколько деревьев необходимо закупить.
        В начале проверяет входное значение.
        :param required_quantity: Нужное нам количество деревьев.

        Example:
        >>> сonifers_6 = Conifers(35.6, 21)
        >>> сonifers_6.purchase(-100)  # некорректный пример
        Traceback (most recent call last):
        ...
        ValueError: Значение необходимого количества деревьев не может быть отрицательным числом
        >>> сonifers_6.purchase('100')  # некорректный пример
        Traceback (most recent call last):
        ...
        TypeError: Значение необходимого количества деревьев должно быть типа int
        """
        if not isinstance(required_quantity, int):  # проверка типа
            raise TypeError("Значение необходимого количества деревьев должно быть типа int")
        if required_quantity < 0:  # проверка значения
            raise ValueError("Значение необходимого количества деревьев не может быть отрицательным числом")
        counting = required_quantity - self.quantity
        if counting <= 0:
            print('На складе достаточно деревьев')
        else:
            print(f'Необходимо докупить {counting} деревьев.')

    def addition(self, add_quantity:int, add_average_height: Union[int, float]):
        """Метод для добавления деревьев к уже существующему количеству.
        Так же этот метод меняет среднюю высоту деревьев.
        :param add_quantity: Количество добавляемых деревьев.
        :param add_average_height: Средняя высота добавляемых деревьев.
        Проводим проверку вводимых значений.
        Example:
        >>> сonifers_7 = Conifers(53.67, 73)
        >>> сonifers_7.addition("2", 100) # некорректный пример
        Traceback (most recent call last):
        ...
        TypeError: Значение добавляемого количества деревьев должно быть типа int
        >>> сonifers_7.addition(0, 32) # добавляем 0 деревьев
        Traceback (most recent call last):
        ...
        ValueError: Нет деревьев, которые нужно добавить или забрать
        >>> сonifers_7.addition(2, 0) # некорректный пример т.к. высота добавляемых деревьев = 0
        Traceback (most recent call last):
        ...
        ValueError: Значение средней высоты добавляемых деревьев не может быть равным 0, если есть деревья

        Проверку на значение количества деревьев не проводим т.к. данный метод предполагает, что мы можем не только
        добавлять деревья на склад, но и забирать их оттуда.
        """
        if not isinstance(add_quantity, int):  # проверка типа
            raise TypeError("Значение добавляемого количества деревьев должно быть типа int")
        if not isinstance(add_average_height, (int, float)):  # проверка типа
            raise TypeError("Значение высоты добавляемых деревьев должно быть типа int или float")
        if add_quantity == 0:
            raise ValueError("Нет деревьев, которые нужно добавить или забрать")
        if add_average_height < 0:  # проверка значения
            raise ValueError("Значение средней высоты добавляемых деревьев не может быть отрицательным")
        if add_quantity != 0 and add_average_height == 0:
            raise ValueError("Значение средней высоты добавляемых деревьев не может быть равным 0, если есть деревья")

        if add_quantity >= 0:
            add_height = add_average_height * add_quantity  # Подсчитываем сумму высот всех добавляемых деревьев
        else:
            add_height = add_average_height * (-add_quantity)
        height = self.average_height * self.quantity  # Подсчитываем сумму высот всех уже имеющихся деревьев
        self.quantity += add_quantity  # Меняем количество деревьев в наличии
        self.average_height = (add_height+height)/self.quantity  # Подсчитываем нынешнюю среднюю высоту деревьев
        print(f'Количество деревьев: {self.quantity}, Средняя высота деревьев: {self.average_height:.2f}')

    def __str__(self):
        return f"Хвойные деревья со средней высотой {self.average_height}. Количество {self.quantity}"

    def __repr__(self):
        return f"{self.__class__.__name__}(average_height={self.average_height!r}, quantity={self.quantity!r})"


class Fir(Conifers):
    """Дочерний класс ель"""
    def __init__(self, average_height, quantity):
        super().__init__(average_height=average_height, quantity=quantity)

    def __str__(self):
        return f"Ель со средней высотой {self.average_height}. Количество {self.quantity}"


class Pine(Conifers):
     """Дочерний класс сосна"""
     def __init__(self, average_height, quantity):
         super().__init__(average_height=average_height, quantity=quantity)


     def __str__(self):
         return f"Сосна со средней высотой {self.average_height}. Количество {self.quantity}"


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print("Примеры работы некоторых методов:", "", sep = '\n')

    print("1. Метод для определения необходимости закупки.")
    pine1 = Pine (32.5, 20)
    required_quantity_ = 100
    print(f'У нас есть {pine1.quantity} деревьев. А нам нужно {required_quantity_} деревьев...')
    pine1.purchase(required_quantity_)
    print()

    print("2. Метод для добавления или удаления деревьев со склада.")
    fir1=Fir(45.6, 100)
    print(f'У нас есть {fir1.quantity} деревьев, средняя высота которых {fir1.average_height} метра.')
    add_quantity_1=31
    add_height_1=43.6
    print(f'Мы добавили на склад {add_quantity_1} деревьев, средняя высота которых {add_height_1} метра.')
    print('Теперь на складе...')
    fir1.addition(add_quantity_1, add_height_1)
    print()




    pass