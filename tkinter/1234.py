import tkinter #导入tkinter模块
root = tkinter.Tk()#生成一个主窗口对象
button1 = tkinter.Button(root,#创建按钮1
anchor = tkinter.E,#设置文本的对齐方式
text ='Button1',#设置按钮上显示的文本
width =30,#设置按钮的宽度
height =7)#设置按钮的高度
button1.pack()#将按钮添加到窗口中
button2 = tkinter.Button(root,#创建按钮2
text ='Button2',#设置按钮上显示的文本
bg ='blue')#设置按钮的背景色
button2.pack()#将按钮添加到窗口中
button3 = tkinter.Button(root,#创建按钮3
text ='Button3',#设置按钮上显示的文本
width =12,#设置按钮的宽度
height =1)#设置按钮的高度
button3.pack()#将按钮添加到窗口中
button4 = tkinter.Button(root,#创建按钮4
text ='Button4',#设置按钮上显示的文本
width =40,#设置按钮的宽度
height =7,#设置按钮的高度
state = tkinter.DISABLED)#设置按钮为禁用的
button4.pack()#将按钮添加到窗口中
root.mainloop()#进入消息循环