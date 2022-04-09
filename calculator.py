from tkinter import *
from tkinter import messagebox
import math
screen = Tk()
screen.title('Calculator by Bhairavi :)')
screen.iconbitmap('sycn.ico')
screen.maxsize(width=470, height= 495)
screen.minsize(width=360, height= 495)
screen.geometry('360x495')

def click(number):
    global operator
    operator += str(number)
    tex.set(operator)

def clear():
    global operator
    operator = ''
    tex.set(operator)

def equal():
    global operator
    try:
        result = eval(operator)
        operator = str(result)
        tex.set(result)
    except:
        messagebox.showinfo('notification', 'Try again something is wrong here', parent=screen)

def casin():
    global operator
    try:
        result = math.sin(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('notification', 'Try again something is wrong here', parent=screen)

def cacos():
    global operator
    try:
        result = math.cos(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('notification', 'Try again something is wrong here', parent=screen)

def catan():
    global operator
    try:
        result = math.tan(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('notification', 'Try again something is wrong here', parent=screen)

def sqrt():
    global operator
    try:
        result = math.sqrt(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('notification', 'Try again something is wrong here', parent=screen)

def log():
    global operator
    try:
        result = math.log(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('notification', 'Try again something is wrong here', parent=screen)

###############################binding function

def on_enter7(e):
    btn7.configure(bg='pink')
def on_leave7(e):
    btn7.configure(bg='powder blue')

def on_enter8(e):
    btn8.configure(bg='pink')
def on_leave8(e):
    btn8.configure(bg='powder blue')

def on_enter9(e):
    btn9.configure(bg='pink')
def on_leave9(e):
    btn9.configure(bg='powder blue')

def on_enteradd(e):
    btnadd.configure(bg='pink')
def on_leaveadd(e):
    btnadd.configure(bg='powder blue')

def on_enter4(e):
    btn4.configure(bg='pink')
def on_leave4(e):
    btn4.configure(bg='powder blue')

def on_enter5(e):
    btn5.configure(bg='pink')
def on_leave5(e):
    btn5.configure(bg='powder blue')

def on_enter6(e):
    btn6.configure(bg='pink')
def on_leave6(e):
    btn6.configure(bg='powder blue')

def on_entersub(e):
    btnsub.configure(bg='pink')
def on_leavesub(e):
    btnsub.configure(bg='powder blue')

def on_enter1(e):
    btn1.configure(bg='pink')
def on_leave1(e):
    btn1.configure(bg='powder blue')

def on_enter2(e):
    btn2.configure(bg='pink')
def on_leave2(e):
    btn2.configure(bg='powder blue')

def on_enter3(e):
    btn3.configure(bg='pink')
def on_leave3(e):
    btn3.configure(bg='powder blue')

def on_entermul(e):
    btnmul.configure(bg='pink')
def on_leavemul(e):
    btnmul.configure(bg='powder blue')

def on_enterdiv(e):
    btndiv.configure(bg='pink')
def on_leavediv(e):
    btndiv.configure(bg='powder blue')

def on_enter0(e):
    btn0.configure(bg='pink')
def on_leave0(e):
    btn0.configure(bg='powder blue')

def on_enterclear(e):
    btnclear.configure(bg='pink')
def on_leaveclear(e):
    btnclear.configure(bg='powder blue')

def on_enterequal(e):
    btnequal.configure(bg='pink')
def on_leaveequal(e):
    btnequal.configure(bg='powder blue')

def on_entersin(e):
    btnsin.configure(bg='pink')
def on_leavesin(e):
    btnsin.configure(bg='orange')

def on_entercos(e):
    btncos.configure(bg='pink')
def on_leavecos(e):
    btncos.configure(bg='orange')

def on_entertan(e):
    btntan.configure(bg='pink')
def on_leavetan(e):
    btntan.configure(bg='orange')

def on_entersqrt(e):
    btnsqrt.configure(bg='pink')
def on_leavesqrt(e):
    btnsqrt.configure(bg='orange')

def on_enterlog(e):
    btnlog.configure(bg='pink')
def on_leavelog(e):
    btnlog.configure(bg='orange')







tex = StringVar()
operator = ''

entry1 = Entry(screen, bg='yellow',font=('arial', 20,'bold'),bd='30', justify='right',textvariable=tex)
entry1.grid(row=0, columnspan =4)

btn7 = Button(screen,text='7', font=('arial',20,"bold"),bd = 8,padx=16,pady=16, command=lambda:click(7),
              activebackground = 'red',activeforeground = 'white', bg = 'powder blue')
btn7.grid(row=1, column=0)


btn8 = Button(screen,text='8', font=('arial',20,"bold"),bd = 8,padx=16,pady=16,command=lambda:click(8),
              activebackground='red', activeforeground='white', bg='powder blue')
btn8.grid(row=1, column=1)

btn9 = Button(screen,text='9', font=('arial',20,"bold"),bd = 8,padx=16,pady=16,command=lambda:click(9),
              activebackground = 'red',activeforeground = 'white', bg = 'powder blue')
btn9.grid(row=1, column=2)

btnadd = Button(screen,text='+', font=('arial',20,"bold"),bd = 8,padx=14,pady=16,command=lambda:click('+'),
                activebackground='red', activeforeground='white', bg='powder blue')
btnadd.grid(row=1, column=3)

btn4 = Button(screen,text='4', font=('arial',20,"bold"),bd = 8,padx=16,pady=16,command=lambda:click(4),
              activebackground = 'red',activeforeground = 'white', bg = 'powder blue')
btn4.grid(row=2, column=0)

btn5 = Button(screen,text='5', font=('arial',20,"bold"),bd = 8,padx=16,pady=16,command=lambda:click(5),
              activebackground='red', activeforeground='white', bg='powder blue')
btn5.grid(row=2, column=1)

btn6 = Button(screen,text='6', font=('arial',20,"bold"),bd = 8,padx=16,pady=16,command=lambda:click(6),
              activebackground='red', activeforeground='white', bg='powder blue')
btn6.grid(row=2, column=2)

btnsub = Button(screen,text='-', font=('arial',20,"bold"),bd = 8,padx=18,pady=16,command=lambda:click('-'),
                activebackground='red', activeforeground='white', bg='powder blue'
                )
btnsub.grid(row=2, column=3)

btn1 = Button(screen,text='1', font=('arial',20,"bold"),bd = 8,padx=16,pady=16,command=lambda:click(1),
              activebackground='red', activeforeground='white', bg='powder blue'
              )
btn1.grid(row=3, column=0)

btn2 = Button(screen,text='2', font=('arial',20,"bold"),bd = 8,padx=16,pady=16,command=lambda:click(2),
              activebackground='red', activeforeground='white', bg='powder blue'
              )
btn2.grid(row=3, column=1)

btn3 = Button(screen,text='3', font=('arial',20,"bold"),bd = 8,padx=16,pady=16,command=lambda:click(3),
              activebackground='red', activeforeground='white', bg='powder blue'
              )
btn3.grid(row=3, column=2)

btnmul = Button(screen,text='*', font=('arial',20,"bold"),bd = 8,padx=16,pady=16,command=lambda:click('*'),
                activebackground='red', activeforeground='white', bg='powder blue'
                )
btnmul.grid(row=3, column=3)

btndiv = Button(screen,text='/', font=('arial',20,"bold"),bd = 8,padx=20,pady=16,command=lambda:click('/'),
                activebackground='red', activeforeground='white', bg='powder blue'
                )
btndiv.grid(row=4, column=0)

btn0 = Button(screen,text='0', font=('arial',20,"bold"),bd = 8,padx=14,pady=16,command=lambda:click(0),
              activebackground='red', activeforeground='white', bg='powder blue'
              )
btn0.grid(row=4, column=1)

btnclear = Button(screen,text='C', font=('arial',20,"bold"),bd = 8,padx=14,pady=16,command = clear,
                  activebackground = 'red',activeforeground = 'white', bg = 'powder blue')
btnclear.grid(row=4, column=2)

btnequal = Button(screen,text='=', font=('arial',20,"bold"),bd = 8,padx=14,pady=16, comman = equal,
                  activebackground='red', activeforeground='white', bg='powder blue'
                  )
btnequal.grid(row=4, column=3)

############################################################advance calculation

btnsin = Button(screen,text='sin', font=('arial',20,"bold"),bd = 8,padx=14,pady=16,command=casin,
              activebackground='red', activeforeground='white', bg='orange'
              )
btnsin.grid(row=0, column=4)

btncos = Button(screen,text='cos', font=('arial',20,"bold"),bd = 8,padx=12,pady=16,command=cacos,
              activebackground='red', activeforeground='white', bg='orange'
              )
btncos.grid(row=1, column=4)

btntan = Button(screen,text='tan', font=('arial',20,"bold"),bd = 8,padx=14,pady=16,command=catan,
              activebackground='red', activeforeground='white', bg='orange'
              )
btntan.grid(row=2, column=4)

btnsqrt = Button(screen,text='sqrt', font=('arial',20,"bold"),bd = 8,padx=8,pady=16,command=sqrt,
              activebackground='red', activeforeground='white', bg='orange'
              )
btnsqrt.grid(row=3, column=4)

btnlog = Button(screen,text='log', font=('arial',20,"bold"),bd = 8,padx=14,pady=16,command=log,
              activebackground='red', activeforeground='white', bg='orange'
              )
btnlog.grid(row=4, column=4)

#######################################################33#binding
btnsin.bind('<Enter>',on_entersin)
btnsin.bind('<Leave>',on_leavesin)

btncos.bind('<Enter>',on_entercos)
btncos.bind('<Leave>',on_leavecos)

btntan.bind('<Enter>',on_entertan)
btntan.bind('<Leave>',on_leavetan)

btnsqrt.bind('<Enter>',on_entersqrt)
btnsqrt.bind('<Leave>',on_leavesqrt)

btnlog.bind('<Enter>',on_enterlog)
btnlog.bind('<Leave>',on_leavelog)


btn7.bind('<Enter>',on_enter7)
btn7.bind('<Leave>',on_leave7)

btn8.bind('<Enter>',on_enter8)
btn8.bind('<Leave>',on_leave8)

btn9.bind('<Enter>',on_enter9)
btn9.bind('<Leave>',on_leave9)

btnadd.bind('<Enter>',on_enteradd)
btnadd.bind('<Leave>',on_leaveadd)

btn4.bind('<Enter>',on_enter4)
btn4.bind('<Leave>',on_leave4)

btn5.bind('<Enter>',on_enter5)
btn5.bind('<Leave>',on_leave5)

btn6.bind('<Enter>',on_enter6)
btn6.bind('<Leave>',on_leave6)

btnsub.bind('<Enter>',on_entersub)
btnsub.bind('<Leave>',on_leavesub)

btn1.bind('<Enter>',on_enter1)
btn1.bind('<Leave>',on_leave1)

btn2.bind('<Enter>',on_enter2)
btn2.bind('<Leave>',on_leave2)

btn3.bind('<Enter>',on_enter3)
btn3.bind('<Leave>',on_leave3)

btnmul.bind('<Enter>',on_entermul)
btnmul.bind('<Leave>',on_leavemul)

btndiv.bind('<Enter>',on_enterdiv)
btndiv.bind('<Leave>',on_leavediv)

btn0.bind('<Enter>',on_enter0)
btn0.bind('<Leave>',on_leave0)

btnclear.bind('<Enter>',on_enterclear)
btnclear.bind('<Leave>',on_leaveclear)

btnequal.bind('<Enter>',on_enterequal)
btnequal.bind('<Leave>',on_leaveequal)






screen.mainloop()
