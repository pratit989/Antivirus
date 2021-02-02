import tkinter as tk
from tkinter import filedialog

from Modules.VirusAPI import scan
from OptionBox import option_box

filename = ''
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
    if filename != '':
        func_selected(file_path=filename)
    else:
        func_selected()


# File Browse Function
def browse_function():
    global filename
    filename = filedialog.askopenfilename()
    try:
        enter_path.insert(tk.END, filename)
        print(filename)
    except NameError:
        pass


# Scan Function
def scan_call():
    scan(filename)


window = tk.Tk()
# Background of window
window.configure(background='#161b22')
window.geometry("860x80")
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
button2.place(rely='0.5', relx='0.02')

# Encrypt Button
button2 = tk.Button(window,
                    text="Encrypt / Decrypt",
                    font="Helvetica 13 bold",
                    command=option_selector,
                    background='#21262d',
                    foreground='white',
                    activeforeground='white',
                    activebackground='#32373e',
                    width=40)
button2.place(rely='0.5', relx='0.51')
window.mainloop()
