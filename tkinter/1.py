import tkinter as tk

root = tk.Tk()
root.geometry('500x300+100+100') #x为乘
root.title('辞职信')

frame1 = tk.Frame(root)
frame1.pack()

tk.Label(frame1, text='尊敬的各位领导：', font=24, padx=30, pady=30).pack(side=tk.LEFT, anchor=tk.N)
img = tk.PhotoImage(file='img.png')
label_img = tk.Label(frame1, image = img, padx=30, pady=30, bd=0)
label_img.pack(side=tk.LEFT, anchor=tk.N)

tk.Label(frame1, text='辞职人：正心', height=25, font=24, padx=30, pady=30, anchor=tk.S).pack(side = tk.LEFT)
img1 = tk.PhotoImage(file='yes.png')
img2 = tk.PhotoImage(file='no.png')
yes_btn = tk.Button(frame1, image=img1, bd=0)
yes_btn.place(relx=0.3 , rely=0.8, anchor=tk.CENTER)
no_btn = tk.Button(frame1, image=img2,bd=0)
no_btn.place(relx=0.7 , rely=0.8, anchor=tk.CENTER)

frame2 = tk.Frame(root)
root.mainloop()