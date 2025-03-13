def   speed_dial_v1(contact_list):
  sd_name, sd_number, sd_freq = contact_list.pop()
  while  len(contact_list)  >  0:
    name, number, freq = contact_list.pop()
    if  freq  > sd_freq:
        sd_name, sd_number, sd_freq = name, number, freq
  return  (sd_name, sd_number)

# sd_name = 'Abe'
# sd_number = '03#'
# sd_freq = 4
# contact_list = [('Buffy', '04#', 5), ('Blade', '04#', 2)]
# while len(contact_list) > 0:
# Pop ('Blade', '04#', 2), update contact_list = [('Buffy', '04#', 5)]
# name = 'Blade', number = '04#', freq = 2
# if freq > sd_freq:  2 > 4, condition is false, skip.
# Pop ('Buffy', '04#', 5), update contact_list = []
# name = 'Buffy', number = '04#', freq = 5
# if freq > sd_freq:  5 > 4, condition is true, update:
# sd_name = 'Buffy'
# sd_number = '04#'
# sd_freq = 5
# return (sd_name, sd_number)
# Return ('Buffy', '04#')

def   speed_dial_v2(contact_list):
  sd_name, sd_number, sd_freq = contact_list[0]
  for   contact   in contact_list:
        name, number, freq = contact
        if  freq  >  sd_freq:
            sd_name, sd_number, sd_freq = name, number, freq
  return  (sd_name, sd_number)

# sd_name = 'Tiffany'
# sd_number = '04#'
# sd_freq = 5
# for contact in contact_list:
# contact = ('Tiffany', '04#', 5), no change.
# contact = ('Hermione', '07#', 2)
# if freq > sd_freq: 2 > 5, condition is false, no update.
# contact = ('Morgan', '00#', 4)
# if freq > sd_freq: 4 > 5, condition is false, no update.
# return (sd_name, sd_number)
# Return ('Tiffany', '04#')


# 1.
list1=[('Buffy', '04#', 5),('Blade', '04#', 2),('Abe','03#', 4)]
x=speed_dial_v1(list1)
print(x)
# x = ('Buffy', '04#')
list2=[('Tiffany', '04#', 5),('Hermione', '07#', 2),('Morgan', '00#', 4)]
y=speed_dial_v2(list2)
print(y)
# y = ('Tiffany', '04#')

# 2.
#speed_dial_v2 is  better, because it does not modify the input list,
# and more efficient.
