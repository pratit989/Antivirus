import tkinter as tk
from tkinter import filedialog

from Modules.VirusAPI import scan
from OptionBox import option_box
from os import remove

filePath = ''
func_selected = ''


def option_selector():
    from Modules.Encryptor import encrypt
    from Modules.Encryptor import decrypt
    global func_selected
    func_selected = option_box(msg='Do you want to encrypt or decrypt the file?',
                               b1=('encrypt', encrypt),
                               b2=('decrypt', decrypt),
                               frame=False,
                               entry=False,
                               t=False)
    clear_entry_box()
    if filePath != '':
        func_selected(file_path=filePath)
    else:
        func_selected()


# File Browse Function
def browse_function():
    global filePath
    filePath = filedialog.askopenfilename()
    try:
        enter_path.insert(tk.END, filePath)
        print(filePath)
    except NameError:
        pass


# Scan Function
def scan_call():
    scan(filePath)
    clear_entry_box()


# Delete Function
def delete_call():
    remove(filePath)
    print(f'Successfully deleted {filePath}')


# Clear entry box
def clear_entry_box():
    sentence = enter_path.get()
    enter_path.delete(0, len(sentence))


window = tk.Tk()
# Background of window
window.configure(background='#161b22')
window.geometry("860x140")
# Title of the window
window.title('VFree Antivirus')
# Enter file path label
Label1 = tk.Label(window,
                  justify=tk.LEFT,
                  fg='#58a6ff',
                  bg='#161b22',
                  padx=15,
                  text='Select File to Scan:',
                  font="Helvetica 16 bold").grid(row=1, column=1)
# Path Entry Box
enter_path = tk.Entry(window,
                      font=40,
                      highlightbackground='#161b22',
                      highlightcolor='#161b22',
                      highlightthickness=5,
                      relief=tk.FLAT,
                      width=50)
enter_path.grid(row=1, column=2)

# Path entry button
button1 = tk.Button(window,
                    text="Open",
                    font="Helvetica 13 bold",
                    command=browse_function,
                    background='#21262d',
                    foreground='white',
                    activeforeground='white',
                    activebackground='#32373e')
button1.grid(row=1, column=3)

# Scan Button
button2 = tk.Button(window,
                    text="Scan",
                    font="Helvetica 13 bold",
                    command=scan_call,
                    background='#21262d',
                    foreground='white',
                    activeforeground='white',
                    activebackground='#32373e',
                    width=40)
button2.place(rely='0.35', relx='0.02')

# Encrypt Button
button3 = tk.Button(window,
                    text="Encrypt / Decrypt",
                    font="Helvetica 13 bold",
                    command=option_selector,
                    background='#21262d',
                    foreground='white',
                    activeforeground='white',
                    activebackground='#32373e',
                    width=40)
button3.place(rely='0.35', relx='0.51')

button4 = tk.Button(window,
                    text="Delete",
                    font="Helvetica 13 bold",
                    command=delete_call,
                    background='#21262d',
                    foreground='white',
                    activeforeground='white',
                    activebackground='#32373e',
                    width=40)
button4.place(rely='0.7', relx='0.25')
window.mainloop()
