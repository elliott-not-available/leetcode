
# I think this should return a boolean and then the error should be raised in use place.
# This would probably lead to more helpfull error messages
def input_validation_1(input_1) -> None:
    if not (1 <= input_1 <= 1000):
        raise ValueError("Failed input 1 validation")

def input_validation_2(input_2) -> None:
    if not (0 <= input_2 <= 100):
        raise ValueError("Failed input 2 validation")


class CustomStack:

    def __init__(self, max_size: int):
        self.max_size = max_size
        self.stack = []

        self.max_calls = 1000
        self.push_calls = 0
        self.pop_calls = 0
        self.increment_calls = 0


    def __post_init__(self):
        input_validation_1(self.max_size)


    def push(self, x: int) -> None:
        input_validation_1(x)

        if self.push_calls >= self.max_calls:
            raise ValueError(f"Maximum number of calls {self.max_calls} reached")

        if len(self.stack) < self.max_size:
            self.stack.append(x)
        

    def pop(self) -> int:
        if self.pop_calls >= self.max_calls:
            raise ValueError(f"Maximum number of calls {self.max_calls} reached")
        if not self.stack:
            return -1
        return self.stack.pop(-1)


    def increment(self, k: int, val: int) -> None:
        input_validation_1(k)
        input_validation_2(val)
        
        if self.increment_calls >= self.max_calls:
            raise ValueError(f"Maximum number of calls {self.max_calls} reached")
        
        if k > len(self.stack): k = len(self.stack)

        for i in range(k):
            self.stack[i] += val