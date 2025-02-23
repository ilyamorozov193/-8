class Car:
    """
    Базовый класс, представляющий автомобиль.
    """

    def __init__(self, brand: str, model: str, year: int, fuel_type: str):
        """
        Конструктор базового класса Car.

        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска.
        :param fuel_type: Тип топлива.
        """
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel_type = fuel_type

    def __str__(self) -> str:
        """
        Возвращает строковое представление автомобиля.
        """
        return f"{self.brand} {self.model} ({self.year}), топливо: {self.fuel_type}"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление автомобиля.
        """
        return f"Car(brand={self.brand}, model={self.model}, year={self.year}, fuel_type={self.fuel_type})"

    def start_engine(self) -> str:
        """
        Запускает двигатель автомобиля.

        :return: Сообщение о запуске двигателя.
        """
        return f"Двигатель {self.brand} {self.model} запущен."


class PassengerCar(Car):
    """
    Дочерний класс, представляющий легковой автомобиль.
    """

    def __init__(self, brand: str, model: str, year: int, fuel_type: str, num_seats: int):
        """
        Конструктор класса PassengerCar.

        :param num_seats: Количество пассажирских мест.
        """
        super().__init__(brand, model, year, fuel_type)
        self.num_seats = num_seats

    def __str__(self) -> str:
        """
        Возвращает строковое представление легкового автомобиля.
        """
        return f"{super().__str__()}, мест: {self.num_seats}"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление легкового автомобиля.
        """
        return f"PassengerCar(brand={self.brand}, model={self.model}, year={self.year}, fuel_type={self.fuel_type}, num_seats={self.num_seats})"

    def start_engine(self) -> str:
        """
        Перегруженный метод запуска двигателя для легкового автомобиля.

        :return: Сообщение о запуске двигателя.
        """
        return f"Двигатель легкового автомобиля {self.brand} {self.model} запущен."


class Truck(Car):
    """
    Дочерний класс, представляющий грузовой автомобиль.
    """

    def __init__(self, brand: str, model: str, year: int, fuel_type: str, max_load: int):
        """
        Конструктор класса Truck.

        :param max_load: Максимальная грузоподъёмность (в тоннах).
        """
        super().__init__(brand, model, year, fuel_type)
        self.max_load = max_load

    def __str__(self) -> str:
        """
        Возвращает строковое представление грузового автомобиля.
        """
        return f"{super().__str__()}, грузоподъёмность: {self.max_load} тонн"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление грузового автомобиля.
        """
        return f"Truck(brand={self.brand}, model={self.model}, year={self.year}, fuel_type={self.fuel_type}, max_load={self.max_load})"

    def start_engine(self) -> str:
        """
        Перегруженный метод запуска двигателя для грузового автомобиля.

        :return: Сообщение о запуске двигателя.
        """
        return f"Двигатель грузового автомобиля {self.brand} {self.model} запущен."


# Пример использования
if __name__ == "__main__":
    # Создаём объекты
    car = Car("Toyota", "Corolla", 2020, "бензин")
    passenger_car = PassengerCar("Honda", "Civic", 2019, "бензин", 5)
    truck = Truck("Volvo", "FH16", 2018, "дизель", 20)

    # Выводим информацию
    print(car)
    print(passenger_car)
    print(truck)

    # Запускаем двигатели
    print(car.start_engine())
    print(passenger_car.start_engine())
    print(truck.start_engine())