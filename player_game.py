from random import randint


class Player:
    """
    make a new player
    """

    def __init__(self, x: int, y: int)-> None:
        """
        initialize new player
        """
        self.wins = 0
        self.x = x
        self.y = y
        self.dead = False
        self.colour = (randint(0, 250), randint(0, 250), randint(0 , 250))


class AI:
    """
    make a new ai computer
    """

    def __init__(self, x: int, y: int)-> None:
        """
        initialize new player
        """
        self.x = x
        self.y = y
        self.colour = (randint(0, 250), randint(0, 250), randint(0, 250))


class Fire:

    def __init__(self, x: int, y: int, speed: int) -> None:
        """
        initialize a new fire ball
        """
        self.x = x
        self.y = y
        self.speed = speed
