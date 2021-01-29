from cryptography.fernet import Fernet
from random import randint

KEY = b'kMIWpzOlxwnyiPN9QfksxwgeCbwA8TYlR5zXdgEEudA='
F = Fernet(KEY)

# PASSWORDS SHOULD NOT BE STORED WITH THE <b''> part
# only the ACTUAL encrypted password in the middle
# BUT CONVERSION TO BYTES NEEDED FOR decrypt() FUNCTION

CHARS = list("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890")
# will store salt, pepper, and encrypted password with salt + pepper
def get_salt_pepper():
    salt_pepper = ""
    for i in range(12):
        salt_pepper += CHARS[randint(0, len(CHARS) - 1)]
    return salt_pepper

def encrypt(salt, pepper, passwd):
    token = F.encrypt(bytes("{}{}{}".format(salt, passwd, pepper), "utf-8"))
    
    # IN BYTES, still have to remove b''
    token = str(token)
    token = token.replace("b'", "")
    token = token.replace("'", "") # remove b''
    
    return token # IN STRING, b'' REMOVED

def decrypt(salt, pepper, token):
    # decrypted in bytes, need string
    decrypted_token = str(F.decrypt(token))
    # usually are in the format b'[password with salt and pepper]'
    # we have to remove <b''>
    decrypted_token = decrypted_token.replace(("b'" + salt), "")
    decrypted_token = decrypted_token.replace(pepper + "'", "")
    return decrypted_token

#pa = "gAAAAABf7ppkasdXj5aozvKMbOP4lvHdjQgfSxsImBRz1uu0TpSC67SQGmz8bysz1L_TTPqJ2EzLdd1GnDHc40q82cMpBhDIVdsHqJPFDBZkX1zCpqCiKkYU_1TVgupgrwa_UurA-k5e"
#print(decrypt("8m9QYMSjcILs", "UwJGt4DHZgKT", bytes(pa, "utf-8")))

#pa = str(encrypt("8m9QYMSjcILs", "UwJGt4DHZgKT", "password1")).replace("b'", "")
#pa = pa.replace("'", "")
#print(pa) # without b''