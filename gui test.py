from tkinter import *
from tkinter import ttk

window=Tk()
window.title("자가진단 도우미")
#window.geometry("640x460") #가로 세로 x좌표이동 y좌표이동
#window.resizable(False,False) #xy좌표변경안됨
user_id, password, user_birthday = StringVar(), StringVar(), StringVar()

def check_data():
    if user_id.get() == "Passing" and password.get() == "Story":
        print("Logged IN Successfully")
    else:
        print("Check your Usernam/Password")

ttk.Label(window, text = "이름").grid(row = 0, column = 0, padx = 10, pady = 10)
ttk.Label(window, text = "생년월일").grid(row = 1, column = 0, padx = 10, pady = 10)
ttk.Label(window, text = "비밀번호").grid(row = 2, column = 0, padx = 10, pady = 10)
ttk.Entry(window, textvariable = user_id).grid(row = 0, column = 1, padx = 10, pady = 10)
ttk.Entry(window, textvariable = user_birthday).grid(row = 1, column = 1, padx = 10, pady = 10)
ttk.Entry(window, textvariable = password).grid(row = 2, column = 1, padx = 10, pady = 10)
ttk.Button(window, text = "시작", command = check_data).grid(row = 3, column = 1, padx = 10, pady = 10)

'''
passwordlabel = Label(root, text = "Password ")
passwordlabel.grid(row = 1, column = 0, padx = 10, pady = 10)
#passwordlabel.pack()

passwordinput = Entry(root, show = "*")
#passwordinput.grid(row = 1, column = 1, padx = 10, pady = 10)
passwordinput.pack()

start_btn = Button(window, padx=20, pady=1, text="시작" )
start_btn.pack()
'''

window.mainloop()