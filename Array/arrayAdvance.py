"""Is it possible to advance from the start of the array to the last element given that the maximum you can advance from a position is based on the value of the array at the index you are currently present on?"""

def array_advance(A):
    reached = 0
    last_idx = len(A) - 1
    i = 0
    while i <= reached and reached < last_idx:
        reached = max(reached, A[i] + i)
        i += 1
    return reached >= last_idx


# returns True
# Moves: 1,3,2
A = [3, 3, 1, 0, 2, 0, 1]
print(array_advance(A))

# returns False
A = [3, 2, 0, 0, 2, 0, 1]
print(array_advance(A))