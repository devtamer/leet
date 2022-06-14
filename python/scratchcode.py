# def foo(a,b,c,**args):
#     print(("a=%s") % (a,))
#     print("b=%s" % (b,))
#     print("c=%s" % (c,))
#     print("args=%s" % (args,))

# argdict = dict(a="testa", b="testb", c="testc", excessarg="string")
# foo(**argdict)

def count_bits(x: int) -> int:
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits

print(count_bits(10))

print(1000 >> 2)

nums = [i for i in range(1,1001)]
string = "Practice Problems to Drill List Comprehension in Your Head."

#finding numbers divisable by 8
print([num for num in nums if (num % 8 == 0)], "\n")

# finding numbers with 6 in them
print([num for num in nums if '6' in str(num)], "\n")

# count the number of spaces in a string
print(len([char for char in string if char == " "]))

# remove all of the vowels in a string
print("".join([char.replace('a', '').replace('e','').replace('i', '').replace('o','').replace('u', '') for char in string]))
print("".join([char for char in string if char not in ["a","e","i","o","u"]]))

# find all words that are less than five letters
splittxt = string.split(" ")
print(([char for char in splittxt if len(char) < 5]))

# use dict comprehension to count length of word in each sentence
q6_answer = {word:len(word) for word in splittxt}
print(q6_answer)
# using list comprehension
print([len(char) for char in splittxt])

# use a nested list compreh to find all numbers divisible my range(1-9)
print([num for num in nums if [True for divisor in range(2,10) if num % divisor == 0]])

# for all numbers use nested list/dict to find the highest single digit any of the numbers is divisible by
# print(max([num for num in nums if num % range(2,10) == 0]))
print({num:max([divisor for divisor in range(1,10) if num % divisor == 0]) for num in nums})
