def pair_sum(arr,k):
    pair_count = 0
    num_count= {}

    for num in arr:
        element = k -num
        if element in num_count:
            pair_count += num_count[element]
        num_count[num] = num_count.get(num, 0) + 1

    return pair_count
arr =[1,2,3,4,5]
k = 6
pair_count = pair_sum(arr, k)

print("Pair count:", pair_count)