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
        self.count_table = count_table # holds how many of each section
        self.save_table = count_table.copy()

    def isLessSections(self): # if the section number is less than the one before, save the current section table
        if self.least_section > self.section_count:
            self.least_section = self.section_count
            self.save_table = self.count_table.copy()

    def computeSections(self, test_val, index):
        if test_val == self.final_sum:
            self.isLessSections() # maybe save current section table
        elif index >= 1 and test_val + self.number_list[index] > self.final_sum:
            # if adding the next section brings it higher than the final sum, then move to the next smallest section
            self.computeSections(test_val, index - 1)
        elif test_val + self.number_list[index] <= self.final_sum:
            # add the next section to the list if it is below the final sum
            self.section_count += 1
            current_section_count = self.section_count
            current_table = self.count_table.copy()
            for i in range(index, -1, -1):
                self.count_table[i] += 1
                self.computeSections(test_val + self.number_list[i], i)
                self.section_count = current_section_count
                self.count_table = current_table.copy()

    def testThis(self):
        for i in range(len(self.number_list) - 1, -1, -1): # move through range in reverse order
            self.section_count = 1 # accounts for first section
            self.count_table = [0] * len(self.number_list)
            self.count_table[i] = 1
            self.computeSections(self.number_list[i], i)
        return self.least_section


def main():
    # get inputs
    input_numbers = list(map(int, input().split(" "))) # convert input to list of integers
    input_sum = int(input())

    # create table to save the counts of each section and initialize class
    table = [0] * len(input_numbers)
    rocket_sections = RocketSections(input_numbers, input_sum, table)

    # divides the sections up to get all combinations for finding the least sections
    sections = str(rocket_sections.testThis())

    # print the number of pieces for each section and the total number of sections
    for i in range(len(input_numbers)):
        print(str(rocket_sections.save_table[i]) + " of length " + str(input_numbers[i]))
    print(sections + " rocket sections minimum")
    pass


if __name__ == "__main__":
    main()
