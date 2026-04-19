import re
import random
import string

def buat_password():
    karakter = string.ascii_letters + string.digits
    return ''.join(random.choices(karakter, k =8))
def cari_email(teks):
    pola = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    temukan_email = re.findall(pola, teks)

    for email in temukan_email:
        username  = email.split('@')[0]
        password = buat_password()
        print(f"username: {username}, password: {password}")

teks = input("masukkan teks: ")
cari_email(teks)