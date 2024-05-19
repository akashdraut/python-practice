def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    

year = int(input("Enter year to check: "))
if is_leap_year(year):
    print(f"Given year {year} is leap year")
else:
    print(f"Given year {year} is not leap year")
