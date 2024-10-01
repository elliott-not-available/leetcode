# TODO: https://leetcode.com/problems/all-oone-data-structure/description/?envType=daily-question&envId=2024-09-29
class AllOne:

    def __init__(self):
        self.store: dict[str, int] = {}

        self.max_str: str = ""
        self.max_count: int = 0

        self.min_str: str = ""
        self.min_count: int = 0
        

    def inc(self, key: str) -> None:
        
        if key in self.store.keys():
            self.store[key] += 1
        else:
            self.store = 1

        

    def dec(self, key: str) -> None:
        pass

    def getMaxKey(self) -> str:
        pass

    def getMinKey(self) -> str:
        pass