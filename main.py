import tkinter as tk
from tkinter import ttk 
from datetime import date
from datetime import datetime

    

root = tk.Tk()                            
root.title("Калькулятор")     
root.geometry("300x250")    
root.minsize(150, 200)          

numsFrame = ttk.Frame(borderwidth=1, relief=tk.SOLID, padding=[8, 10])
buttonsFrame = ttk.Frame(borderwidth=1, relief=tk.SOLID, padding=[8, 10])

numsVar = tk.StringVar()
numsVar.set('')

def error(event):
    root.unbind_all("<Button-1>")
    numsVar.set('')

def clickCE():
    value = numsVar.get()
    value = value[:-1]
    numsVar.set(value)
def clickC():
    numsVar.set('')

def clickOP():
    f = open('log.txt', 'r')
    for line in f:
        lastline  = line
    lastline = lastline.split(' ')
    print(lastline[1])
    numsVar.set(lastline[1])
def clickBtn1():
    value = numsVar.get()
    numsVar.set(value + '1')
def clickBtn2():
    value = numsVar.get()
    numsVar.set(value + '2')
def clickBtn3():
    value = numsVar.get()
    numsVar.set(value + '3')
def clickBtn4():
    value = numsVar.get()
    numsVar.set(value + '4')
def clickBtn5():
    value = numsVar.get()
    numsVar.set(value + '5')
def clickBtn6():
    value = numsVar.get()
    numsVar.set(value + '6')
def clickBtn7():
    value = numsVar.get()
    numsVar.set(value + '7')
def clickBtn8():
    value = numsVar.get()
    numsVar.set(value + '8')
def clickBtn9():
    value = numsVar.get()
    numsVar.set(value + '9')
def clickBtn0():
    value = numsVar.get()
    numsVar.set(value + '0')

def clickPlus():
    value = numsVar.get()
    numsVar.set(value + '+')    
def clickMinus():
    value = numsVar.get()
    numsVar.set(value + '-')
def clickMultiply():
    value = numsVar.get()
    numsVar.set(value + '*')
def clickDevision():
    value = numsVar.get()
    numsVar.set(value + '/')

def clickRightBracket():
    value = numsVar.get()
    numsVar.set(value + ')')
def clickLeftBracket():
    value = numsVar.get()
    numsVar.set(value + '(')

def clickEqual():
    currentDate = datetime.now().date()
    currentTime = datetime.now().time()    
    try:
        value = numsVar.get()
        result = eval(value)
        numsVar.set(result)

        f = open('log.txt', 'a')
        f.write(f"RESULT: {str(result)} DATE: {currentDate} TIME: {currentTime.hour}:{currentTime.minute}")
        f.write('\n')
        f.close()
    except Exception as errorName:
        f = open('log.txt', 'a')
        f.write(f"ERROR: \"{errorName}\" DATE: {currentDate} TIME: {currentTime.hour}:{currentTime.minute}")
        f.write('\n')
        f.close()        
        numsVar.set("Ошибка!")
        root.bind_all("<Button-1>", error)


        


numsEntry = tk.Entry(numsFrame, state=tk.DISABLED, textvariable=numsVar)
numsEntry.pack(fill=tk.X)   

btnPlus = ttk.Button(buttonsFrame, text="+", command=clickPlus)
btnMinus = ttk.Button(buttonsFrame, text="-", command=clickMinus)
btnMultiply = ttk.Button(buttonsFrame, text="*", command=clickMultiply)
btnDevision = ttk.Button(buttonsFrame, text="/", command=clickDevision)
btnEqual = ttk.Button(buttonsFrame, text="=", command=clickEqual)

btnRightBracket = ttk.Button(buttonsFrame, text=")", command=clickRightBracket)
btnLeftBracket = ttk.Button(buttonsFrame, text="(", command=clickLeftBracket)

btnC = ttk.Button(buttonsFrame, text="C", command=clickC)
btnCE = ttk.Button(buttonsFrame, text="CE", command=clickCE)
btnOP = ttk.Button(buttonsFrame, text="OP", command=clickOP)

btn0 = ttk.Button(buttonsFrame, text="0", command=clickBtn0)
btn1 = ttk.Button(buttonsFrame, text="1", command=clickBtn1)
btn2 = ttk.Button(buttonsFrame, text="2", command=clickBtn2)
btn3 = ttk.Button(buttonsFrame, text="3", command=clickBtn3)
btn4 = ttk.Button(buttonsFrame, text="4", command=clickBtn4)
btn5 = ttk.Button(buttonsFrame, text="5", command=clickBtn5)
btn6 = ttk.Button(buttonsFrame, text="6", command=clickBtn6)
btn7 = ttk.Button(buttonsFrame, text="7", command=clickBtn7)
btn8 = ttk.Button(buttonsFrame, text="8", command=clickBtn8)
btn9 = ttk.Button(buttonsFrame, text="9", command=clickBtn9)

btn9.place(relx=0.50, rely=0.00, relwidth=0.25, relheight=0.20)
btn8.place(relx=0.25, rely=0.00, relwidth=0.25, relheight=0.20)
btn7.place(relx=0.00, rely=0.00, relwidth=0.25, relheight=0.20)
btn6.place(relx=0.50, rely=0.20, relwidth=0.25, relheight=0.20)
btn5.place(relx=0.25, rely=0.20, relwidth=0.25, relheight=0.20)
btn4.place(relx=0.00, rely=0.20, relwidth=0.25, relheight=0.20)
btn3.place(relx=0.50, rely=0.40, relwidth=0.25, relheight=0.20)
btn2.place(relx=0.25, rely=0.40, relwidth=0.25, relheight=0.20)
btn1.place(relx=0.00, rely=0.40, relwidth=0.25, relheight=0.20)
btn0.place(relx=0.00, rely=0.60, relwidth=0.25, relheight=0.20)

btnPlus.place(relx=0.75, rely=0.00, relwidth=0.25, relheight=0.20)
btnMinus.place(relx=0.75, rely=0.20, relwidth=0.25, relheight=0.20)
btnMultiply.place(relx=0.75, rely=0.40, relwidth=0.25, relheight=0.20)
btnDevision.place(relx=0.75, rely=0.60, relwidth=0.25, relheight=0.20)

btnCE.place(relx=0.25, rely=0.60, relwidth=0.25, relheight=0.20)
btnC.place(relx=0.50, rely=0.60, relwidth=0.25, relheight=0.20)

btnEqual.place(relx=0.00, rely=0.80, relwidth=0.25, relheight=0.20)
btnOP.place(relx=0.25, rely=0.80, relwidth=0.25, relheight=0.20)
btnLeftBracket.place(relx=0.50, rely=0.80, relwidth=0.25, relheight=0.20)
btnRightBracket.place(relx=0.75, rely=0.80, relwidth=0.25, relheight=0.20)

numsFrame.pack(fill=tk.X, padx=5, pady=5)
buttonsFrame.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)

root.mainloop()