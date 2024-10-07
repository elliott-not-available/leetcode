# https://leetcode.com/problems/sentence-similarity-iii/description/?envType=daily-question&envId=2024-10-06

# UNSOLVED

class Solution_og:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        
        s1_n = len(sentence1)
        s2_n = len(sentence2)

        if s1_n == s2_n:
            if sentence1 == sentence2:
                return True
            return False
                
        if s1_n < s2_n:
            small = sentence1
            large = sentence2
        elif s1_n > s2_n:
            small = sentence2
            large = sentence1

        small_n = len(small)
        large_n = len(large)

        if small == large[0:small_n]:
            # print(large[small_n])
            if large[small_n] == " ":
                return True
            return False

        start = ""
        start_finish = False
        end_finish = False
        end = ""

        i = 0
        while i < small_n:

            if not start_finish:
                if small[i] == large[i]:
                    start += small[i]
                else:
                    start_finish = True

            if not end_finish:
                # -0 = 0
                if small[-i-1] == large[-i-1]:
                    end = small[-i-1] + end
                else:
                    end_finish = True
            
            i += 1
  
        mid = large[len(start) : large_n - len(end)]

        if end and mid:
            if end[0] == " ":
                end = end[1:]
                mid+= " "

        print(f"small sentence = {small}")
        print(f"large sentece = {large}")

        print(f"start: '{start}'")
        print(f"middle: '{mid}'")
        print(f"end: '{end}'")

        # if mid:
        #     if mid[-1] == " ":
        #         return False

        if mid == large:
            return False

        if start + mid + end != large:
            return False
        # if not start and not end:
        #     return False
            
        # if start[-1] == " " and end[0] == " ":
        #     return True
        
        # if end =="" and mid[0] == " ":
        #     return True
        if small in start.strip() + " "+end.strip():
            return True
        return False
    

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        
        s1_n = len(sentence1)
        s2_n = len(sentence2)

        if s1_n == s2_n:
            if sentence1 == sentence2:
                return True
            return False
                
        if s1_n < s2_n:
            small = sentence1.split()
            large = sentence2.split()
        elif s1_n > s2_n:
            small = sentence2.split()
            large = sentence1.split()

        small_n = len(small)
        large_n = len(large)

        start, end = 0, 0

        # print(small)

        while start < small_n and small[start] == large[start]:
            start += 1

        while end < small_n and small[small_n - 1 - end] == large[large_n - 1 - end]:
            end += 1

        return start + end >= small_n