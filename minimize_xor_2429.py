class Solution:
    def _set_bit(self, x: int, bit: int):
        return x | (1 << bit)
    
    def _unset_bit(self, x: int, bit: int):
        return x & ~(1 << bit)
    
    def _is_set(self, x: int, bit: int) -> bool:
        return (x & (1 << bit)) != 0
    
    def minimizeXor(self, num1: int, num2: int) -> int:

        res = num1

        target = bin(num2).count("1")
        set_bits_cnt = bin(res).count("1")

        cur_bit = 0

        while set_bits_cnt < target:
            if not self._is_set(res, cur_bit):
                res = self._set_bit(res, cur_bit)
                set_bits_cnt += 1
            cur_bit += 1

        while set_bits_cnt > target:
            if self._is_set(res, cur_bit):
                res = self._unset_bit(res, cur_bit)
                set_bits_cnt -= 1
            cur_bit += 1

        return res