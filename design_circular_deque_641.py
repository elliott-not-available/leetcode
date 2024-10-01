def validate_k(k: int) -> bool:
    if not (k>=1 & k<=1000):
        raise ValueError(f"Supplied k is not within acceptable params: {k}")


def validate_value(value: int) -> bool:
    if not (value>=1 & value<=1000):
        raise ValueError(f"Supplied value is not within acceptable params: {value}")


class MyCircularDeque:

    def __init__(self, k: int):
        self.list = []
        self.maxsize = k

    def __post_init__(self):
        validate_k(self.list[0])
        

    def insertFront(self, value: int) -> bool:
        validate_value(value)
        if len(self.list) < self.maxsize:
            self.list.append(value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        validate_value(value)
        if len(self.list) < self.maxsize:
            self.list.insert(0, value)
            return True
        return False

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        try:
            self.list = self.list[:-1]
            return True
        except:
            return False

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        
        try:
            self.list = self.list[1:]
            return True
        except:
            return False

    def getFront(self) -> int:
        try:
            return self.list[-1]
        except:
            return -1


    def getRear(self) -> int:
        try:
            return self.list[0]
        except:
            return -1

    def isEmpty(self) -> bool:
        if self.list:
            return False
        return True
    
    def isFull(self) -> bool:
        return len(self.list) == self.maxsize