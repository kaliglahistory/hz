from tkinter import *
from tkinter import filedialog

import test2

window = Tk()
window.title("Добро пожаловать")
window.geometry('800x600')

def batton_c():
    files = filedialog.askopenfilename()
    test123 = files
    print(test123)
batton = Button(text="Выполнить экранирование", command =batton_c)
batton.pack()
batton.grid(column=1, row=0)
batton.place(relx=.5, rely=.5,anchor="c")

lbl =Label(window,text="1. Закинуть файл в папку hz")
lbl2=Label(window,text ="2. запустить ярлык по")
lbl2.place(relx=0.4, rely=0.25)
lbl2_5=Label(window,text ="2.нажать кнопку")
lbl3=Label(window,text ="3. Готово")
lbl2.place(x = 150, y = 500)
lbl.grid(column = 5, row = 1)
lbl2_5
lbl2.grid(column = 5, row = 3)
lbl3.grid(column = 5, row = 4)
lbl2_5.grid(column = 5, row =2)




window.mainloop()


