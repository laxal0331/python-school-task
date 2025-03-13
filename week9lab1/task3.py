a = open("Class.csv", "r")
lstc = a.readlines()
total=0
num=0
count=0
for x in range(len(lstc)-1):
    name, num = lstc[x+1].split(",")
    total += int(num[:-2])
    count += 1
print("Average mark:", total/count)
