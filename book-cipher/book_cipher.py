from random import choice
from re import findall

# @author Abakshin-Bavitsky GG
# БПИз-18-01
def regular(txt):
    template = r"[0-9]+"
    return findall(template, txt)

def encryptDecrypt(mode, message, key, result = ""):
    with open(key) as bookKey:
        book = bookKey.read()
    if mode == 1:
        for symbolMessage in message:
            listIndexKey = []
            for indexKey, symbolKey in enumerate(book):
                if symbolMessage == symbolKey:
                    listIndexKey.append(indexKey)
            try: result += str(choice(listIndexKey)) + '/'
            except IndexError: pass
    else:
        for numbers in regular(message):
            for indexKey, symbolKey in enumerate(book):
                if numbers == str(indexKey):
                    result += symbolKey
    return result

if __name__ == "__main__":
    cryptMode = int(input('[1] - Шифровать | [2] - Дешифровать '))
    if cryptMode not in [1, 2]:
        raise Exception("Input option does not exist.")
    startMessage = input('Введите текст: ')
    bookKey = input('Введите книгу-ключ: ')
    print("Результат работы: ", encryptDecrypt(cryptMode, startMessage, bookKey))
    
