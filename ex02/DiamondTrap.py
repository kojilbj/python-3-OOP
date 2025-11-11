from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """False King"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor"""
        super().__init__(first_name, is_alive)

    def set_hairs(self, hairs: str):
        """This function set hairs attribute."""
        self.hairs = hairs

    def set_eyes(self, eyes: str):
        """This function set eyes attribute."""
        self.eyes = eyes

    def get_hairs(self):
        """This function return hairs attribute."""
        return self.hairs

    def get_eyes(self):
        """This function return eyes attribute."""
        return self.eyes
