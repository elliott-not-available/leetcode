# https://leetcode.com/problems/implement-router/description/?envType=daily-question&envId=2025-09-20
from typing import List
from collections import deque, defaultdict
from bisect import bisect_left, bisect_right

class Router:

    def __init__(self, memoryLimit: int):
        self.max = memoryLimit
        self.cur_size = 0
        self.data = defaultdict(int)
        self.fifo = deque()

        self.destinations = defaultdict(deque)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        # check data for duplicaties
        if (source, destination, timestamp) in self.data and self.data[(source, destination, timestamp)] > 0:
            # print(f"Duplicate found for {(source, destination, timestamp)}")
            return False
        
        # check size limit
        if self.cur_size >= self.max:
            # recursively remove oldest packet until there is space
            # print(f"Reached max size, removing oldest packet")
            oldest_pack = self.forwardPacket()
            print(oldest_pack)
            return self.addPacket(source, destination, timestamp)

        # add packet
        # print(f"Adding packet: {(source, destination, timestamp)}")
        self.fifo.append((source, destination, timestamp))
        self.data[(source, destination, timestamp)] += 1
        self.cur_size += 1

        self.destinations[destination].append(timestamp)
        return True
        

    def forwardPacket(self) -> List[int]:
        # I think i would create a seperate function, remove_oldest_package
        # and use that in add package instead of this

        # pop from fifo
        if self.fifo:
            old_source, old_dest, old_ts = self.fifo.popleft()
            # print(f"Oldest package found is: {(old_source, old_dest, old_ts)}")

            # remove from data
            self.data[(old_source, old_dest, old_ts)] -= 1
            self.cur_size -= 1

            # if self.data[(old_source, old_dest, old_ts)] == 0:
            del self.data[(old_source, old_dest, old_ts)]
            self.destinations[old_dest].popleft()

            return [old_source, old_dest, old_ts]
        # print("No packages in queue")
        return []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        # too slow
        # cnt = 0
        # for k,v in self.data.items():
        #     _, d, ts = k

        #     if d == destination and ts>=startTime and ts<=endTime:
        #         cnt += v
        # return cnt

        # print(self.destinations[destination])
        l = bisect_left(self.destinations[destination], startTime) # left of start time not inclusive
        r = bisect_right(self.destinations[destination], endTime) # left?? of end time inclusive
        # print(l, r)
        return r - l



# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)