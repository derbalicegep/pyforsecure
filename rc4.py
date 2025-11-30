
# Online Python - IDE, Editor, Compiler, Interpreter
from Crypto.Cipher import ARC4
import binascii
	
def decrypt_rc4(cipher_hex, key):
    """
    Decrypts a hex-encoded ciphertext using RC4 with a given key.
    """
    # Convert the hex string to bytes
    cipher_bytes = bytes.fromhex(cipher_hex)

    # Create an RC4 cipher object
    cipher = ARC4.new(key.encode())

    # Decrypt the message
    decrypted_bytes = cipher.decrypt(cipher_bytes)

    # Convert decrypted bytes to a string
    return decrypted_bytes.decode('utf-8', errors='ignore')
	
# Ciphertext in hexadecimal format
ciphertext_hex = "afdd793b510967cd50af8324bcf19c335ad046ec"
	
# Key
key = "KAREEM"
	
# Decrypt the message
original_message = decrypt_rc4(ciphertext_hex, key)
print(f"Message original : {original_message}") # Mission Accomplished
