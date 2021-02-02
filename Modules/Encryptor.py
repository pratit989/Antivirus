import pyAesCrypt
from OptionBox import option_box
from tkinter import filedialog

# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
file_name = '*'


def encrypt(file_path=filedialog.askopenfilename, output_path=filedialog.asksaveasfilename):
    global file_name
    ALLOPTION = dict(initialfile=file_name, filetypes=[('All Files', '*.*')])
    if file_path == filedialog.askopenfilename:
        file_path = file_path(**ALLOPTION)
        file_name = file_path.split('/')[-1]
    password = option_box(msg='Enter the password you want to set.',
                          b1='OK',
                          b2='Cancel',
                          frame=False,
                          entry=True,
                          t=False)
    AESOPTION = dict(defaultextension='.aes', initialfile=file_name + '.aes',
                     filetypes=[('AES File', '*.aes'), ('AES file', '*.aes')])
    output = output_path(**AESOPTION)
    pyAesCrypt.encryptFile(file_path, output, password, bufferSize)


def decrypt(file_path=filedialog.askopenfilename, output_path=filedialog.asksaveasfilename):
    global file_name
    AESOPTION = dict(defaultextension='.aes', initialfile=file_name + '.aes',
                     filetypes=[('AES File', '*.aes'), ('AES file', '*.aes')])
    if file_path == filedialog.askopenfilename:
        file_path = file_path(**AESOPTION)
        file_name = file_path.split('/')[-1].replace('.aes', '')
    password = option_box(msg='Enter file password',
                          b1='OK',
                          b2='Cancel',
                          frame=False,
                          entry=True,
                          t=False)
    ALLOPTION = dict(initialfile=file_name, filetypes=[('All Files', '*.*')])
    output = output_path(**ALLOPTION)
    pyAesCrypt.decryptFile(file_path, output, password, bufferSize)
