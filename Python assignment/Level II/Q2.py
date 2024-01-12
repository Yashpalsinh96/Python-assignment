def unique_elements (input_list):
    
    unique_list = set(input_list)
    unique_list = list(unique_list)

    return unique_list

list1 = [1,2,2,3,4,4,5,5]
list2 = unique_elements(list1)

print ("unique element", list2)