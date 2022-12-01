#converting to  binary
from stack import Stack


def convert_int_to_bin(dec):
    if dec == 0:
        return 0

    s = Stack()

    while dec > 0:
        remainder = dec % 2
        s.push(remainder)
        #round
        dec = dec // 2

    bin = ""
    while not s.is_empty():
        bin += str(s.pop())

    return bin

print (convert_int_to_bin(242))