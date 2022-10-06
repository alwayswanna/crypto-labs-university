import rsa

# @author Abakshin-Bavitsky G.G
# БПИз-18-01
def generate_signature():
    (public_key, private_key) = rsa.newkeys(512)

    user_message = input('Введите текст: ').encode("utf8")
    crypto_message = rsa.encrypt(user_message, public_key)
    decrypted_message = rsa.decrypt(crypto_message, private_key)

    signature = rsa.sign(decrypted_message, private_key, 'SHA-1')

    rsa.verify(decrypted_message, signature, public_key)
    message = input('Проверочный текст: ').encode("utf8")

    if rsa.verify(message, signature, public_key):
        print('Подпись подтверждена')
        
if __name__ == "__main__":
    generate_signature()