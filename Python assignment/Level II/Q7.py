number_list = [7,2,5,1,9,3]
num = len(number_list)
number_list.sort()

if num % 2 == 0:
    median1 = number_list[num//2]
    median2 = number_list[num//2-1]
    median = (median1 + median2)/2
else: 
    median = number_list[num//2]

print("Median: ", str(median))