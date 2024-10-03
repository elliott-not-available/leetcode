def validation(input: list[int]) -> None:
    if len(input) < 0 or len(input) > 10 ** 5:
        raise ValueError("Failed input validation")
    # list element validation


class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:

        validation(arr)

        sorted_arr = sorted(set(arr))

        # sorted_index = []
        # temp_val = None
        # indx = 0

        # print(sorted_arr)

        # for val in sorted_arr:
        #     if temp_val is None:
        #         indx = 1
        #         temp_val = val
        #         sorted_index.append(indx)
        #     elif val == temp_val:
        #         sorted_index.append(indx)
        #     else:
        #         indx += 1
        #         temp_val = val
        #         sorted_index.append(indx)

        # print(sorted_index)

        # for x in arr:
        #     for i, y in enumerate(sorted_arr):
        #         if x == y:
        #             # v = sorted_arr.index(y)
        #             # duplicates = len(sorted_arr[:v]) - len(set(sorted_arr[:v]))
        #             output_arr.append((i+1))# - duplicates)
        #             break

        rank_dict = {}
        for i, val in enumerate(sorted_arr):
            rank_dict[val] = i + 1

        for j, val in enumerate(arr):
            arr[j] = rank_dict[val]

        return arr