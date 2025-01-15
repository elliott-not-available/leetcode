class Solution:
    # 2 / 3 pass
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        res = []

        set_a = set()
        set_b = set()

        for a, b in zip(A,B):
            set_a.add(a)
            set_b.add(b)

            t = set_a.intersection(set_b)
            res.append(len(t))

        return res
