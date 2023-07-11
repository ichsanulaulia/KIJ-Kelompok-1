import math

def encrypt(m, e, n):
    return pow(m,e,n)

s = "123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def to_ascii(text):
    ascii_values = [ord(character) for character in text]
    return ascii_values

def listToString(s):
    # initialize an empty string
    str1 = "" 
    # traverse in the string  
    for ele in s: 
        # str1 += str(ele)
        print(ele)
    # return string  
    return str1

def split2len(s, n):
    def _f(s, n):
        while s:
            yield s[:n]
            s = s[n:]
    return list(_f(s, n))

h = [95, 104, 104]

def toChar(text):
    result = ""
    for idx in text:
        result += chr(idx)
        # print(idx)
    return result

def split2Ascii(text):
    result = list()
    i = 0
    while i < len(text):
        if(text[i] == '1'):
            result.append(text[i:i+3])
            i+=3
        else:
            result.append(text[i:i+2])
            i+=2
    return result

# print(listToString(to_ascii(s)))

# print(to_ascii(s))
# print(toChar(to_ascii(s)))
# print(split2len(s, 2))

# print(encrypt(3,79,3337))

print(split2Ascii(s))