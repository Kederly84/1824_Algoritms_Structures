# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2x.

task1 = 1
task2 = 16
task3 = 3



def cheker(x: int):
    if x == 2 or x == 1:
        return True
    elif x % 2 != 0:
        return False
    else:
        return cheker(x // 2)



print(cheker(task1))
print(cheker(task2))
print(cheker(task3))