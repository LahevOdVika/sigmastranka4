from cryptography.fernet import Fernet

def generateKey():
    key = Fernet.generate_key()
    with open('misc_files\\key', 'wb') as key_file:
        key_file.write(key)
    return key

def loadKey():
    try:
        with open('misc_files\\key', 'rb') as key_file:
            return key_file.read()
    except FileNotFoundError:
    except FileNotFoundError:
        raise FileNotFoundError("Key file not found. Please generate a key first.")

def encrypt(message: str, key: bytes = None):
    if key is None:
        key = loadKey()
    f = Fernet(key)
    return f.encrypt(message)

def decrypt(message: bytes, key: bytes = None):
    if key is None:
        key = loadKey()
    f = Fernet(key)
    try:
        data = [message[1], message[2], message[3], message[4]]
        newData = [message[0]]
        for i in data:
            newData.append(f.decrypt(i).decode('utf-8'))
        return newData
    except Exception as e:
        raise Exception(f"Decryption failed: {str(e)}")

if __name__ == '__main__':
    inputStr = input("> ")
    try:
        print(encrypt(inputStr))
    except Exception as e:
        print(f"Error: {str(e)}")
