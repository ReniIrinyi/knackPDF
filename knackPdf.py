# -*- coding: utf-8 -*-
import PyPDF2
import itertools
from PyPDF2 import PdfReader

def crack_password(pdf_path, char_set, max_length):
    pdf_file = open(pdf_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    
    for length in range(1, max_length + 1):
        for pwd in itertools.product(char_set, repeat=length):
            try_password = ''.join(pwd)
            if pdf_reader.decrypt(try_password):
                return try_password
    return None

pdf_path = 'PATH_TO_YOUR_FILE'  
char_set = '0123456789XXAAA'  
max_length = 3  

password = crack_password(pdf_path, char_set, max_length)
if password:
    print('Passwort gefunden:')
    print(password)
else:
    print('Passwort nicht gefunden.')