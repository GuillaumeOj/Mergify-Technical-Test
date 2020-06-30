class Stock:
    """
    Represent the warehouse
    """

    def __init__(self, boxes):
        self._boxes = boxes

    @property
    def two_letters_boxes(self):
        """
        Count boxes with two letters inside
        """
        return self._count_boxes(2)

    @property
    def three_letters_boxes(self):
        """
        Count boxes with three letters inside
        """
        return self._count_boxes(3)

    @property
    def checksum(self):
        return self.two_letters_boxes * self.three_letters_boxes

    def _count_boxes(self, letters_number):
        """
        Count boxes with letters_number inside
        """
        boxes_number = 0
        for box in self._boxes:
            if (letters_number == 2 and box.has_double) or (
                letters_number == 3 and box.has_triple
            ):
                boxes_number += 1

        return boxes_number
