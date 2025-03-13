x=int(input())
y=int(input())
operator = input()
if operator == "+":
        print(x+y)
elif operator =="-":
        print(x-y)
elif operator =="*":
        print(x*y)
elif operator =="/":
  if y == 0:
            print("cannot divide by zero")
  else:
            print(x/y)
else:
        print("invalid operator")