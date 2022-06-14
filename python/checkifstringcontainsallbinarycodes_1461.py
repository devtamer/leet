def hasAllCodes(s, k):
    d = []
    if k == 2:
        d.append(('00','01','10','11'))
    # split = [x for word in d for x in word.split(',')]
    print([x in d for x in '22'])
    found = s.find(str(k))
    return found



print(hasAllCodes(s = "00110110", k = 2))