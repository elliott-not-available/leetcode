# longest_happy_string_1405
# https://leetcode.com/problems/longest-happy-string/description/?envType=daily-question&envId=2024-10-16

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        data = {'a': a, 'b': b, 'c': c}
        sl = sorted(data.items(), key=lambda x: x[1], reverse=True)

        # Initialise
        if sl[0][1] >= sl[1][1] * 2 and sl[0][1] >= 2:
            output = sl[0][0] * 2
            data[sl[0][0]] -= 2
        else:
            output = sl[0][0]
            data[sl[0][0]] -= 1

        # loop till done
        while True:

            temp_data = {x: y for x, y in data.items() if x != output[-1]}
            sl = sorted(temp_data.items(), key=lambda x: x[1], reverse=True)

            if sl[0][1] == 0:
                return output

            if data[output[-1]] * 2 <= sl[0][1] and sl[0][1] >= 2:
                # if previous input * 2 is less than or equal to current max
                output += sl[0][0] * 2
                data[sl[0][0]] -= 2
            else:
                # if previous output * 2 is greater than current max
                output += sl[0][0]
                data[sl[0][0]] -= 1

            print(temp_data)
            print(output)

import heapq

class Solution_TOP:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []
        if a > 0:
            heapq.headpush(pq, (-a, 'a'))
        if b > 0:
            heapq.headpush(pq, (-b, 'b'))
        if c > 0:
            heapq.headpush(pq, (-c, 'c'))

        result = []

        while pq:
            count1, char1 = heapq.heappop(pq)

            # if the last 2 chars are the same as char1
            if len(result) >= 2 and result[-1] == char1 and result[-2] == char1:
                if not pq:
                    # if pq is empty then we are done
                    break
                # otherwise get the next char from pq
                count2, char2 = heapq.heappop(pq)
                result.append(char2)
                count2 += 1 # (count is negative for so this is -1)

                # if count2 < 0 then push it back in pq
                if count2 < 0:
                    heapq.heappush(pq, (count2, char2))

                # also add c1 back to pq
                heapq.heappush(pq, (count1, char1))

            else:
                # otherwise use char1
                result.append(char1)
                count += 1

                if count < 0:
                    heapq.heappush(pq, (count, char1))

        return ''.join(result)