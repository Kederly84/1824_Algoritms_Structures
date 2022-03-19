class makeConnected:

    def __init__(self, n: int):
        self.parent = [0] * n
        for i in range(n):
            self.parent[i] = i
        self.counter = 0

    def union(self, x, y):
        t1 = self.find(x)
        t2 = self.find(y)
        if t1 == t2:
            self.counter += 1
            return
        self.parent[t1] = t2

    def find(self, x):
        # print(self.parent[x], x)
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # def print(self):
    #     print(self.parent)


a = makeConnected(4)
connections = [[0, 1], [0, 2], [1, 2]]

for con in connections:
    a.union(con[0], con[1])

ans = []
for _ in a.parent:
    if _ not in ans:
        ans.append(_)

if a.counter >= len(ans) - 1:
    print(len(ans) - 1)
else:
    print(-1)

# a.print()
# print(ans)
