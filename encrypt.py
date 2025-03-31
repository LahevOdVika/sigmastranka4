from cryptography.fernet import Fernet

def generateKey():
    key = Fernet.generate_key()
    with open('misc_files\key', 'wb') as key_file:
        key_file.write(key)
    return key

def loadKey():
    return open('misc_files\key', 'rb').read()

def encrypt(message: str, key: str= loadKey()):
    f = Fernet(key)
    return f.encrypt(message)

if __name__ == '__main__':
    inputStr = input("> ")
    print(encrypt(inputStr.encode('utf-8')))