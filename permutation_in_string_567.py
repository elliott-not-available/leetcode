def validation(input1: str, input2: str) -> None:
    if len(input1) < 1 or len(input1) > 10 ** 4:
        raise ValueError(f"Input1: failed validation")
    if len(input2) < 1 or len(input2) > 10 ** 4:
        raise ValueError(f"Input2: failed validation")

def string_mapping(string_input: str) -> dict[str: int]:
    string_dict = {}
    for char in string_input:
        if char not in string_dict:
            string_dict[char] = 1
        else:
            string_dict[char] += 1
    return string_dict

def compare(s1:str, s2:str) -> bool:
    m1 = string_mapping(s1)
    m2 = string_mapping(s2)

    for k in m1:
        if k not in m2:
            return False
        if m2[k] != m1[k]:
            return False
    return True


class Solution_og:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        validation(s1, s2)

        # s1_d = string_mapping(s1)
        # s2_d = string_mapping(s2)

        # print(f"s1 :{s1_d}")

        # print(f"s2 :{s2_d}")

        # for k in s1_d.keys():

        #     if k not in s2_d:
        #         # print("Here")
        #         return False
        #     if s2_d[k] < s1_d[k]:
        #         # print("Here")
        #         return False
        
        wl = len(s1)
        sw_f = []
        # sw_b = []

        # exception for wl = len s2
        if wl == len(s2):
            if compare(s1,s2):
                return True
            else:
                return False


        for i in range(len(s2)):
            if i <= len(s2) - wl:
                sw_f = s2[i:i+wl]
            # if i >= (wl - 1):
            #     # sw_b = s2[i-wl+1:i+1]
            #     sw_b = s2[i+1:i-wl+1:-1]

            # print (f"WINDOW 1 {sw_f}           WINDOW 2 {sw_b}")
            if compare(s1, sw_f):
                return True
        return False
    
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        wl = len(s1)
        s2_n = len(s2)
        s1_c = Counter(s1)

        if s2_n< wl:
            return False

        if wl == s2_n:
            return s1_c == Counter(s2)
        
        # the example solution shows while looping through i and iterating on the counter is faster
        for i in range(s2_n):
            if i <= len(s2) - wl:
                temp_c = Counter(s2[i:i+wl])
                if s1_c == temp_c:
                    return True
        return False



