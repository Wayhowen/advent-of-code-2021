from collections import defaultdict
from typing import List


# TODO: code is ineffective, mainly because i have realized, that we need to calculate the most
#  common bit with each filtering step, not just once for the whole array..
class Solver:
    def __init__(self, task_input):
        self.task_input = task_input

    def solve(self):
        oxygen_generator_rating = self.find_oxygen_generator_rating(
            self.task_input
        )
        co_scrubber_rating = self.find_co_scrubber_rating(
            self.task_input
        )

        return self.bit_to_int(oxygen_generator_rating) * self.bit_to_int(co_scrubber_rating)

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
            if bit_rarity['1'] >= bit_rarity['0']:
                bit_string += '1'
            else:
                bit_string += '0'
        return bit_string

    def find_oxygen_generator_rating(self, bit_strings: List[str]):
        index = 0
        while len(bit_strings) != 1:
            rarity = self.find_rarity_of_bits(bit_strings)
            most_common_bit_string = self.find_most_common_bit_string(rarity)
            bit_strings = list(filter(
                lambda s: s[index] == most_common_bit_string[index],
                bit_strings))
            index += 1
        return bit_strings[0]

    def find_co_scrubber_rating(self, bit_strings: List[str]):
        index = 0
        while len(bit_strings) != 1:
            rarity = self.find_rarity_of_bits(bit_strings)
            most_common_bit_string = self.find_most_common_bit_string(rarity)
            bit_strings = list(filter(
                lambda s: s[index] != most_common_bit_string[index],
                bit_strings))
            index += 1
        return bit_strings[0]

    def bit_to_int(self, bit_string):
        return int(bit_string, 2)
