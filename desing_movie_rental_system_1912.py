# https://leetcode.com/problems/design-movie-rental-system/?envType=daily-question&envId=2025-09-21
from typing import List
from sortedcontainers import SortedList
from collections import defaultdict

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.available = defaultdict(SortedList)
        self.rented = SortedList()
        self.smp = {(s, m): p for s, m, p in entries}

        for s,m,p in entries:
            self.available[m].add((p, s))


    def search(self, movie: int) -> List[int]:
        # get 5 cheapest of movie
        return [s for _, s in self.available[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        # makes movie unavaliable (fifo)
        p = self.smp[(shop, movie)]
        self.available[movie].remove((p, shop))
        self.rented.add((p, shop, movie))
        

    def drop(self, shop: int, movie: int) -> None:
        # makes movie availablke (fifo)
        p = self.smp[(shop, movie)]
        self.rented.remove((p, shop, movie))
        self.available[movie].add((p, shop))
        

    def report(self) -> List[List[int]]:
        # cheapest 5 rented movies
        return [[s, m] for _, s, m in self.rented[:5]]


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()