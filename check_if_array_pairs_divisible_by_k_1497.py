def get_range_from_k(k: int) -> tuple[int, bool]:
    if k % 2 !=0:
        y = int((k-1) / 2)
        even = False
    else:
        y = int((k / 2))
        even = True
    return y, even


class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:
        
        if len(arr) % 2 != 0:
            return False
        
        mod_freq = {}

        for i in range(k):
            mod_freq[i] = 0

        for v in arr:
            mod = v % k
            # if mod in mod_freq:
            mod_freq[mod] += 1
            # else:
            #     mod_freq[mod] = 1

        y, even = get_range_from_k(k)

        # this can be optimised, do not need to check the second (k-1)/2
        for x in range(1,y+1):
            if mod_freq[x] != mod_freq[k-x]:
                return False
        
        if even:
            if mod_freq[y] % 2 != 0:
                return False
            
        return True

