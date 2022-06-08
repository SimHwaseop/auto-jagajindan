import csv
import tkinter
from tkinter import ttk

infocsv = open('./info.csv',  encoding="utf-8") #파일이 있는 경로+파일이름.csv
value_csv1 = csv.reader(infocsv)
csv_info=[]
for value_csv2 in value_csv1 :
    csv_info.append(value_csv2)

#csvname = csv_info[0]
#csvbirthday = csv_info[1]
#csvpassword = csv_info[2]

window=tkinter.Tk()

window.title("자가진단")
window.geometry("245x210")#("260x210") #가로 세로 x좌표이동 y좌표이동
window.resizable(False,False) #xy좌표변경안됨
start_time, user_name, user_birthday ,user_password = tkinter.StringVar(),tkinter.StringVar(), tkinter.StringVar(), tkinter.StringVar()
start_time.set(csv_info[0]),user_name.set(csv_info[1]), user_birthday.set(csv_info[2]), user_password.set(csv_info[3])



def data_check():
    if start_time.get() == csv_info[0] and user_name.get() == csv_info[1] and user_birthday.get() == csv_info[2] and user_password.get() == csv_info[3]:
        print("같음")
    else:
        print("다름")

ttk.Label(window, text = "실행 시간" ).grid(row = 0, column = 0, padx = 10, pady = 10)
ttk.Label(window, text = "이름" ).grid(row = 1, column = 0, padx = 10, pady = 10)
ttk.Label(window, text = "생년월일").grid(row = 2, column = 0, padx = 10, pady = 10)
ttk.Label(window, text = "비밀번호").grid(row = 3, column = 0, padx = 10, pady = 10)
ttk.Entry(window, textvariable = start_time).grid(row = 0, column = 1, padx = 10, pady = 10)
ttk.Entry(window, textvariable = user_name).grid(row = 1, column = 1, padx = 10, pady = 10)
ttk.Entry(window, textvariable = user_birthday).grid(row = 2, column = 1, padx = 10, pady = 10)
ttk.Entry(window, textvariable = user_password, show='*').grid(row = 3, column = 1, padx = 10, pady = 10)
ttk.Button(window, text = "시작", command = data_check).grid(row = 4, column = 1, padx = 10, pady = 10)

window.mainloop()