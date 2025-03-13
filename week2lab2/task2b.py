year = int(input())
if year<2024:
 if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Year was a leap year")
        else:
            print("Year was not a leap year")
    else:
        print("Year was a leap year")
 else:
    print("Year was not a leap year")
else:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Year will be a leap year")
            else:
                print("Year will not be a leap year")
        else:
            print("Year will be a leap year")
    else:
        print("Year will not be a leap year")
