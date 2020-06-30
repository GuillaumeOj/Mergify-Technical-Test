from warehouse.stock import Stock


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
