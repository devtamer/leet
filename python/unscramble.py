# "emwtafsdoaraisle" ----> "tamer elsawaf"
# do the characters exist given the input string
import copy

def unscramble(word, chars):
    if len(word)==0 or len(chars)==0:
        return 0
    max_count = 0
    for word in word:
        tmp_chars = copy.deepcopy(chars)
        tmp_chars = list(tmp_chars)
        cnt = 0
        for char in word:
            if char in tmp_chars:
               idx = tmp_chars.index(char)
               tmp_chars[idx] = ''
               cnt += 1
            else:
                cnt = 0
                break
        max_count += cnt
    if (max_count // len(word) == 1):
        return("the word {} exists within the chars".format(word))
    else:
        return("word cannot be found in chars")

word = ["tamerelsawaf"]
chars = "emwtafsdoaraisle"
print(unscramble(word, chars))