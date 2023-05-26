from tkinter import *
from tkinter import ttk
from tkinter import messagebox
currency_converter =Tk()
currency_converter.title("Currency Converter")
currency_converter.geometry('451x350')
currency_converter.configure(background='cyan2')
currency=['Indian Rupees','US Dollar','Euro','Pound','Japanese Yen']
cb=ttk.Combobox(currency_converter,values=currency,state="readonly",width=17,font=("Ar
ial Rounded MT Bold",16))
cb.grid(column=0, row=1,pady=20)
cb.current(0)
def curcal():
 try:
 cur=float(textbox1.get())
 if cb.get() == 'Indian Rupees':
 l2.config(text='US Dollar')
 l3.config(text=round((cur*0.014),3))
 l4.config(text='Euro')
 l5.config(text=round((cur*0.013),3))
 l6.config(text='Pound')
 l7.config(text=round((cur*0.011),3))
 l8.config(text='Japanese Yen')
 l9.config(text=round((cur*1.54),3))
 elif cb.get() == 'US Dollar':
 l2.config(text='Indian Rupees')
 l3.config(text=round((cur*71.18),3))
 l4.config(text='Euro')
 l5.config(text=round((cur*0.90),3))
 l6.config(text='Pound')
 l7.config(text=round((cur*0.77),3))
 l8.config(text='Japanese Yen')
 l9.config(text=round((cur*109.54),3))
 elif cb.get() == 'Euro':
 l2.config(text='Indian Rupees')
 l3.config(text=round((cur*79.04),3))
 l4.config(text='US Dollar')
 l5.config(text=round((cur*1.11),3))
 l6.config(text='Pound')
 l7.config(text=round((cur*0.85),3))
 l8.config(text='Japanese Yen')
 l9.config(text=round((cur*121.63),3))
 elif cb.get() == 'Pound':
 l2.config(text='Indian Rupees')
 l3.config(text=round((cur*92.86),3))
 l4.config(text='US Dollar')
 l5.config(text=round((cur*1.30),3))
 l6.config(text='Euro')
 l7.config(text=round((cur*1.17),3))
 l8.config(text='Japanese Yen')
 l9.config(text=round((cur*142.85),3))
 elif cb.get() == 'Japanese Yen':
 l2.config(text='Indian Rupees')
 l3.config(text=round((cur*0.65),3))
 l4.config(text='US Dollar')
 l5.config(text=round((cur*0.0091),3))
 l6.config(text='Euro')
 l7.config(text=round((cur*0.0082),3))
 l8.config(text='Pound')
 l9.config(text=round((cur*0.0070),3))
 except:
 currency_converter.withdraw()
 messagebox.showerror("ERROR","Invalid Operation")
 currency_converter.destroy()

def clear():
 textbox1.delete(0, END)
 l2.config(text='')
 l3.config(text='')
 l4.config(text='')
 l5.config(text='')
 l6.config(text='')
 l7.config(text='')
 l8.config(text='')
 l9.config(text='')

textbox1 = Entry(currency_converter,font=("Arial Rounded MT Bold",14))
textbox1.grid(column=1, row=1)
b1=Button(currency_converter,text="CONVERT",command=curcal,fg='black',font=("Coppe
rplate Gothic Bold",14))
b1.grid(column=1, row=7,pady=20)
b3=Button(currency_converter,text="CLEAR",command=clear,fg='black',font=("Copperplat
e Gothic Bold",14))
b3.grid(column=0, row=7,pady=20)
l2 = Label(currency_converter, text='',bg='cyan2',fg='black',font=("Arial Rounded MT
Bold",12))
l2.grid(column=0, row=2)
l3 = Label(currency_converter, text='',bg='cyan2',fg='black',font=("Arial Rounded MT
Bold",12))
l3.grid(column=1, row=2)
l4 = Label(currency_converter, text='',bg='cyan2',fg='black',font=("Arial Rounded MT
Bold",12))
l4.grid(column=0, row=3)
l5= Label(currency_converter, text='',bg='cyan2',fg='black',font=("Arial Rounded MT
Bold",12))
l5.grid(column=1, row=3)
l6 = Label(currency_converter, text='',bg='cyan2',fg='black',font=("Arial Rounded MT
Bold",12))
l6.grid(column=0, row=4)
l7 = Label(currency_converter, text='',bg='cyan2',fg='black',font=("Arial Rounded MT
Bold",12))
l7.grid(column=1, row=4)
l8 = Label(currency_converter, text='',bg='cyan2',fg='black',font=("Arial Rounded MT
Bold",12))
l8.grid(column=0, row=5)
l9 = Label(currency_converter, text='',bg='cyan2',fg='black',font=("Arial Rounded MT
Bold",12))
l9.grid(column=1, row=5)
currency_converter.mainloop()