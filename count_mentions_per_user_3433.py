# https://leetcode.com/problems/count-mentions-per-user/description/?envType=daily-question&envId=2025-12-12
from operator import add
class Solution:
    def countMentions(self, numberOfUsers: int, events: list[list[str]]) -> list[int]:
        events.sort(key=lambda x: (int(x[1]), x[0] == "MESSAGE"))

        online = [True] * numberOfUsers
        offline = [False] * numberOfUsers
        res = [0] * numberOfUsers
        
        print(events)

        def convert_mentions(mes):
            out = [0] * numberOfUsers

            for element in mes.split("id")[1:]:
                element = int(element.strip())

                out[element] += 1
            return out


        for event in events:
            time = int(event[1])

            for i in range(numberOfUsers):
                u = offline[i]
                if u:
                    if time >= u+60:
                        offline[i] = False
                        online[i] = True

            if event[0] == "OFFLINE":
                offline[int(event[2])] = int(event[1])
                online[int(event[2])] = False

            if event[0] == "MESSAGE":

                m = event[2]

                if m == "ALL":
                    res = list( map(add, res, [1] * numberOfUsers) )
                elif m == "HERE":
                    res = list( map(add, res, online) )
                else:
                    mentions = convert_mentions(m)
                    res = list( map(add, res, mentions) )

            


        return res