new_string=""
my_string= 'hare paws wall tuba draw'
for i in range(len(my_string)):
    if my_string[i]=='a':
        new_string+='e'
    else:new_string += my_string[i]
print(new_string)