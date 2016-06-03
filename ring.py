# This is ring.py
from genericobject import GenericObject

"""

State:
    emoji:  💍
    ability: kill spiders

"""


class Ring(GenericObject):
    """Blueprint for a ring in the Dungeon of Doom!

    Extends GenericObject
    """

    def __init__(self, description):
        """Initialize"""
        super().__init__(description)
        self.i_am_a = 'ring'
        self.emoji = '💍'

    def __repr__(self):
        return """ring(description={self.description}, i_am_a={self.i_am_a}, emoji={self.emoji}""".format(self=self)

if __name__ == '__main__':
    from doctest import testmod

    testmod()
