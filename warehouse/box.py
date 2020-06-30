class Box:
    """
    Represent a box in the warehouse
    """

    def __init__(self, content):
        self.content = list(content)
        self.letters = set(content)
        self.count = {letter: content.count(letter) for letter in self.letters}

    @property
    def has_double(self):
        """
        Return True if the box have two letters at least once
        """
        if 2 in self.count.values():
            return True

    @property
    def has_triple(self):
        """
        Return True if the box have three letters at least once
        """
        if 3 in self.count.values():
            return True
