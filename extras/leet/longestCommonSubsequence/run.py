class Solution:
    def comp(array1, array2):
        # your code
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


a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
print(Solution.comp(a1, a2))
a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
print(Solution.comp(a1, a2))
a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
print(Solution.comp(a1, a2))
