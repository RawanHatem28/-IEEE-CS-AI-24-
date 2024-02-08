def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
def get_days_in_month(month, year):
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    elif month in {4, 6, 9, 11}:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        return None
def get_tomorrows_date(day, month, year):
    days_in_month = get_days_in_month(month, year)
    if days_in_month is None:
        return None

    if day < days_in_month:
        return day + 1, month, year
    elif month < 12:
        return 1, month + 1, year
    else:
        return 1, 1, year + 1


day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
tomorrow_date = get_tomorrows_date(day, month, year)
if tomorrow_date is not None:
    print("Tomorrow's date:")
    print(f"Day : {tomorrow_date[0]}    Month: {tomorrow_date[1]}    Year: {tomorrow_date[2]}")
else:
    print("Invalid date input.")