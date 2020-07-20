year = int(input("Please enter a 4-digit Gregorian calendar year..:"))

c1 = year % 4
c2 = year % 100
c3 = year % 400

leap = f"{year} is a leap year."
not_leap = f"{year} is NOT a leap year."

if c1 == 0:
    if c2 == 0:
        if c3 == 0:
            print(leap)
        else:
            print(not_leap)
    else:
        print(leap)
else:
    print(not_leap)