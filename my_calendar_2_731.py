from dataclasses import dataclass, field


def validate_start(start: int) -> bool:
    return start >= 0


def validate_end(end: int) -> bool:
    return end <= 10**9


def validate_relative(start:int, end:int) -> bool:
    return start < end


def validation(start:int, end:int) -> None:
    fail_message = f"Validation failed for start value: {start} and end value: {end}"
    if not validate_start(start):
        raise ValueError(fail_message)
    if not validate_end(start):
        raise ValueError(fail_message)
    if not validate_relative(start, end):
        raise ValueError(fail_message)


@dataclass
class a_booking:
    start: int
    end: int

    def __post_init__(self) -> None:
        validation(start=self.start, end=self.end)


def check_no_booking_overlap(new: a_booking, old: a_booking) -> bool:
    # if the booking starts during an existing booking return False
    if new.start >= old.start and new.start < old.end:
        return False
    # if the booking ends during an existing booking return False
    if new.end > old.start and new.end <= old.end:
        return False
    # if the booking envelops an existing booking return False
    if new.start <= old.start and new.end >= old.end:
        return False
    return True    


@dataclass
class MyCalendarTwo:

    booking_list: list[a_booking] = field(default_factory=list)
    number_of_book_calls: int = 0
    call_threshold = 1000

    def book(self, start: int, end: int) -> bool:

        new_booking = a_booking(start=start, end=end)
        # print(f"input: {new_booking}")

        self.number_of_book_calls += 1
    
        if self.number_of_book_calls > self.call_threshold:
            raise ValueError(f"Number of book calls made to a singular calendar exceed threshold of {self.call_threshold}")
        
        overlapped = []
        for booking in self.booking_list:
            resp = check_no_booking_overlap(new_booking, booking)
            if not resp:
                # print(f"new booking = {new_booking} is overlaping with old booking = {booking}")
                overlapped.append(booking)

            # of the overlapped bookings check they also do not overlap,
            if len(overlapped) >= 2:
                for i, x in enumerate(overlapped):
                    for n in range(i+1, len(overlapped)):
                        overlap_resp = check_no_booking_overlap(x, overlapped[n])
                        if not overlap_resp:
                            return False
            
        self.booking_list.append(new_booking)
        return True
    

if __name__ == "__main__":
    cal = MyCalendarTwo()
    values = [[10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
    output = []
    for v in values:
        output.append(cal.book(v[0], v[1]))

    print(output)