start=input()
end=input()
step=input()
total=0
if int(end)>=0:
 for i in range(int(start),int(end)+1,int(step)):
     total = total + i
else:
 for i in range(int(start), int(end)-1, int(step)):
     total = total + i
print(total)