from tkinter import *
root=Tk()
root.title("Temperature Converter")
var1=DoubleVar()
var2=DoubleVar()
root.geometry('1500x800')
root.configure(background="Green")

label=Label(root,text='TEMPERATURE CONVERTER',font=('Arial',30),bg="Light Green")
label.pack(side=TOP)

label1=Label(root,text='Temperture in Celcius = ',font=('Arial',25))
label1.place(x=200,y=200)

label2=Label(root,text='Temperture in Fahrenheit =',font=('Arial',25))
label2.place(x=200,y=300)

entry1=Entry(root,font=('Arial',25),textvariable=var1)
entry1.place(x=600,y=200)


label3=Label(root,font=('Arial',25),bg="Green")
label3.place(x=600,y=300)

def click1():
	label3.config(text=str(var1.get() * 1.8+32)+' °F')
	
button1=Button(root,text='Convert', font=('Arial',25),command=click1)
button1.place(x=1000,y=190)

label4=Label(root,text='Temperture in Fahrenheit =',font=('Arial',25))
label4.place(x=200,y=400)

label5=Label(root,text='Temperture in Celcius = ',font=('Arial',25))
label5.place(x=200,y=500)


entry2=Entry(root, font=('Arial',25),textvariable=var2)
entry2.place(x=600,y=400)

label6=Label(root, font=('Arial',25),bg="Green")
label6.place(x=600,y=500)

def click2():
	label6.config(text=str((var2.get()-32)/1.8)+' °C')

button2=Button(root,text='Convert', font=('Arial',25),command=click2)
button2.place(x=1000,y=390)

root.mainloop()
