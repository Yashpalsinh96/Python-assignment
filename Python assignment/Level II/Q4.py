arr = [1, 2, 3, 4, 5]
D = 2

n = len(arr)
D = D % n

arr[D:] = reversed(arr[D:])
arr[:D] = reversed(arr[:D])

arr.reverse()

print("arr after rotation:", arr)
