import rsa

# @author Abakshin-Bavitsky G.G
# БПИз-18-01
def rsa_test():
    (public_key, private_key) = rsa.newkeys(512)
    print(str('Public key: ' + str(public_key)) + "\n\n" + str('Private key: ' + str(private_key)))

    user_message = input('Input message: ').encode("utf8")
    crypto = rsa.encrypt(user_message, public_key)
    message = rsa.decrypt(crypto, private_key)

    print("userMessage is: " + str(user_message))
    print("RSA crypt: " + str(crypto))
    print("RSA decrypt: " + str(message))

if __name__ == "__main__":
    rsa_test()