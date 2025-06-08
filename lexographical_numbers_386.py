# https://leetcode.com/problems/lexicographical-numbers/description/?envType=daily-question&envId=2025-06-08

# this does not work, i can not see why
# class Solution:
#     def lexicalOrder(self, n: int) -> list[int]:
        
#         res = []
#         cur = 1

#         for _ in range(10):

#             res.append(cur)

#             if cur*10 <= n:

#                 cur *= 10

#             else:

#                 if cur >= n:
#                     cur //= 10

#                 cur += 1

#                 while cur % 10 == 9:
#                     cur //= 10


#         return res
#         ###########################################


class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        lexicographical_numbers = []
        current_number = 1

        # Generate numbers from 1 to n
        for _ in range(n):
            lexicographical_numbers.append(current_number)

            # If multiplying the current number by 10 is within the limit, do it
            if current_number * 10 <= n:
                current_number *= 10
            else:
                # Adjust the current number by moving up one digit
                while current_number % 10 == 9 or current_number >= n:
                    current_number //= 10  # Remove the last digit
                current_number += 1  # Increment the number

        return lexicographical_numbers