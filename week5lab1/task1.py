def my_abs(num):
    if num < 0:
        return -num
    else:
        return num

def my_sum(lst):
    total = 0.0
    for number in lst:
        total+=number
    return total

def my_is_in(char,string):
    for a in string:
        if a == char:
            return True
    return False

def my_any(lst):
    for b in lst:
        if bool(b):
            return True
    return False

