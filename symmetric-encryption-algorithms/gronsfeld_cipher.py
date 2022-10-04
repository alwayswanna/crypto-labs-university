# @author Abakshin-Bavitsky G.G
# БПИз-18-01

cryptMode = int(input('Доступные режимы: [1]-шифровать [2]-дешифровать: ').upper())
if cryptMode not in [1, 2]:
    raise Exception('Index out of bound. You must pres [1] or [2].')
start_message = input('Введите текст: ').upper()
key_number = input('Введите числовой ключ: ')

def gronsfeld_cipher(mode, message, key, result = ""):
    key *= len(message) // len(key) + 1
    for index, symbol in enumerate(message):
        if mode == 1:
            temp = ord(symbol) + int(key[index]) - 13
        else:
            temp = ord(symbol) - int(key[index]) - 13
        result += chr(temp%26 + ord('A'))
    return result
        
    
if __name__ == "__main__":
    print('Результат: ' + gronsfeld_cipher(cryptMode, start_message, key_number))