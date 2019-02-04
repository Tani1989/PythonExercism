class Luhn(object):
    def __init__(self, card_num):
        self.card_num = card_num
        self.sum_of_all_numbers = 0

        pass

    def is_valid(self):
        remove_whitespace = self.card_num.replace(" ", "")
        list_of_rejected = [":", "-", "a", "$", "a"]

        for j, num in enumerate(remove_whitespace):
            if num in list_of_rejected:
                 return False

        convert_to_int = [int(digits) for digits in str(remove_whitespace)]
        old_list = list(convert_to_int)
        new_list = []

        if len(old_list) % 2 == 0:
            for index, number in enumerate(old_list):
                if index % 2 == 0:
                    new_list.append(number * 2)
                else:
                    new_list.append(number * 1)
        else:
            for index, number in enumerate(old_list):
                if index % 2 == 0:
                    new_list.append(number * 1)
                else:
                    new_list.append(number * 2)

        for indexes, numm in enumerate(new_list):
            if len(new_list) == 1 and numm == 0:
                return False

        new_list1 = []
        for i, two_digits in enumerate(new_list):
            if two_digits > 9:
                convert_to_string = str(two_digits)
                new_list1.append(sum(map(int, convert_to_string)))
            else:
                new_list1.append(two_digits)

        self.sum_of_all_numbers = sum(new_list1)
        if self.sum_of_all_numbers % 10 == 0:
             return True
        else:
            return False


