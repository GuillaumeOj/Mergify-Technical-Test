from warehouse.stock import Stock
from warehouse.box import Box


class MockBoxHasDoubleTriple:
    def has_double(self):
        return True

    def has_triple(self):
        return True


class MockBoxHasDoubleNoTriple:
    def has_double(self):
        return True

    def has_triple(self):
        return False


class MockBoxHasNoDoubleTriple:
    def has_double(self):
        return False

    def has_triple(self):
        return True


class MockBoxHasNoDoubleNoTriple:
    def has_double(self):
        return False

    def has_triple(self):
        return False


class TestStock:
    def test_stock_has_one_box_with_two_letters(self, monkeypatch):
        monkeypatch.setattr("warehouse.box.Box", MockBoxHasDoubleNoTriple)
        stock = Stock([Box("abbcde")])
        assert stock.two_letters_boxes == 1
        assert stock.three_letters_boxes == 0
        assert stock.checksum == 0

    def test_stock_has_one_box_with_three_letters(self, monkeypatch):
        monkeypatch.setattr("warehouse.box.Box", MockBoxHasNoDoubleTriple)
        stock = Stock([Box("abcccd")])
        assert stock.two_letters_boxes == 0
        assert stock.three_letters_boxes == 1
        assert stock.checksum == 0

    def test_stock_has_one_box_with_two_letters_and_one_box_with_three_letters(
        self, monkeypatch
    ):
        monkeypatch.setattr("warehouse.box.Box", MockBoxHasDoubleTriple)
        stock = Stock([Box("abbcde"), Box("abcccd")])
        assert stock.two_letters_boxes == 1
        assert stock.three_letters_boxes == 1
        assert stock.checksum == 1
