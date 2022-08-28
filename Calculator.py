from tkinter import*
class MyWindow:
    def __init__(self,root):
        self.exp=""
        self.entry=""
        self.t1=Entry(root,relief=RIDGE, justify='right', bd=23, bg="powder blue")
        self.t1.pack(fill=BOTH)
        self.B1=Button(root,text='1',height=1,width=8,command=lambda:self.press(1),fg="white",bg="black").place(x=0,y=65)
        self.B2=Button(root,text='2',height=1,width=8,command=lambda:self.press(2),fg="white",bg="black").place(x=68,y=65)
        self.B3=Button(root,text='3',height=1,width=8,command=lambda:self.press(3),fg="white",bg="black").place(x=136,y=65)
        self.B4=Button(root,text='4',height=1,width=8,command=lambda:self.press(4),fg="white",bg="black").place(x=0,y=93)
        self.B5=Button(root,text='5',height=1,width=8,command=lambda:self.press(5),fg="white",bg="black").place(x=68,y=93)
        self.B6=Button(root,text='6',height=1,width=8,command=lambda:self.press(6),fg="white",bg="black").place(x=136,y=93)
        self.B7=Button(root,text='7',height=1,width=8,command=lambda:self.press(7),fg="white",bg="black").place(x=0,y=121)
        self.B8=Button(root,text='8',height=1,width=8,command=lambda:self.press(8),fg="white",bg="black").place(x=68,y=121)
        self.B9=Button(root,text='9',height=1,width=8,command=lambda:self.press(9),fg="white",bg="black").place(x=136,y=121)
        self.B10=Button(root,text='0',height=1,width=8,command=lambda:self.press(0),fg="white",bg="black").place(x=68,y=149)
        self.B11=Button(root,text='+',height=1,width=8,command=lambda:self.press("+"),fg="white",bg="black").place(x=204,y=65)
        self.B12=Button(root,text='-',height=1,width=8,command=lambda:self.press("-"),fg="white",bg="black").place(x=204,y=93)
        self.B13=Button(root,text='*',height=1,width=8,command=lambda:self.press("*"),fg="white",bg="black").place(x=204,y=121)
        self.B14=Button(root,text=chr(247),height=1,width=8,command=lambda:self.press(chr(247)),fg="white",bg="black").place(x=204,y=149)
        self.B15=Button(root,text='.',height=1,width=8,command=lambda:self.press("."),fg="white",bg="black").place(x=0,y=149)
        self.B16=Button(root,text='=',height=1,width=8,command=self.equalto,fg="white",bg="black").place(x=136,y=149)
        self.B17=Button(root,text='CLEAR',height=1,width=8,command=self.clear,fg="white",bg="black").place(x=0,y=177)
        self.B18=Button(root,text='BACK',height=1,width=8,command=self.back,fg="white",bg="black").place(x=68,y=177)
        self.B19=Button(root,text='%',height=1,width=8,command=lambda:self.press("%"),fg="white",bg="black").place(x=136,y=177)
        self.B20=Button(root,text='^',height=1,width=8,command=lambda:self.press("^"),fg="white",bg="black").place(x=204,y=177)
    def press(self,num):
        self.exp=self.exp+str(num)
        self.display(self.exp)
        self.entry=num
        print(self.entry)
    def clear(self):
        self.exp=""
        self.t1.delete(0,'end')
    def equalto(self):
        self.t1.delete(0,'end')
        self.exp=self.exp.replace("%","/100")
        self.exp=self.exp.replace(chr(247),"/")
        self.exp=self.exp.replace("^","**")
        total=str(eval(self.exp))
        self.exp=total
        self.t1.insert(END,total)
    def back(self):
        self.t1.delete(0,'end')
        E=self.exp
        E.split()
        self.exp=E[:-1]
        self.t1.insert(END,self.exp)
    def PN(self):
        nev=-(self.entry)
        exp=self.exp
        exp.split()
        exp=exp.replace(str(exp[-1]),str(nev))
        self.exp=exp
        self.display(self.exp)
           
    def display(self,exp):
        self.t1.delete(0,'end')
        self.t1.insert(END,exp)
   
window=Tk()
frame=Frame(window)
frame.pack()
mywin=MyWindow(window)
window.title("CALCULATOR")
window.geometry("266x200")
window.mainloop() 
