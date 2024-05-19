
def calculate_year_weeks_days(num):
    years = num // 365
    remaining_days = num % 365
    weeks = remaining_days // 7
    days = remaining_days % 7

    return years, weeks, days

num = int(input("Enter number of days: "))
y, w, d = calculate_year_weeks_days(num)
print("year: ", y, ", weeks: ", w, ", days: ", d)

