from dataclasses import dataclass, field

def validate_start(start: int) -> bool:
    return start >= 0

def validate_end(end: int) -> bool:
    return end <= 10**9

@dataclass
class a_booking:
    start: int
    end: int

    def __post_init__(self) -> None:
        if not validate_start(self.start):
            raise ValueError(f"start value {self.start} failed validation")
        if not validate_end(self.end):
            raise ValueError(f"end value {self.end} failed validation")

@dataclass
class MyCalendar:

    list_of_bookings: list[a_booking] = field(default_factory=list)
    number_of_book_calls: int = 0
    call_threshold = 1000

    def book(self, start: int, end: int) -> bool:
        self.number_of_book_calls += 1
        if self.number_of_book_calls > self.call_threshold:
            raise ValueError(f"Number of book calls made to a singular calendar exceed threshold of {self.call_threshold}")
        
        # this would be faster with a number map (although memory issues witha very large numbers)
        for booking in self.list_of_bookings:
            # if the booking starts during an existing booking return False
            if start >= booking.start and start < booking.end:
                return False
            # if the booking ends during an existing booking return False
            if end > booking.start and end <= booking.end:
                return False
            # if the booking envelops an existing booking return False
            if start <= booking.start and end >= booking.end:
                return False
            
        # add the booking and return true
        self.list_of_bookings.append(a_booking(start=start, end=end))
        return True


if __name__ == "__main__":
    cal = MyCalendar()
    resp1 = cal.book(10,20)
    resp2 = cal.book(15,25)
    resp3 = cal.book(20,30)

    print(resp1, resp2, resp3)