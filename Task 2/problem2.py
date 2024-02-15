def is_leap(year):
    leap = False
    if year > 0:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            leap = True
        else:
            leap = False
    else:
        print("please enter exact year number")
    return leap


year = int(input())
if is_leap(year):
    print(f"{year} Is a Leap Year")
else:
    print(f"{year} Is not a Leap Year")
