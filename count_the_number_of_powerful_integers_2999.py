# https://leetcode.com/problems/count-the-number-of-powerful-integers/description/?envType=daily-question&envId=2025-04-10

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:

        # # brute force - O(finish-start) - timelimit exceeded


        # def check_limit(prefix, limit):
        #     for c in str(prefix):
        #         if int(c) > limit:
        #             return False
        #     return True

        # cur = int(s)
        # pre = 0
        # # pot = 0
        # res = 0

        # while cur < finish:
        #     # prefix = pre * (10**pot)
        #     cur = int(str(pre) + s)
        #     if not check_limit(pre, limit):
        #         pre += 1
        #         continue
        #     if cur > finish:
        #         break
        #     if cur < start:
        #         pre += 1
        #         continue

        #     print(f"{cur}")
        #     pre += 1
        #     res += 1

        # return res
        ##########################################################

        # calculate number of digits that satisfy limit in 0-9
        # calculate number of digits that can be added to s before > finish
        # calculate number of digits that can be added to s before > start-1

        # count(finish) - count(start-1)

        # limit + 1

        def calc(fin:str, s:str, limit:int) -> int:

            if len(fin) < len(s):
                return 0
            if len(fin) == len(s):
                return 1 if fin >= s else 0
            
            suffix = fin[len(fin) - len(s):]
            count = 0
            pre_len = len(fin) - len(s)

            for i in range(pre_len):
                if limit < int(fin[i]):
                    count += (limit + 1) ** (pre_len - i)
                    return count
                count += int(fin[i]) * (limit + 1) ** (pre_len -1 -i)

            if suffix >= s:
                count += 1

            return count
        
        fin_ = str(finish)
        start_ = str(start - 1)

        return calc(fin_, s, limit) - calc(start_, s, limit)

