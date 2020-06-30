from warehouse.finder import Finder
from warehouse.box import Box


class MockBox:
    def __init__(self, box_id):
        self.box_id = list(box_id)


class TestFinder:
    def test_compare_boxes_with_one_different_character_in_same_position(
        self, monkeypatch
    ):
        monkeypatch.setattr("warehouse.box.Box", MockBox)
        result = Finder().compare_boxes(Box("fghij"), Box("fguij"))
        assert result

    def test_compare_boxes_with_no_different_character(self, monkeypatch):
        monkeypatch.setattr("warehouse.box.Box", MockBox)
        result = Finder().compare_boxes(Box("fghij"), Box("fghij"))
        assert not result

    def test_compare_boxes_with_one_different_character_in_different_positions(
        self, monkeypatch
    ):
        monkeypatch.setattr("warehouse.box.Box", MockBox)
        result = Finder().compare_boxes(Box("fghij"), Box("fgiuj"))
        assert not result

    def test_compare_boxes_with_two_different_characters(self, monkeypatch):
        monkeypatch.setattr("warehouse.box.Box", MockBox)
        result = Finder().compare_boxes(Box("fghij"), Box("fguxj"))
        assert not result

    def test_common_letters(self, monkeypatch):
        monkeypatch.setattr("warehouse.box.Box", MockBox)
        result = Finder().common_letters(Box("fghij"), Box("fguij"))
        assert result == "fgij"

