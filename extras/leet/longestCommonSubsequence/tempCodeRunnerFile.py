    array1.sort()
        array2.sort()
        output = False
        for i in array1:
            num = i * i
            for j in array2:
                if j == num:
                    output = True
                else:
                    output = False
        return output