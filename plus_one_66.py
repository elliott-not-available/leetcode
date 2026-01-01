class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        return [c for c in str(int("".join(map(str, digits)))+1)]