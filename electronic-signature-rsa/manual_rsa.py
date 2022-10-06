from this import d

# @author Abakshin-Bavitsky G.G
# БПИз-18-01
def generate_keys_parts(a, b):
    if b > a:
        if b % a == 0:
            return a
        else: return generate_keys_parts(b % a, a)
    else:
        if a % b == 0:
            return b
        else: return generate_keys_parts(b, a % b)
        
def find_d(phi_n, e):
    k = 1
    mod0 = False
    while not mod0:
        d, rem = divmod(k * phi_n + 1, e)
        if rem == 0:
            return d
        k += 1
        
def find_e(phi_n):
    e = 3
    while True:
        if not generate_keys_parts(e, phi_n) == 1:
            e += 2
        else: return e

def generate_keys(p1, p2):
    global n, e, d
    n = p1 * p2
    phi_n = (p1 - 1)*(p2 - 1)
    e = find_e(phi_n)
    d = int(find_d(phi_n, e))
    return ((e, n), (d, n))

def generate_rsa_signature():
    alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    sp = []; res = ''
    p = int(input('Введите p = '))
    q = int(input('Введите q = '))
    generate_keys(p, q)
    s = input('Введите текст для шифрования = ').strip()
    for c in s:
        if c in alpha:
            num = alpha.find(c)
            num1 = int((num ** e) % n)
            sp.append(num1)
            res = res + str(num1)
        else: 
            print("Данная буква отстутствует в алфавите: " + c.__str__)
            break
    print('Результат: ', sp)

if __name__ == "__main__":
    generate_rsa_signature()