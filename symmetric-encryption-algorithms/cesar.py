# @author Abakshin-Bavitsky G.G
# БПИз-18-01

def cesar():
    result = ''
    print("Hi!")
    alpha = 'фищтршцкти - еъц эръшцщъд р щхцшцкти'
    n = int(input('Велечина сдвига = '))
    mode = int(input('Будем шифровать(1) или дешифровать (2) = '))
    s = input('Введите текст который терубется зашифровать или расшифровать = ')
    for c in s:
        if c in alpha:
            num = alpha.find(c)
            if mode == 1:
                num = num + n
            elif mode == 2:
                num = num - n
            if num >= len(alpha):
                num = num - len(alpha)
            elif num < 0:
                num = num + len(alpha)
            result = result + alpha[num]
        else:
            result = result + c
    print(result)
        
    
if __name__ == "__main__":
    cesar()