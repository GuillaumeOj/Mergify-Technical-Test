from warehouse.box import Box
from warehouse.stock import Stock


class TestBox:
    def test_box_has_no_double_and_no_triple_letters(self):
        box = Box("abcdef")
        assert not box.has_double
        assert not box.has_triple

    def test_box_has_double_letters_once_and_triple_letters_once(self):
        box = Box("bababc")
        assert box.has_double
        assert box.has_triple

    def test_box_has_double_letters_once_and_no_triple_letters(self):
        box = Box("abbcde")
        assert box.has_double
        assert not box.has_triple

    def test_box_has_no_double_letters_and_triple_letters_once(self):
        box = Box("abcccd")
        assert not box.has_double
        assert box.has_triple

    def test_box_has_double_letters_twice_and_no_triple_letters(self):
        box = Box("aabcdd")
        assert box.has_double
        assert not box.has_triple

    def test_box_has_no_double_letters_and_triple_letters_twice(self):
        box = Box("ababab")
        assert not box.has_double
        assert box.has_triple


class MockStockAddBox:
    def add_box(self, box):
        self._boxes.append(box)


class TestStock:
    def test_stock_has_one_box_with_two_letters(self, monkeypatch):
        monkeypatch.setattr("warehouse.stock.Stock.add_box", MockStockAddBox.add_box)
        stock = Stock()
        stock.add_box(list("abbcde"))
        stock.add_box(list("abcdef"))
        assert stock.two_letters_boxes == 1
        assert stock.three_letters_boxes == 0
        assert stock.checksum == 0

    def test_stock_has_one_box_with_three_letters(self, monkeypatch):
        monkeypatch.setattr("warehouse.stock.Stock.add_box", MockStockAddBox.add_box)
        stock = Stock()
        stock.add_box(list("abcccd"))
        stock.add_box(list("abcdef"))
        assert stock.two_letters_boxes == 0
        assert stock.three_letters_boxes == 1
        assert stock.checksum == 0

    def test_stock_has_one_box_with_two_letters_and_one_box_with_three_letters(
        self, monkeypatch
    ):
        monkeypatch.setattr("warehouse.stock.Stock.add_box", MockStockAddBox.add_box)
        stock = Stock()
        stock.add_box(list("abbcde"))
        stock.add_box(list("abcccd"))
        stock.add_box(list("abcdef"))
        assert stock.two_letters_boxes == 1
        assert stock.three_letters_boxes == 1
        assert stock.checksum == 1

    def test_stock_has_two_boxes_with_two_letters_and_two_boxes_with_three_letters(
        self, monkeypatch
    ):
        monkeypatch.setattr("warehouse.stock.Stock.add_box", MockStockAddBox.add_box)
        stock = Stock()
        stock.add_box(list("abbcde"))
        stock.add_box(list("abccde"))
        stock.add_box(list("abcccd"))
        stock.add_box(list("abeeed"))
        stock.add_box(list("abcdef"))
        assert stock.two_letters_boxes == 2
        assert stock.three_letters_boxes == 2
        assert stock.checksum == 4
