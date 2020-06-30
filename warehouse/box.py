class Box:
    """
    Represent a box in the warehouse
    """

    def __init__(self, box_id):
        self.box_id = list(box_id)
        self.letters = set(box_id)
        self.count = {letter: box_id.count(letter) for letter in self.letters}

    @property
    def has_double(self):
        """
        Return True if the box_id have two letters at least once
        """
        if 2 in self.count.values():
            return True
        return False

    @property
    def has_triple(self):
        """
        Return True if the box_id have three letters at least once
        """
        if 3 in self.count.values():
            return True
        return False
