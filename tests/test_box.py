from warehouse.box import Box


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
