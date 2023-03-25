from abc import ABC, abstractmethod


class Storage(ABC):
    """
    Абстрактный класс хранилища
    """
    @property
    @abstractmethod
    def items(self):
        """
        Предметы
        """
        pass

    @property
    @abstractmethod
    def capacity(self):
        """
        Вместительность
        """
        pass

    @abstractmethod
    def add(self, name, qnt):
        """
        Метод для добавления предметов в хранилище
        """
        pass

    @abstractmethod
    def remove(self, name, qnt):
        """
        Метод для забора предметов из хранилища
        """
        pass

    @abstractmethod
    def _get_free_space(self):
        """
        Метод для получения свободного места
        """
        pass

    @abstractmethod
    def get_items(self):
        """
        Метод для получения содержимого хранилища
        """
        pass

    @abstractmethod
    def _get_unique_items_count(self):
        """
        Метод для получения количества уникальных товаров
        """
        pass
    