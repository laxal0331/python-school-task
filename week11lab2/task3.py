def simplify(instring):

    if len(instring) <= 1:
        return instring

    if instring[0] == instring[1]:
        return simplify(instring[1:])
    else:
        return instring[0] + simplify(instring[1:])
