x=3
lives=3
while lives>0:
    number=int(input("Enter a number: "))

    if  number == x:
        print("just right")
        break
    elif number < x:
        print("Too low!")
        lives=lives-1
    else:
        print("Too high!")
        lives=lives-1
    if lives == 0:
         print("Oops! No more lives left to guess.")