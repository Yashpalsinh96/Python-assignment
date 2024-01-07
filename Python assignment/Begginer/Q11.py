num = int(input())
sum_of_digits = 0

while num>0 or sum_of_digits>=10:
    if num == 0:
       print(sum_of_digits)
       num = sum_of_digits
       sum_of_digits =0
    sum_of_digits += num % 10
    num //= 10
print(sum_of_digits)