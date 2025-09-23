# https://leetcode.com/problems/compare-version-numbers/description/?envType=daily-question&envId=2025-09-23

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")

        n1= len(v1)
        n2 = len(v2)

        for a, b in zip(v1,v2):
            if int(a) < int(b): return -1
            if int(a) > int(b): return 1

        n3 = min(n1,n2)
        if n1<n2:
            return -1 if any(int(v2[i])>0 for i in range(n3,n2)) else 0
        elif n1>n2:
            return 1 if any(int(v1[i])>0 for i in range(n3,n1)) else 0
        return 0 
        # return 1 if int(version1.split(".")[1]) > int(version2.split(".")[1]) else -1