# Christerpher Hunter
# Lab 08: Pick6


from random import randint


class Pick6:
    """Generate and pick winners at random"""

    def __init__(self, ticket: list) -> None:

        self.ticket = ticket

    def pick6(self) -> list:
        """Generate 6 random numbers"""

        

