# List indexing and slicing
L = [2, 3, 5, 7, 11]
print(L[2])
print(L[1])

print(L[-1])
print(L[-2])

print(L[0:3])
print(L[:3])

print(L[-3:])
print(L[:-3])

print(L[0:len(L)-1:2])
print(L[::-1])

L[0] = 100
print(L)
L[1:3] = [55, 56]
print(L)
