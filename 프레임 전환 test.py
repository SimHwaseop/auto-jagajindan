import csv
import tkinter
from tkinter import ttk
    
class SampleApp(tkinter.Tk):
    def __init__(window):
        tkinter.Tk.__init__(window)
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
        infocsv = open('./info.csv',  encoding="utf-8") #파일이 있는 경로+파일이름.csv
        value_csv1 = csv.reader(infocsv)
        csv_info=[]
        for value_csv2 in value_csv1 :
            csv_info.append(value_csv2)

        start_time, user_name, user_birthday ,user_password = tkinter.StringVar(),tkinter.StringVar(), tkinter.StringVar(), tkinter.StringVar()
        start_time.set(csv_info[0]),user_name.set(csv_info[1]), user_birthday.set(csv_info[2]), user_password.set(csv_info[3])

        def data_check():
            lambda: master.switch_frame(PageOne)
            if start_time.get() == csv_info[0] and user_name.get() == csv_info[1] and user_birthday.get() == csv_info[2] and user_password.get() == csv_info[3]:
                print("같음")
            else:
                print("다름")
                

        tkinter.Frame.__init__(window, master)
        ttk.Label(window, text = "실행 시간" ).grid(row = 0, column = 0, padx = 10, pady = 10)
        ttk.Label(window, text = "이름" ).grid(row = 1, column = 0, padx = 10, pady = 10)
        ttk.Label(window, text = "생년월일").grid(row = 2, column = 0, padx = 10, pady = 10)
        ttk.Label(window, text = "비밀번호").grid(row = 3, column = 0, padx = 10, pady = 10)
        ttk.Button(window, text="one",command=lambda: master.switch_frame(PageOne)).grid(row = 4, column = 0, padx = 10, pady = 10)
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

class PageOne(tkinter.Frame):
    def __init__(window, master):
        tkinter.Frame.__init__(window, master)
        ttk.Label(window, text = "실행 시간" ).grid(row = 0, column = 0, padx = 10, pady = 10)
        ttk.Label(window, text = "이름" ).grid(row = 1, column = 0, padx = 10, pady = 10)
        ttk.Label(window, text = "생년월일").grid(row = 2, column = 0, padx = 10, pady = 10)
        ttk.Label(window, text = "비밀번호").grid(row = 3, column = 0, padx = 10, pady = 10)
        #tkinter.Frame.__init__(self, master)
        #tkinter.Frame.configure(self,bg='blue')
        #tkinter.Label(self, text="Page one", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        #tkinter.Button(self, text="Go back to start page",
        #          command=lambda: master.switch_frame(StartPage)).pack()

class PageTwo(tkinter.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='red')
        tk.Label(self, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()