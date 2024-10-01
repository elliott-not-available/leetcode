from design_circular_deque_641 import MyCircularDeque

def runner(arg_list: list[str], input_list: list[list]) -> tuple[list, MyCircularDeque]:
    output = []

    dq = MyCircularDeque(input_list[0][0])

    for a, i in zip(arg_list[1:], input_list[1:]):
        print(a, i)
        if i:
            i=i[0]
            output.append(getattr(dq, a)(i))
        else:
            output.append(getattr(dq, a)())

    return output, dq


args = ["MyCircularDeque","insertFront","insertLast","getFront","insertLast","getFront","insertFront","getRear","getFront","getFront","deleteLast","getRear"]
inps = [[5],[7],[0],[],[3],[],[9],[],[],[],[],[]]

args2= ["MyCircularDeque","insertFront","deleteLast","getRear","getFront","getFront","deleteFront","insertFront","insertLast","insertFront","getFront","insertFront"]
inps2 = [[4],[9],[],[],[],[],[],[6],[5],[9],[],[6]]

args3 = ["MyCircularDeque","insertFront","getRear","deleteLast","getRear","insertFront","insertFront","insertFront","insertFront","isFull","insertFront","isFull","getRear","deleteLast","getFront","getFront","insertLast","deleteFront","getFront","insertLast","getRear","insertLast","getRear","getFront","getFront","getFront","getRear","getRear","insertFront","getFront","getFront","getFront","getFront","deleteFront","insertFront","getFront","deleteLast","insertLast","insertLast","getRear","getRear","getRear","isEmpty","insertFront","deleteLast","getFront","deleteLast","getRear","getFront","isFull","isFull","deleteFront","getFront","deleteLast","getRear","insertFront","getFront","insertFront","insertFront","getRear","isFull","getFront","getFront","insertFront","insertLast","getRear","getRear","deleteLast","insertFront","getRear","insertLast","getFront","getFront","getFront","getRear","insertFront","isEmpty","getFront","getFront","insertFront","deleteFront","insertFront","deleteLast","getFront","getRear","getFront","insertFront","getFront","deleteFront","insertFront","isEmpty","getRear","getRear","getRear","getRear","deleteFront","getRear","isEmpty","deleteFront","insertFront","insertLast","deleteLast"]
inps3 = [[77],[89],[],[],[],[19],[23],[23],[82],[],[45],[],[],[],[],[],[74],[],[],[98],[],[99],[],[],[],[],[],[],[8],[],[],[],[],[],[75],[],[],[35],[59],[],[],[],[],[22],[],[],[],[],[],[],[],[],[],[],[],[21],[],[26],[63],[],[],[],[],[87],[76],[],[],[],[26],[],[67],[],[],[],[],[36],[],[],[],[72],[],[87],[],[],[],[],[85],[],[],[91],[],[],[],[],[],[],[],[],[],[34],[44],[]]

o, dq = runner(args, inps)

print(o)
print(dq.list)


## example with callables instead of getattibes
# dq = MyCircularDeque(k=5)

# me_functions = {
#     "insertFront": dq.insertFront,
#     "insertLast": dq.insertLast,
#     "getFront": dq.getFront,
#     }

# arg = ["insertFront", "insertLast", "getFront"]

# inp = [[2], [5], []]

# output = []

# for a,i in zip(arg, inp):

#     if i:
#         i=i[0]
#         output.append(me_functions[a](i))
#     else:
#         output.append(me_functions[a]())

# print(output)


