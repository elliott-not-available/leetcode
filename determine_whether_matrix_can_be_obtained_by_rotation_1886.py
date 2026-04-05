# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/description/?envType=daily-question&envId=2026-03-22

class Solution:

    def rotate_90(self, mat):
        n = len(mat)

        for i in range(n):
            for j in range(i, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        for i in range(n):
            mat[i].reverse()


    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        # if mat==target:
        #     return True
        
        for _ in range(4):
            if mat==target:
                return True
            self.rotate_90(mat)
        return False




        