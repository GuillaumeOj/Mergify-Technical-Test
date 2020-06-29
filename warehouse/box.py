class Box:
    def __init__(self, content):
        self.content = list(content)
        self.letters = set(content)
        self.count = {letter: content.count(letter) for letter in self.letters}

    @property
    def has_double(self):
        if 2 in self.count.values():
            return True

    @property
    def has_triple(self):
        if 3 in self.count.values():
            return True
