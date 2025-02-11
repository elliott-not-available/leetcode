class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # i = 0
        # res = []
        # m = len(part)
        # match = [c for c in part]

        # while i < len(s):
        #     window = s[i:i+m]
        #     if part == window:
        #         i += m
        #     else:
        #         res.append(s[i])
        #         if len(res) >= m:
        #             if res[-m:] == match:
        #                 res = res[:-m]
        #         i += 1
        # return "".join(res)

        stack = []
        m = len(part)
        match = [char for char in part]

        for c in s:
            stack.append(c)

            if len(stack) >= m and (stack[-m:] == match):
                # or stack = stack[:-m]
                for _ in range(m):
                    stack.pop() 

        return "".join(stack)