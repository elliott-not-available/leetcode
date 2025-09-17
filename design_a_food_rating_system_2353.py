# https://leetcode.com/problems/design-a-food-rating-system/description/?envType=daily-question&envId=2025-09-17
from typing import List
import heapq
  
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):

        self.data = {}
        self.max_heaps = {}

        for f, c, r in zip(foods, cuisines, ratings):
            self.data[f] = [c, r]
            
            if c not in self.max_heaps:
                self.max_heaps[c] = []
            
            heapq.heappush(self.max_heaps[c], (-r, f))


        

    def changeRating(self, food: str, newRating: int) -> None:

        c, old_rating = self.data[food]

        self.data[food] = [c, newRating]
        heapq.heappush(self.max_heaps[c], (-newRating, food))

        

    def highestRated(self, cuisine: str) -> str:
        # print(self.max_heaps[cuisine])
        # r, f = self.max_heaps[cuisine][0]
        # return f if r == self.data[f][1]*-1 else self.max_heaps[cuisine][1][1]

        cuis = self.max_heaps[cuisine]
        print(cuis)

        while cuis:

            r, f = cuis[0]
            if r == self.data[f][1]*-1:
                return f
            heapq.heappop(cuis)
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)