import csv, time
from encodings import utf_8
import tkinter
from datetime import datetime
from tkinter import ttk
    
class SampleApp(tkinter.Tk):
    def __init__(window):
        tkinter.Tk.__init__(window)
        window.title("자가진단")
        window.geometry("290x210")#("260x210") #가로 세로 x좌표이동 y좌표이동
        window.resizable(False,False) #xy좌표변경안됨
        window._frame = None
        window.switch_frame(StartPage)
        
    def switch_frame(window, frame_class):
        new_frame = frame_class(window)
        if window._frame is not None:
            window._frame.destroy()
        window._frame = new_frame
        window._frame.pack()

class StartPage(tkinter.Frame):
    def __init__(window, master):
        infocsv = open('./info.csv', 'r', encoding="utf-8") #파일이 있는 경로+파일이름.csv
        value_csv1 = csv.reader(infocsv)
        csv_info=[]
        for value_csv2 in value_csv1 :
            csv_info.append(value_csv2)

        start_time, user_name, user_birthday ,user_password = tkinter.StringVar(),tkinter.StringVar(), tkinter.StringVar(), tkinter.StringVar()
        start_time.set(csv_info[0]),user_name.set(csv_info[1]), user_birthday.set(csv_info[2]), user_password.set(csv_info[3])


        def data_check():
            if '['+start_time.get()[1:-2]+']' == str(csv_info[0]) and '['+user_name.get()[1:-2]+']' == str(csv_info[1]) and '['+user_birthday.get()[1:-2]+']' == str(csv_info[2]) and '['+user_password.get()[1:-2]+']' == str(csv_info[3]):
                master.switch_frame(SamePage)
                
            else:
                #csv_save=[str(start_time.get()),str(user_name.get()),str(user_birthday.get()),str(user_password.get())]
                with open("info.csv", 'w') as f:
                    if str(start_time.get()).startswith('('):
                        f.write(str(start_time.get()[2:-3]))
                        f.close
                    else:
                        f.write(str(start_time.get()))
                        f.close
                with open("info.csv", 'a', newline='',encoding = "utf-8") as f:
                    if str(user_name.get()).startswith('('):
                        f.write('\n'+str(user_name.get()[2:-3]))
                        f.close
                    else:
                        f.write('\n'+str(user_name.get()))
                        f.close
                with open("info.csv", 'a') as f:
                    if str(user_birthday.get()).startswith('('):
                        f.write('\n'+str(user_birthday.get()[2:-3]))
                        f.close
                    else:
                        f.write('\n'+str(user_birthday.get()))
                        f.close
                with open("info.csv", 'a') as f:
                    if str(user_password.get()).startswith('('):
                        f.write('\n'+str(user_password.get()[2:-3]))
                        f.close
                    else:
                        f.write('\n'+str(user_password.get()))
                        f.close

                #f = open('info.csv', 'w', newline='', encoding="utf-8")
                #f.write(str(start_time.get()[2:-3])+'\n')
                #f.write(str(user_name.get()[2:-3])+'\n')
                #f.write(str(user_birthday.get()[2:-3])+'\n')
                #f.write(str(user_password.get()[2:-3]))
                #f.close
                time.sleep(1)
                master.switch_frame(SamePage)
                #master.switch_frame(DifferentPage)
                
        tkinter.Frame.__init__(window, master)
        ttk.Label(window, text = "실행 시간" ).grid(row = 0, column = 0, padx = 10, pady = 10)
        ttk.Label(window, text = "이름" ).grid(row = 1, column = 0, padx = 10, pady = 10)
        ttk.Label(window, text = "생년월일").grid(row = 2, column = 0, padx = 10, pady = 10)
        ttk.Label(window, text = "비밀번호").grid(row = 3, column = 0, padx = 10, pady = 10)
        #ttk.Button(window, text="one",command=lambda: master.switch_frame(PageOne)).grid(row = 4, column = 0, padx = 10, pady = 10)
        ttk.Entry(window, textvariable = start_time).grid(row = 0, column = 1, padx = 10, pady = 10)
        ttk.Entry(window, textvariable = user_name).grid(row = 1, column = 1, padx = 10, pady = 10)
        ttk.Entry(window, textvariable = user_birthday).grid(row = 2, column = 1, padx = 10, pady = 10)
        ttk.Entry(window, textvariable = user_password, show='*').grid(row = 3, column = 1, padx = 10, pady = 10)
        ttk.Button(window, text = "시작", command = data_check).grid(row = 4, column = 1, padx = 10, pady = 10)
        
        #tkinter.Frame.__init__(self, master)
        #tkinter.Label(self, text="Start page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        #tkinter.Button(self, text="Go to page one",
        #          command=lambda: master.switch_frame(PageOne)).pack()
        #tkinter.Button(self, text="Go to page two",
        #          command=lambda: master.switch_frame(PageTwo)).pack()

class DifferentPage(tkinter.Frame):
    def __init__(window, master):
        tkinter.Frame.__init__(window, master)
        ttk.Label(window, text = " " ).grid(row = 0, column = 0, padx = 10, pady = 10)
        ttk.Label(window, text = " 정보가 다릅니다." ).grid(row = 1, column = 0, padx = 10, pady = 10)
        ttk.Label(window, text = "입력된 정보를 저장하고 실행 하시겠습니까?").grid(row = 2, column = 0, padx = 10, pady = 10)
        ttk.Label(window, text = " ").grid(row = 3, column = 0, padx = 10, pady = 10)
        ttk.Button(window, text= "취소", command =lambda: master.switch_frame(StartPage)).grid(row = 4, column = 0, padx = 10, pady = 10)
        ttk.Label(window, text = " ").grid(row = 0, column = 1, padx = 10, pady = 10)
        ttk.Label(window, text = " ").grid(row = 1, column = 1, padx = 10, pady = 10)
        ttk.Label(window, text = " ").grid(row = 2, column = 1, padx = 10, pady = 10)
        ttk.Label(window, text = " ").grid(row = 3, column = 1, padx = 10, pady = 10)
        ttk.Button(window, text= "저장&실행", command=lambda: master.switch_frame(SamePage)).grid(row = 4, column = 1, padx = 10, pady = 10)
        
        #tkinter.Frame.__init__(self, master)
        #tkinter.Frame.configure(self,bg='blue')
        #tkinter.Label(self, text="Page one", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        #tkinter.Button(self, text="Go back to start page",
        #          command=lambda: master.switch_frame(StartPage)).pack()

class SamePage(tkinter.Frame):
    def __init__(window, master):
        tkinter.Frame.__init__(window, master)

        infocsv = open('./info.csv',  encoding="utf-8") #파일이 있는 경로+파일이름.csv
        value_csv1 = csv.reader(infocsv)
        csv_info=[]
        for value_csv2 in value_csv1 :
            csv_info.append(value_csv2)
        start_time =  str(csv_info[0])[2:-2]

        # Define a function to print something inside infinite loop
        condition=True
        def infinite_loop():
            if condition:
                print(datetime.now())
                window.after(10000, infinite_loop)

        # Call the infinite_loop() again after 1 sec win.after(1000, infinite_loop)

        def start():
            global condition
            condition=True
            infinite_loop()

        def stop():
            global condition
            condition=False
            master.switch_frame(StartPage)

        start()
        
        ttk.Label(window, text = " ").grid(row = 0, column = 0, padx = 10, pady = 10)
        ttk.Label(window, text = " ").grid(row = 1, column = 0, padx = 10, pady = 10)
        ttk.Label(window, text = str(start_time)+'에').grid(row = 2, column = 0, padx = 10, pady = 10)
        ttk.Label(window, text = " ").grid(row = 3, column = 0, padx = 10, pady = 10)
        ttk.Button(window, text= "중지", command = stop).grid(row = 4, column = 0, padx = 10, pady = 10)
        ttk.Label(window, text = " ").grid(row = 0, column = 1, padx = 10, pady = 10)
        ttk.Label(window, text = " ").grid(row = 1, column = 1, padx = 10, pady = 10)
        ttk.Label(window, text = "실행 됩니다").grid(row = 2, column = 1, padx = 10, pady = 10)
        ttk.Label(window, text = " ").grid(row = 3, column = 1, padx = 10, pady = 10)
        ttk.Button(window, text= "종료", command = window.quit).grid(row = 4, column = 1, padx = 10, pady = 10)
        
        #test()
        #tk.Frame.__init__(self, master)
        #tk.Frame.configure(self,bg='red')
        #tk.Label(self, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        #tk.Button(self, text="Go back to start page",
        #          command=lambda: master.switch_frame(StartPage)).pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()