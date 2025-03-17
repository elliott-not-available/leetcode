from collections import defaultdict
from sortedcontainers import SortedSet
# from typing import SortedSet

class NumberContainers:

    # another shitty solution, not able to0 focus sorry
    
    def __init__(self):
        self.data = {}
        self.mins = defaultdict(SortedSet)

    def change(self, index: int, number: int) -> None:

        # if index already exists, remove from mins
        if index in self.data.keys():
            old_number = self.data[index]
            self.mins[old_number].remove(index)

        # perform change
        self.data[index] = number
        
        # # if number not in mins, add
        # if number not in self.mins.keys():
        #     self.mins[number] = [index]
        # # if number is in mins, add and sort
        # else:
        #     # temp = self.mins[number]
        #     # temp.append(index)
        #     # self.mins[number] = sorted(temp)
        #     self.mins.append[number]

        self.mins[number].add(index)

    def find(self, number: int) -> int:
        if number in self.mins and self.mins[number]:
        # print(self.data)
        # print(self.mins)
            return self.mins[number][0]
        return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)