import a2
import tkinter
root = tkinter.Tk()

root.geometry('500x300+100+100') #x为乘

root.title('辞职信')

frame1 = tkinter.Frame(root)

frame1.pack()

tkinter.Label(frame1, text='尊敬的各位领导：', font=24, padx=30, pady=30).pack(side=tkinter.LEFT, anchor=tkinter.N)


frame2 = tkinter.Frame(root)

root.mainloop()

