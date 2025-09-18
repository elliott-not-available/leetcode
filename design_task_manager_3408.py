# https://leetcode.com/problems/design-task-manager/?envType=daily-question&envId=2025-09-18
from typing import List
from collections import defaultdict
import heapq
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        # grab task by task id
        # grab top priority
        self.data = defaultdict()
        self.prio_heap = []

        for user_id, task_id, priority in tasks:
            self.add(user_id, task_id, priority)
        

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.data[taskId] = (userId, priority)
        heapq.heappush(self.prio_heap, (-priority, -taskId, userId))
        

    def edit(self, taskId: int, newPriority: int) -> None:
        user_id, _ = self.data[taskId]
        self.add(user_id, taskId, newPriority)
        

    def rmv(self, taskId: int) -> None:
        # del self.data[taskId] # will throw error if key doesnt exist
        # self.data.pop(taskId, None) # returns none if key doesnt exist
        self.data[taskId] = -1
        

    def execTop(self) -> int:

        while self.prio_heap:
            prio_n, task_id_n, user_id = heapq.heappop(self.prio_heap)
            t = task_id_n * -1
            p = prio_n * -1

            if self.data[t] == (user_id, p):
                self.data[t] = -1
                return user_id
        return -1

        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()

