# problem 6
num = int(input())
if num <= 0:
    print("Please Enter Positive Number")
else:
    i = 0
    sum = 0
    while i <= num:
        sum += i
        i += 2
print(f"The sum of even numbers from 1 to {num} is {sum}")