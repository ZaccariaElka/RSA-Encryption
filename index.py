import math

def encryption(text):

    number_1 = 11
    number_2 = 13

    n = number_1 * number_2 #the rsa encryption module
    phi = (number_1 - 1) * (number_2 - 1)

    e = 17

    if math.gcd(e, phi) == 1: #check if the greatest common divisor is 1
        print(math.gcd(e,phi))
    else:
        print("the gcd must be 1")
        return
    
    d = 113

    if (e * d) % phi == 1: #check if d is a multiplicative intense to e
        print(f"{(e * d) % phi}")
    else:
        print("pick another number for d")
        return 

    private_key = [n, d]
    public_key = [n, e]

    message = text
    encrypted_message = []

    for char in message:
        m = ord(char) #convert every character to ASCII value
        if m >= 0 and m <= n: #check if m is within the range of 0 and n
            c = pow(m, public_key[1], public_key[0]) #encryption
            encrypted_message.append(c)
        else:
            print(f"{char} with {m} is out of range")
            return
        
    return encrypted_message, public_key, private_key

def decryption(encrypted_message, private_key):

    decrypted_message = ''
    n, d = private_key

    for num in encrypted_message:
        m = pow(num, d, n)  #decryption
        decrypted_message += chr(m)  #convert ASCII value to character

    return decrypted_message
    

text = "Mississippi"
text_encrypted = encryption(text)
print(text_encrypted) #mississippi = [77, 118, 124, 124, 118, 124, 124, 118, 73, 73, 118]

result = encryption(text)

if result:
    encrypted_message, public_key, private_key = result

    print("Encrypted:", encrypted_message) #[77, 118, 124, 124, 118, 124, 124, 118, 73, 73, 118]
    print("Public Key:", public_key) #[143, 17]
    print("Private Key:", private_key) #[143, 113]

    decrypted_message = decryption(encrypted_message, private_key)
    print("Decrypted:", decrypted_message) #Mississippi
