class Finder:
    def compare_boxes(self, box1, box2):

        compared_list = list()
        for i, letter in enumerate(box1.box_id):
            if letter == box2.box_id[i]:
                compared_list.append(True)
            else:
                compared_list.append(False)

        if compared_list.count(False) == 1:
            return True

    def common_letters(self, box1, box2):
        common_letters = list()
        for i, letter in enumerate(box1.box_id):
            if letter == box2.box_id[i]:
                common_letters.append(letter)

        return "".join(common_letters)
