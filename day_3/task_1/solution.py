from collections import defaultdict


class Solver:
    def __init__(self, task_input):
        self.task_input = task_input

    def solve(self):
        rarity = self.find_rarity_of_bits(self.task_input)
        most_common_bit_string = self.find_most_common_bit_string(rarity)
        inverse = self.find_inverse_of_most_common_bit_string(most_common_bit_string)
        return self.bit_to_int(most_common_bit_string) * self.bit_to_int(inverse)

    def find_rarity_of_bits(self, bit_strings):
        rarity = defaultdict(
            lambda: defaultdict(lambda: 0)
        )
        for bit_string in bit_strings:
            for index, bit in enumerate(bit_string):
                rarity[index][bit] += 1
        return rarity

    def find_most_common_bit_string(self, rarity):
        bit_string = ""
        for bit, bit_rarity in rarity.items():
            if bit_rarity['1'] > bit_rarity['0']:
                bit_string += '1'
            else:
                bit_string += '0'
        return bit_string

    def find_inverse_of_most_common_bit_string(self, bit_string):
        inverse = ""
        for bit in bit_string:
            if bit == "0":
                inverse += '1'
            else:
                inverse += '0'
        return inverse

    def bit_to_int(self, bit_string):
        return int(bit_string, 2)
