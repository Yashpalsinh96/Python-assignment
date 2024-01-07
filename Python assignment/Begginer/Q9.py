input_list=[1,2,3,2,4,1,2,4,5]
count ={}
for i in input_list:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print("freqency count:", count)