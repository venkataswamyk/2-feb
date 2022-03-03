#matrix multpilcation
m1 = [
    [1,2,3,4],
    [1,2,3,4],
    [1,2,3,4],
    [1,2,3,4],
]
m2 = [
    [4,3,2,1],
    [4,3,2,1],
    [4,3,2,1],
    [4,3,2,1],
]


pro =[]

res = []
for row in range(len(m1)):
    t = []
    for column in range(len(m2)):
        t.append(m2[column][row] * m1[row][column])
    res.append(t)

print(res)
