from warehouse.stock import Stock


class MockStockAddBox:
    def add_box(self, boxes):
        self._boxes = boxes


class TestStock:
    def test_stock_has_one_box_with_two_letters(self, monkeypatch):
        monkeypatch.setattr("warehouse.stock.Stock.add_box", MockStockAddBox.add_box)
        stock = Stock()
        stock.add_box([list("abbcde"), list("abcdef")])
        assert stock.two_letters_boxes == 1
        assert stock.three_letters_boxes == 0
        assert stock.checksum == 0

    def test_stock_has_one_box_with_three_letters(self, monkeypatch):
        monkeypatch.setattr("warehouse.stock.Stock.add_box", MockStockAddBox.add_box)
        stock = Stock()
        stock.add_box([list("abcccd"), list("abcdef")])
        assert stock.two_letters_boxes == 0
        assert stock.three_letters_boxes == 1
        assert stock.checksum == 0

    def test_stock_has_one_box_with_two_letters_and_one_box_with_three_letters(
        self, monkeypatch
    ):
        monkeypatch.setattr("warehouse.stock.Stock.add_box", MockStockAddBox.add_box)
        stock = Stock()
        stock.add_box([list("abbcde"), list("abcccd"), list("abcdef")])
        assert stock.two_letters_boxes == 1
        assert stock.three_letters_boxes == 1
        assert stock.checksum == 1

    def test_stock_has_two_boxes_with_two_letters_and_two_boxes_with_three_letters(
        self, monkeypatch
    ):
        monkeypatch.setattr("warehouse.stock.Stock.add_box", MockStockAddBox.add_box)
        stock = Stock()
        stock.add_box(
            [
                list("abbcde"),
                list("abccde"),
                list("abcccd"),
                list("abeeed"),
                list("abcdef"),
            ]
        )
        assert stock.two_letters_boxes == 2
        assert stock.three_letters_boxes == 2
        assert stock.checksum == 4
