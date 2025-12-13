# https://leetcode.com/problems/coupon-code-validator/description/?envType=daily-question&envId=2025-12-13
from string import ascii_letters
class Solution:
    def validateCoupons(self, code: list[str], businessLine: list[str], isActive: list[bool]) -> list[str]:
        
        # valid code (alphanumeric + "_")
        def c_check(item):
            if item:
                return all(c in ascii_letters+"_"+"0123456789" for c in item)
            return False

        # buisnessline is one of ["electronics", "grocery", "pharmacy", "restaurant"] 
        def b_check(item):
            if item in {"electronics", "grocery", "pharmacy", "restaurant"}:
                return True
            return False
        
        r_map = {
            "electronics":[], 
            "grocery":[], 
            "pharmacy":[], 
            "restaurant":[],
        }

        for i in range(len(code)):
            if not isActive[i]:
                continue

            if not b_check(businessLine[i]):
                continue
            
            if c_check(code[i]):
                r_map[businessLine[i]].append(code[i])


        for k,_ in r_map.items():
            r_map[k].sort()

        return r_map["electronics"] + r_map["grocery"] + r_map["pharmacy"] + r_map["restaurant"] 