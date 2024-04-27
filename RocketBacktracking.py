import sys
"""
    name:  Elizabeth Johnson

"""


class RocketSections:
    def __init__(self, number_list, final_sum, count_table):
        self.final_sum = final_sum  # holds what the rocket sum should be
        self.number_list = number_list  # holds the section parts
        self.least_section = sys.maxsize
        self.section_count = 1
        self.count_table = count_table
        self.save_table = count_table.copy()

    def isLessSections(self):
        if self.least_section > self.section_count:
            self.least_section = self.section_count
            self.save_table = self.count_table.copy()

    def computeSections(self, test_val, index):
        if test_val == self.final_sum:
            self.isLessSections()
        elif index >= 1 and test_val + self.number_list[index] > self.final_sum:
            self.computeSections(test_val, index - 1)
        elif test_val + self.number_list[index] <= self.final_sum:
            self.section_count += 1
            # self.count_table[index] += 1
            current_section_count = self.section_count
            current_table = self.count_table.copy()
            for i in range(index, -1, -1):
                self.count_table[i] += 1
                self.computeSections(test_val + self.number_list[i], i)
                self.section_count = current_section_count
                self.count_table = current_table.copy()

    def testThis(self):
        for i in range(len(self.number_list) - 1, -1, -1):
            self.section_count = 1
            self.count_table = [0] * len(self.number_list)
            self.count_table[i] = 1
            self.computeSections(self.number_list[i], i)
        return self.least_section


# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts
def main():
    input_numbers = list(map(int, input().split(" ")))
    input_sum = int(input())
    table = [0] * len(input_numbers)
    rocket_sections = RocketSections(input_numbers, input_sum, table)
    # rocket_sections.computeSections(input_numbers[len(input_numbers) - 1], len(input_numbers) - 1)
    sections = str(rocket_sections.testThis())
    for i in range(len(input_numbers)):
        print(str(rocket_sections.save_table[i]) + " of length " + str(input_numbers[i]))
    print(sections + " rocket sections minimum")
    # print(str(rocket_sections.least_section) + " rocket sections minimum")
    pass


if __name__ == "__main__":
    main()
