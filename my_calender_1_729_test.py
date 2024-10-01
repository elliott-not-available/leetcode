from my_calender_1_729 import MyCalendar

# scruffy fixing of a failing leetcode test - i had forgotten to account for the scenario where
# a new booking fully encloses and existing booking

def running_a_test(input: list) -> list[bool]:
    cal = MyCalendar()
    output = []

    for timings in input:
        # print(timings)
        resp = cal.book(start=timings[0], end=timings[1])
        # print(resp)
        output.append(resp)
    return output

test_input = [[97,100],[33,51],[89,100],[83,100],[75,92],[76,95],[19,30],[53,63],[8,23],[18,37],[87,100],[83,100],[54,67],[35,48],[58,75],[70,89],[13,32],[44,63],[51,62],[2,15]]
expected_output = [True, True, False, False, True, False, True, True, False, False, False, False, False, False, False, False, False, False, False, True]

output = running_a_test(test_input)

print(output)
assert output == expected_output
print("pass")
