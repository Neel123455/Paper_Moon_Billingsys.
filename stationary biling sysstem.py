from tkinter import *
from tkinter import messagebox as ms
import mysql.connector as my
from PIL import ImageTk, Image

windows=Tk()
windows['bg']='BLACK'
windows.title('LOGIN PAGE')
windows.maxsize(1000,1000)
windows.minsize(1000,1000)
c=0
windows.c=0
bg=Image.open('paper.png')
ri=bg.resize((1000,700))
bg=ImageTk.PhotoImage(ri)
l=Label(windows,image=bg)
l.image=bg
l.pack()
v=StringVar()
L1=Label(windows,text='USERNAME',fg='white',bg='black',font=('calibra',20),width=10,bd=8)
L1.place(x=300,y=50)
e1=Entry(windows,font=('calibra',20),width=20,textvariable=v,bd=8,relief="solid",borderwidth=3)
e1.place(x=500,y=50)
n=StringVar()
L2=Label(windows,text='PASSWORD' ,fg='white',bg='black',font=('calibra',20),width=10,bd=8)
L2.place(x=300,y=150)
e2=Entry(windows,font=('calibra',20),show="*",width=20,textvariable=n,bd=8,relief="solid",borderwidth=3)
e2.place(x=500,y=150)

#....................................................................................................................

def enter1():
      windows=Toplevel()
      windows['bg']='BLACK'
      windows.title('BILL')
      windows.maxsize(1000,1000)
      windows.minsize(1000,1000)
      bg=Image.open('PAPER MOON.png')
      ri=bg.resize((1000,700))
      bg=ImageTk.PhotoImage(ri)
      la=Label(windows,image=bg)
      la.image=bg
      la.pack()
      qe=StringVar()
      L6=Label(windows,text='NAME',fg='black',bg='lightskyblue',font=('calibra',20),width=10)
      L6.place(x=50,y=100)
      e6=Entry(windows,font=('calibra',20),width=20,textvariable=qe,relief=SUNKEN,borderwidth=7)
      e6.place(x=250,y=100)
      s=IntVar()
      L7=Label(windows,text='ID',fg='black',bg='lightskyblue',font=('calibra',20),width=10)
      L7.place(x=50,y=200)
      z=IntVar()
      e7=Entry(windows,font=('calibra',20),width=20,textvariable=z,bd=10,relief=SUNKEN,borderwidth=7)
      e7.place(x=250,y=200)
      L8=Label(windows,text='ITEMS',fg='black',bg='lightskyblue',font=('calibra',20),width=10)
      L8.place(x=50,y=300)
      q=StringVar()
      e8=Entry(windows,font=('calibra',20),width=20,textvariable=q,relief=SUNKEN,borderwidth=7)
      e8.place(x=250,y=300)
      L9=Label(windows,text='PRICE',fg='black',bg='lightskyblue',font=('calibra',20),width=10)
      L9.place(x=50,y=400)
      f=IntVar()
      e9=Entry(windows,font=('calibra',20),width=20,textvariable=f,relief=SUNKEN,borderwidth=7)
      e9.place(x=250,y=400)
      L10=Label(windows,text='QUANTITY',fg='black',bg='lightskyblue',font=('calibra',20),width=10)
      L10.place(x=50,y=500)
      w=StringVar()
      e10=Entry(windows,font=('calibra',20),width=20,textvariable=w,relief=SUNKEN,borderwidth=7)
      e10.place(x=250,y=500)
      to=StringVar()
      t=Label(windows,text='TOTAL',fg='black',bg='lightskyblue',font=('calibra',20),width=10)
      t.place(x=600,y=150)
      t1=Entry(windows,font=('calibra',20),width=10,textvariable=to,relief=SUNKEN,borderwidth=7)
      t1.place(x=800,y=150)
      gs=StringVar()
      g=Label(windows,text='GST',fg='black',bg='lightskyblue',font=('calibra',20),width=10)
      g.place(x=600,y=100)
      g1=Entry(windows,font=('calibra',20),width=10,textvariable=gs,relief=SUNKEN,borderwidth=7)
      g1.place(x=800,y=100)
      gt=StringVar()
      g2=Label(windows,text='GST%',fg='black',bg='lightskyblue',font=('calibra',20),width=10)
      g2.place(x=55,y=550)
      g3=Entry(windows,font=('calibra',20),width=10,textvariable=gt,relief=SUNKEN,borderwidth=7)
      g3.place(x=255,y=550)
      def gst():
            a=float(e9.get())
            b=float(g3.get())
            s=a*((b*2)/100)
            gs.set(s)
      b=Button(windows,text='GST',fg='black',bg='lightskyblue',font=('calibra',20),width=10,border=5,command=gst)
      b.place(x=600,y=400)
      def cal():
            s=(int(e9.get())*int(e10.get()))
            z=s+float(g1.get())
            to.set(z)
      b=Button(windows,text='TOTAL',fg='black',bg='lightskyblue',font=('calibra',20),width=10,border=5,command=cal)
      b.place(x=600,y=500)
      def sql():
            cn=my.connect(host="localhost",user="root",passwd="Neel3319",database="project")
            cu=cn.cursor()
            m="insert into bill_infos values({},'{}',{},{},'{}',{},{},{})".format(e7.get(),e8.get(),e9.get(),e10.get(),e6.get(),t1.get(),g1.get(),g3.get())
            cu.execute(m)
            cn.commit()
      b4=Button(windows,text='ENTER',fg='white',bg='red',font=('calibra',20),width=10,border=5,command=sql)
      b4.place(x=600,y=200)
      def Exit():
            Exit= ms.askyesno("Exit the System","Do you want to Exit(y/n)?")
            if Exit > 0:
                  windows.destroy()
                  return
      Button_6= Button(windows,highlightcolor="blue",activebackground="red", text="Exit",bd=8, bg="red", fg="white", width=25, font=("Times", 16),command=Exit)
      Button_6.place(x=600,y=300,width=200)
      def bill_display():
           windows=Toplevel()
           windows.title('BILL')
           windows.maxsize(500,500)
           windows.minsize(500,500)
           t=Text(windows,font=('calibra',15))
           t.pack()
           t.insert(END,"====WELCOM TO PAPER MOON STATIONARY====")
           t.insert(END,f"\n")
           t.insert(END,f"\n\t\tCustomer id~:{e7.get()}")
           t.insert(END,f"\n")
           t.insert(END,f"\nCustomer Name~:{e6.get()}")
           t.insert(END,f"\nItems : {e8.get()}")
           t.insert(END,f"\n")
           t.insert(END,"\n===================================")
           t.insert(END,f"\n")
           t.insert(END,f"\nPrice~:{e9.get()}")
           t.insert(END,f" Qty~:{e10.get()}")
           t.insert(END,f"\n")
           t.insert(END,"\n===================================")
           t.insert(END,f"\n")
           t.insert(END,f"\nGST%~:{g3.get()}")
           t.insert(END,f"\nGST_amt~:{g1.get()}")
           t.insert(END,f"\n")
           t.insert(END,"\n===================================")
           t.insert(END,f"\nTotal~:{t1.get()}")
           t.insert(END,f"\n")
           t.insert(END,"\n\t\t:::THANK YOU VISIT AGAIN:::")
      b=Button(windows,text='GENERATE BILL',bg='blue',fg='white',width='30',font=("Times New Roman",21),command=bill_display)
      b.place(x=500,y=600)

#....................................................................................................................

def login():
    windows.c+=1
    cn=my.connect(host='localhost',user='root',passwd='Neel3319',database='project' )
    cur=cn.cursor()
    cur.execute("select uname,password from login where uname='{}' and password='{}'".format(e1.get(),e2.get()))
    data=cur.fetchall()
    data=list(data)
    rc=cur.rowcount
    if rc==1:
        windows.overrideredirect(1)
        ms.showinfo("Welcome", "Login Sucessfull")
        enter1()
    else:
          ms.askretrycancel("Wrong Password or Username","Try again?")
    if windows.c > 3:
        windows.overrideredirect(1)
        windows.withdraw()
        windows.destroy()
b1=Button(windows,text='LOGIN',fg='orange',bg='black',font=('calibra',20),width=10,border=5,command=login)
b1.place(x=600,y=550)

#....................................................................................................................
