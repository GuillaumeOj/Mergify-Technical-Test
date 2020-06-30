import os

from warehouse.box import Box
from warehouse.stock import Stock
from warehouse.finder import Finder

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class App:
    """
    Main application
    """

    def __init__(self):
        self.input_boxes = list()
        self.boxes = list()
        self.stock = None

    def open_file(self):
        """
        Read the input file content
        """
        file_path = os.path.join(BASE_DIR, "src", "input.txt")
        with open(file_path, "r") as f:
            self.input_boxes = f.read().splitlines()

    def read_boxes(self):
        """
        Read the boxes content
        """
        self.boxes = list()

        for input_box in self.input_boxes:
            self.boxes.append(Box(input_box))

    def store_boxes(self):
        """
        Store the boxes in the warehouse
        """
        self.stock = Stock(self.boxes)

    @property
    def stock_checksum(self):
        """
        Read the list checksum
        """
        return self.stock.checksum

    @property
    def common_letters_between_correct_boxes(self):
        """
        Find the two correct boxes and return the common letters between their ID
        """
        boxes_to_compare = list(self.boxes)
        boxes_common_letters = str()
        finder = Finder()

        for box1 in self.boxes:
            for box2 in boxes_to_compare:
                if finder.compare_boxes(box1, box2):
                    # find common letters between the two correct boxes
                    boxes_common_letters = finder.common_letters(box1, box2)
                    break
            if boxes_common_letters:
                break

        return boxes_common_letters


if __name__ == "__main__":
    app = App()
    app.open_file()
    app.read_boxes()
    app.store_boxes()
    print(f"Answer for Part I  📝 {app.stock_checksum}")
    print(f"Answer for Part II 📦 {app.common_letters_between_correct_boxes}")
