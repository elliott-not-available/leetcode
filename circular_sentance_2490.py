# circular_sentance_2490
# https://leetcode.com/problems/circular-sentence/

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()

        if words[0][0] != words[-1][-1]:
            return False

        temp_end = words[0][-1]

        for w in words[1:]:
            if w[0] != temp_end:
                return False
            temp_end = w[-1]
        return True