import os

from warehouse.box import Box
from warehouse.stock import Stock

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class App:
    """
    Main application
    """

    def __init__(self):
        self.input_boxes = list()
        self.boxes = list()
        self.stock = Stock()

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
        for box in self.boxes:
            self.stock.add_box(box)

    @property
    def stock_checksum(self):
        """
        Read the list checksum
        """
        return self.stock.checksum


if __name__ == "__main__":
    app = App()
    app.open_file()
    app.read_boxes()
    app.store_boxes()
    print(app.stock_checksum)
