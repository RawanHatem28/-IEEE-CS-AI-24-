# problem 1
num_list = []
while True:
    num = int(input())
    if num != -1:
       num_list.append(num)
    else:
        print(max(num_list))
        print(min(num_list))
        break