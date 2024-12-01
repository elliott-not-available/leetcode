# check_if_n_and_its_double_exists_1346
# https://leetcode.com/problems/check-if-n-and-its-double-exist/description/?envType=daily-question&envId=2024-12-01

class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        doubles = [2*j for j in arr]

        for ind_i, i in enumerate(arr):
            for ind_j, j in enumerate(doubles):
                if ind_i == ind_j:
                    continue
                if i == j:
                    return True
        return False
        