# @author Abakshin-Bavitskii G.G
# БПИз-18-01
table = [[4, 10, 9, 2, 13, 8, 0, 14, 6, 11, 1, 12, 7, 15, 5, 3],
         [14, 11, 4, 12, 6, 13, 15, 10, 2, 3, 8, 1, 0, 7, 5, 9],
         [5, 8, 1, 13, 10, 3, 4, 2, 14, 15, 12, 7, 6, 0, 9, 11],
         [7, 3, 10, 1, 0, 8, 9, 15, 14, 4, 6, 12, 11, 2, 5, 3],
         [6, 12, 7, 1, 5, 15, 13, 8, 4, 10, 9, 14, 0, 3, 11, 2],
         [4, 11, 10, 0, 7, 2, 1, 13, 3, 6, 8, 5, 9, 12, 15, 14],
         [13, 11, 4, 1, 3, 15, 5, 9, 0, 10, 14, 7, 6, 8, 2, 12],
         [1, 15, 13, 0, 5, 7, 10, 4, 9, 2, 3, 14, 6, 11, 8, 12]]

def to_ascii(c):
    num = ord(c)
    if num > 1039:
        return num - 848
    return num

def to_letter(c):
    if c > 191:
        return chr(c + 848)
    return chr(c)

def to_binary(n):
    return [int(d) for d in "{0:08b}".format(n)]

def addMod32(a, k):
    a = str.join('', list(map(str, a[0]))) + str.join('', list(map(str, a[1])))\
        + str.join('', list(map(str, a[2]))) + str.join('', list(map(str, a[3])))
    k = str.join('', list(map(str, k[0]))) + str.join('', list(map(str, k[1])))\
        + str.join('', list(map(str, k[2]))) + str.join('', list(map(str, k[3])))
    a1 = int(a, 2)
    k1 = int(k, 2)
    b1 = bin(a1 + k1)
    return b1[-32:]

def getReplace(i, num):
    a = int(num, 2)
    return "{0:04b}".format(table[i][a])

def shift11(s):
    s = list(s)
    for i in range(11):
        s.append(s.pop(0))
    return [str.join('', s[0:8]), str.join('', s[8:16]), str.join('', s[16:24]), str.join('', s[24:32])]

def xorSB(s, b):
    s = int(s, 2)
    b = int(b, 2)
    return "{0:08b}".format(s ^ b)

# @author Abakshin-Bavitskii G.G
# БПИз-18-01
text = "Одна пчела немного меду натаскает"
while len(text) % 8 != 0:
    text += ' '
key = "шмель"
key_l = len(key)
while len(key) < 32:
    key += key[len(key) % key_l]

print(text, len(text))
print(key)

for r in range(32):
    for i in range(len(text) // 8):
        A = list(reversed(text[(8 * i) : (8 * i) + 4]))
        B = list(reversed(text[(8 * i) + 4 : (8 * i) + 8]))
        BA = list(map(to_binary, list(map(to_ascii, A))))
        BB = list(map(to_binary, list(map(to_ascii, B))))
        K = list(reversed(key[4 * i : 4 * i + 4]))
        BK = list(map(to_binary, list(map(to_ascii, K))))

        S = addMod32(BA, BK)
        S0 = getReplace(0, S[28:32])
        S1 = getReplace(1, S[24:28])
        S2 = getReplace(2, S[20:24])
        S3 = getReplace(3, S[16:20])
        S4 = getReplace(4, S[12:16])
        S5 = getReplace(5, S[8:12])
        S6 = getReplace(6, S[4:8])
        S7 = getReplace(7, S[0:4])
        S = S7 + S6 + S5 + S4 + S3 + S2 + S1 + S0

        S = shift11(str.join('', S))

        X3 = xorSB(S[3], str.join('', list(map(str,BB[3]))))
        X2 = xorSB(S[2], str.join('', list(map(str,BB[2]))))
        X1 = xorSB(S[1], str.join('', list(map(str,BB[1]))))
        X0 = xorSB(S[0], str.join('', list(map(str,BB[0]))))
        X = [int(X0, 2), int(X1, 2), int(X2, 2), int(X3, 2)]

        for j in range(8 * i + 4, 8 * i + 8):
            text = text[:j-4] + text[j - 4] + text[j-3:]
        for j in range((8 * i) + 4, (8 * i) + 8):
            text = text[:j] + to_letter(X[j - (8 * i) - 4]) + text[j+1:]
        t = list(text[8*i:8*i+8])
        t = list(reversed(t[4:8])) + t[0:4]
        text = text[:8*i] + str.join('', t) + text[8*i+8:]

print('Result: ' + text)
print((list(map(ord, text))))
