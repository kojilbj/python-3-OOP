from abc import ABC, abstractclassmethod


class Character(ABC):
    """Abstract Class that has name, is_alive as members."""
    first_name: str = ""
    is_alive: bool = True

    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor of Character that initialize name and is_alive"""
        self.first_name = first_name
        self.is_alive = is_alive

    @classmethod
    @abstractclassmethod
    def die(self):
        """This abstract function change is_alive into false"""
        pass


class Stark(Character):
    """This class inherit Character"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor of Stark that pass args to Character's constructor"""
        super().__init__(first_name, is_alive)

    def die(self):
        """This function change is_alive into false"""
        self.is_alive = False
