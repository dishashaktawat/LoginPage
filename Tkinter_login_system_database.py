from tkinter import *
from datetime import *
import time
from math import *
from PIL import Image,ImageTk,ImageDraw
import pymysql as mysql
from tkinter import messagebox
class Clock:
       def __init__(self,root):
              self.root = root
              self.root.title('GUI Analog Clock')
              self.root.geometry('1350x700+0+0')
              self.root.config(bg='#021e2f')
              #==========bg colors==========
              left_lbl=Label(self.root,bg='#08A3D2',bd=0)
              left_lbl.place(x=0,y=0,relheight=1,width=600)

              right_lbl=Label(self.root,bg='#031F3C',bd=0)
              right_lbl.place(x=600,y=0,relheight=1,relwidth=1)

              #=========Frames==============
              login_frame=Frame(self.root,bg='white')
              login_frame.place(x=250,y=100,height=500,width=800)

              title = Label(login_frame,text='LOGIN HERE',font=('times new roman',30,'bold'),bg='white',fg='#08A3D2').place(x=250,y=50)

              email_Label = Label(login_frame,text="Email Address",font=('times new roman',18),bg='white',fg='gray').place(x=250,y=130)
              self.email_frame = Entry(login_frame,font=('times new roman',15),bg='lightgray')
              self.email_frame.place(x=250,y=180,width=350,height=35)

              password_label = Label(login_frame,text='Password',font=('times new roman',18),bg='white',fg='gray').place(x=250,y=230)
              self.pass_frame = Entry(login_frame,font=('times new roman',15),bg='lightgray')
              self.pass_frame.place(x=250,y=270,width=350,height=35)

              btn_register = Button(login_frame,text='Register new Account?',command=self.register_window,font=('times new roman',14),fg='#B00857',bd=0,cursor='hand2').place(x=250,y=320)
              btn_login = Button(login_frame,text='Login',command=self.login,font=('times new roman',20,'bold'),bd=0,fg='white',bg='#B00857',cursor='hand2').place(x=300,y=380,width=180,height=40)
              #=========clock========
              self.lbl=Label(self.root,text='\nClock',font=('Book Antique',25,'bold'),fg='white',compound=BOTTOM,bg='black',bd=0)
              self.lbl.place(x=90,y=120,height=450,width=350)
              self.working()

       def register_window(self):
              self.root.destroy()
              import database_project

       def login(self):
              if self.email_frame.get()=='' or self.pass_frame.get()=='':
                     messagebox.showerror('Error','All fields are required',parent=self.root)

              else:
                     try:
                            con = mysql.connect(host='localhost',user='root',password='',database='employee')
                            cur = con.cursor()
                            cur.execute('select * from employeee where email=%s and password=%s',
                                        (self.email_frame.get(),self.pass_frame.get()))
                            row=cur.fetchone()
                            if row == None:
                                   messagebox.showerror('Error','Invalid USERNAME & PASSWORD',parent=self.root)
                                   
                            else:
                                   messagebox.showerror('Success','Welcome',parent=self.root)
                            con.close()
                     except Exception as es:
                            messagebox.showerror('Error',f'Error due to {str(es)}',parent=self.root)
                             #messagebox.showinfo('Success','Successfully Login',parent=self.root)


              

       def clock_image(self,hr,min_,sec_):
              clock=Image.new('RGB',(400,400),(1,1,1))
              draw=ImageDraw.Draw(clock)
              #====for Clock image======
              bg=Image.open(r'E:\python\clock_black_bg.png')
              bg=bg.resize((300,300),Image.ANTIALIAS)
              clock.paste(bg,(50,50))
              origin=200,200
              draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill='lightgray',width=3)
               #=====for min Line Image=====
              draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill='blue',width=3)
               #=====for sec Line Image=====
              draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill='green',width=3)
              draw.ellipse((195,195,210,210),fill='white')
              clock.save('clock_new.png')

       def working(self):
              h=datetime.now().time().hour
              m=datetime.now().time().minute
              s=datetime.now().time().second
              hr=(h/12)*360
              min_=(m/60)*360
              sec_=(s/60)*360
              self.clock_image(hr,min_,sec_)
              self.img=ImageTk.PhotoImage(file='clock_new.png')
              self.lbl.config(image=self.img)
              self.lbl.after(200,self.working)
##              print(h,m,s)
##              print(hr,min_,sec_)
##
root = Tk()
obj = Clock(root)
root.mainloop()
