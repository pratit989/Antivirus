import pyAesCrypt
from OptionBox import option_box
from tkinter import filedialog

# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
file_name = '*'


def encrypt(file_path=filedialog.askopenfilename, output_path=filedialog.asksaveasfilename):
    global file_name
    allOption = dict(initialfile=file_name, filetypes=[('All Files', '*.*')])
    if file_path == filedialog.askopenfilename:
        file_path = file_path(**allOption)
        file_name = file_path.split('/')[-1]
    password = option_box(msg='Enter the password you want to set.',
                          b1='OK',
                          b2='Cancel',
                          frame=False,
                          entry=True,
                          t=False)
    aesOption = dict(defaultextension='.aes', initialfile=file_name + '.aes',
                     filetypes=[('AES File', '*.aes'), ('AES file', '*.aes')])
    output = output_path(**aesOption)
    pyAesCrypt.encryptFile(file_path, output, password, bufferSize)


def decrypt(file_path=filedialog.askopenfilename, output_path=filedialog.asksaveasfilename):
    global file_name
    aesOption = dict(defaultextension='.aes', initialfile=file_name + '.aes',
                     filetypes=[('AES File', '*.aes'), ('AES file', '*.aes')])
    if file_path == filedialog.askopenfilename:
        file_path = file_path(**aesOption)
        file_name = file_path.split('/')[-1].replace('.aes', '')
    password = option_box(msg='Enter file password',
                          b1='OK',
                          b2='Cancel',
                          frame=False,
                          entry=True,
                          t=False)
    allOption = dict(initialfile=file_name, filetypes=[('All Files', '*.*')])
    output = output_path(**allOption)
    pyAesCrypt.decryptFile(file_path, output, password, bufferSize)
