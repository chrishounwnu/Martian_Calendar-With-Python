def mars(day, month, year):
    
    days_per_month_non_leap = [28, 28, 28, 28, 28, 27]
    days_per_month_leap = [28, 28, 28, 28, 28, 27]
    days_in_non_leap_year = 668
    days_in_leap_year = 669
    base_day, base_month, base_year = 28, 24, 220 
    base_weekday = 1  # Monday = 1

    
    def is_leap_year(y):
        return y % 2 == 1 or y % 10 == 0

    # Validate the input date
    if not (1 <= day <= 28 and 1 <= month <= 24 and year >= 1):
        return -1
    month_days = days_per_month_leap if is_leap_year(year) else days_per_month_non_leap
    if day > month_days[(month - 1) % 6]:
        return -1

    
    total_days = 0
    if year > base_year:
        for y in range(base_year, year):
            total_days += days_in_leap_year if is_leap_year(y) else days_in_non_leap_year
    elif year < base_year:
        for y in range(year, base_year):
            total_days -= days_in_leap_year if is_leap_year(y) else days_in_non_leap_year

    
    if year == base_year:
        if month > base_month:
            for m in range(base_month, month):
                total_days += month_days[(m - 1) % 6]
        elif month < base_month:
            for m in range(month, base_month):
                total_days -= month_days[(m - 1) % 6]
    else:
        for m in range(1, month):
            total_days += month_days[(m - 1) % 6]
        base_month_days = days_per_month_leap if is_leap_year(base_year) else days_per_month_non_leap
        for m in range(1, base_month):
            total_days -= base_month_days[(m - 1) % 6]

    
    total_days += (day - base_day)

    
    weekday = (base_weekday + total_days) % 7
    return weekday if weekday >= 0 else weekday + 7


#################   DO NOT CHANGE BELOW ###########################

def run_code(name):
    fin = open(name, 'r')
    fout = open('datasets/mars/mars_sol.out', 'w')
    n_tests = int(fin.readline())
    for i in range(n_tests):
        d, m, y = map(int, fin.readline().split('.'))
        fout.write('%d\n' % mars(d, m, y))
    fin.close()
    fout.close()
