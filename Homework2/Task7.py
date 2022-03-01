# Write a function that reverses a string. The input string is given as an array of characters s.

task1 = ["h", "e", "l", "l", "o"]
task2 = ["H", "a", "n", "n", "a", "h"]


def reverse(s: list):
    ksat = []
    def helper(x: list, z: int):
        if z >= len(x):
            return
        helper(x, z + 1)
        ksat.append(x[z])
    helper(s, 0)
    return ksat


print(reverse(task1))
print(reverse(task2))
