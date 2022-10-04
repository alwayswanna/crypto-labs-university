# @author Abakshin-Bavitsky G.G
# БПИз-18-01


alplabet = [chr(x) for x in range(65, 122)]

crypt_alplabet = (
    ')', '[','!',',',';','{',':', '*','^','/','!','[', ')', 
    '[', ']', '^', '/', '!', ')', '[', '!', ';',':','+', ',',
    '!', '&', ';', '{', '/', '!',',', '^', '@','/','[', '!', ';', '+', '%'
)


def replacement_cipher():
    result = ''
    dial = int(input('Будем шифровать (1) или дешифровать (2) = ').upper())
    if dial not in [1, 2]:
        raise Exception('Index out of bound. You must pres [1] or [2].')
    message = input('Введите текст который требуется зашифровать или расшифровать: ')
    keys = dict(zip(alplabet, crypt_alplabet))
    if dial == 1:
        for symbol in message:
            if symbol in keys:
                result += keys[symbol]
    else:
        for symbol in message:
            for key in keys: 
                if symbol == keys[key]: result += key
    
    print('Результат: ' +result)
        
    
if __name__ == "__main__":
    replacement_cipher()