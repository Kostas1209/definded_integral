from tkinter import *
import math
from tkinter import messagebox

# sin() cos() tg() ctg() arsin() arcos() artg() ln() lg() log() 
# + - * / 
# a^()
# e pi
# example: "e^(pi*x) , 

mainWindow = Tk()
mainWindow.title("Приблеженные вычисления интегралов")
mainWindow.geometry("1080x500")
PI = math.pi
exp = math.e
RectResult = StringVar()
TrapezResult = StringVar()
ParabolResult = StringVar()
RectResult.set('')
TrapezResult.set('')
ParabolResult.set('')

class Stack:
    def __init__(self):
        self.arr=list()

    def isEmpty(self):
        return len(self.arr)==0

    def push(self,n):
        self.arr.append(n)

    def top(self):
        return self.arr[len(self.arr)-1]

    def pop(self):
        x=self.arr.pop()
        return x

def Parser(string):
    arr=list()
    temp=''
    i=0
    while i<len(string):
        if string[i].isnumeric() or string[i]=='.': #check numeric
            temp+=string[i]
        elif temp!='':   #add numeric
           arr.append(float(temp))
           temp=''
        if (string[i] == '(' or string[i] == ')' or string[i] == '+' or string[i] == '-' or string[i] == '*' or string[i] == '/' 
               or string[i] == '^'): #add ()
            arr.append(string[i])

        if string[i] == 's' and string[i+1] == 'i' and string[i+2] == 'n': #sin
            arr.append('sin')
            i+=2

        elif string[i] == 'c' and string[i+1] == 'o' and string[i+2] == 's': #cos
            arr.append('cos')
            i+=2

        elif string[i] == 't' and string[i+1] == 'g': #tg
            arr.append('tg')
            i+=1

        elif string[i] == 'c' and string[i+1] == 't' and string[i+2] == 'g': #ctg
            arr.append('ctg')
            i+=2

        elif string[i] == 'a' and string[i+1] == 'r' and string[i+2] == 's' and string[i+3] == 'i' and string[i+4] == 'n' : #arsin
            arr.append('arsin')
            i+=4

        elif string[i] == 'a' and string[i+1] == 'r' and string[i+2] == 'c' and string[i+3] == 'o' and string[i+4] == 's' : #arcos
            arr.append('arcos')
            i+=4

        elif string[i] == 'a' and string[i+1] == 'r' and string[i+2] == 't' and string[i+3] == 'g' : #artg
            arr.append('artg')
            i+=3

        elif string[i] == 'l' and string[i+1] == 'n': #ln
            arr.append('ln')
            i+=1

        elif string[i] == 'l' and string[i+1] == 'g': #lg
            arr.append('lg')
            i+=1

        elif string[i] == 'l' and string [i+1] == 'o' and string[i+2] == 'g' : #log
            arr.append('log')
            i+=2

        elif string[i] == 'e': # exponent
            arr.append('e')

        elif string[i] == 'x': # variable
            arr.append('x')

        elif string[i] == 'p' and string[i+1] == 'i':  #pi
            arr.append('pi')
            i+=1
        i+=1

    if temp!='':   #add numeric if it stay at the end
         arr.append(float(temp))
         temp=''

    return arr

def calculation(x1,x2,sign):
    if sign == '+':
        return x1+x2
    if sign == '-':
        return x1-x2
    if sign == '*':
        return x1*x2
    if sign == '/':
        return x1/x2
    if sign == '^':
        return x1**x2
    return 


def calcFunction(x1,sign):
    if sign == 'sin':
        return math.sin(x1)
    if sign == 'cos':
        return math.cos(x1)
    if sign == 'tg':
        return math.tan(x1)
    if sign == 'ctg':
        return 1/math.tan(x1)
    if sign == 'arsin':
        return math.asin(x1)
    if sign == 'arcos':
        return math.acos(x1)
    if sign == 'artg':
        return math.atan(x1)
    if sign == 'ln':
        return math.log(x1,exp)
    if sign == 'lg':
        return math.log10(x1)
    if sign == 'log':
        return math.log(x1,2)
    return

def Check(upper ,below,tokens, amount):
    if float(below) >= float(upper):
        messagebox.showinfo("Error","Нижняя граница больше верхней")
        return False
    temp=0
    for item in tokens:
        if item == '(':
            temp+=1
        if item == ')':
            temp-=1
    if temp!=0:
        messagebox.showinfo("Error","Неправильно поставлены скобки")
        return False
    if int(amount) <= 0 :
        messagebox.showinfo("Error","Неправиьное количество интервалов")
        return False
    return True

def isfunction(s):
    if s!='+' and s!='-' and s!='*' and s!=')' and s!='(' and s!='/' and s!='^':
        return True
    else :
        return False


def Compute(n,arr):
    numbers = Stack()
    signs = Stack()
    for item in arr:
        if type(item) is float or item == 'e' or item == 'pi' or item == 'x':  # item is number 
            if item == 'e':
                numbers.push(exp)
            if item == 'pi':
                numbers.push(PI)
            if item == 'x':
                numbers.push(n)
            if type(item) is float:
                numbers.push(item)
        else:
            if  signs.isEmpty():
                signs.push(item)
            else:
                if isfunction(item):
                    signs.push(item)
                else:
                   if item == '(':
                      signs.push(item)
                   else:
                       if item == ')':
                          top = signs.pop()
                          while top!='(':
                             x2 = numbers.pop()
                             x1 = numbers.pop()
                             res = calculation(x1,x2,top)
                             numbers.push(res)
                             top=signs.pop()
                          if not signs.isEmpty():
                             if weight[signs.top()] == 1 :
                                sign=signs.pop()
                                x = numbers.pop()
                                res=calcFunction(x,sign)
                                numbers.push(res)
                             elif weight[signs.top()] == 4:
                                sign=signs.pop()
                                x2 = numbers.pop()
                                x1 = numbers.pop()
                                res=calculation(x1,x2,sign)
                                numbers.push(res)
                       else:
                           if weight[signs.top()] < weight[item]:
                              signs.push(item)
                           else:
                              top = signs.top()
                              while weight[top] >= weight[item]:
                                 top=signs.pop()
                                 x2=numbers.pop()
                                 x1=numbers.pop()
                                 res=calculation(x1,x2,top)
                                 numbers.push(res)
                                 if signs.isEmpty():
                                     break
                                 else:
                                     top=signs.top()
                              signs.push(item)
    while signs.isEmpty()==False:
        top=signs.pop()
        x2=numbers.pop()
        x1=numbers.pop()
        res=calculation(x1,x2,top)
        numbers.push(res)

    return numbers.top()

weight = { '(' : 0 , ')' : 0 , 'sin': 1 , 'cos' : 1 ,'tg' : 1 , 'ctg' : 1,
           'arsin':1 , 'arcos' : 1, 'artg' : 1,
           'ln' : 1 , 'lg' : 1, 'log' : 1, '+' : 2, '-' : 2,
           '*' : 3 , '/' : 3, '^' : 4
          }

def click_button(string , amount, upper , below):
    yes= Check(upper ,below,string,amount)
    if yes==True:
       tokens = Parser(string)
       result =[0,0,0]
       h= (upper - below)/amount
       temp1=0
       temp2=0
       result[1] =( Compute(below,tokens) + Compute(upper,tokens) )/2
       result[0] = Compute(below,tokens)
       result[2]=Compute(below,tokens) + Compute(upper,tokens)

       for i in range(1,amount):
          temp=Compute(below+i*h,tokens)
          result[0]+=temp
          result[1]+=temp
          if i%2==1:
             temp1+=temp
          else:
             temp2+=temp
       result[0]*=h
       result[1]*=(h)
       if amount%2==1:
          result[2]=0
       else:
          temp2*=2
          temp1*=4
          result[2]+=temp1+temp2
          result[2]=result[2]*h/3
       
       RectResult.set(str (result[0]) )
       TrapezResult.set(str (result[1]) )
       ParabolResult.set(str (result[2]) )
    return 


def main():
    
    AmountOfSection = IntVar() # поле ввода количества интервалов
    AmountOfSection.set(10)
    entryAmountOfSections = Entry(textvariable = AmountOfSection,font=30,bg = "#FFF8DC")
    entryAmountOfSections.place(x=720,y=50,height=25,width=70)

    LabelAmountOfSections = Label(text = "Напишите количество отрезков (метод парабол -  парное количество) : ", font="Arial 15")#инструкция
    LabelAmountOfSections.place(x=50,y=50)

    LabelIntegral = Label(text='S', font = "Arial 80")#Знак интеграла
    LabelIntegral.place(x=130,y=150)

    upperBorder = DoubleVar()#верхняя граница
    entryUpperBorder = Entry(textvariable = upperBorder,font="Arial 15" , bg = "#FFF8DC",justify = CENTER)
    entryUpperBorder.place(x=145,y=120,height=40,width=80)

    belowBorder = DoubleVar()# нижняя граница
    entryBelowBorder = Entry(textvariable = belowBorder,font="Arial 15" , bg = "#FFF8DC",justify = CENTER)
    entryBelowBorder.place(x=145,y=255,height=40,width=80)

    function = StringVar()# поле ввода функции
    entryFunction = Entry(textvariable = function,font = "Arial 15")
    entryFunction.place(x = 250 ,y=200,height=40,width=400)

    LabelDiference = Label(text='dx', font = "Arial 30")# надпись диференциала
    LabelDiference.place(x=670,y=190)

    LabelRectMethod = Label (text = 'Метод прямоугольников   : ', font = "Arial 20")
    LabelTrapezMethod = Label(text ='Метод трапеций          : ', font = "Arial 20")
    LabelParabolaMethod =Label(text='Метод парабол(Симпсона) : ', font = "Arial 20")
    LabelRectMethod.place(x = 250, y = 290)
    LabelTrapezMethod.place(x = 250, y = 340)
    LabelParabolaMethod.place(x = 250, y = 390)

    ComputeButton = Button(text = "Считать", font="Arial 20",bg = "#FFFF00", command = lambda : click_button(function.get(),AmountOfSection.get(),upperBorder.get() ,belowBorder.get()) )
    ComputeButton.place( x = 750 ,y = 190)

    LabelRectResult = Label (textvariable = RectResult, font = "Arial 20")
    LabelTrapezResult = Label(textvariable = TrapezResult, font = "Arial 20")
    LabelParabolaResult =Label(textvariable = ParabolResult, font = "Arial 20")
    LabelRectResult.place(x=700,y=290)
    LabelTrapezResult.place(x=700,y=340)
    LabelParabolaResult.place(x=700,y=390)


    mainloop()

main()