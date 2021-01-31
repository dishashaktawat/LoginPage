from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import pymysql as mysql
class Register:
       def __init__(self,root):
              self.root = root
              self.root.title('Registration Window')
              self.root.geometry('1350x700+0+0')
              #------bg Image-----
              self.bg = ImageTk.PhotoImage(file=r'E:\pyhton login database project\database.jpg')
              bg =Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

              #-------Left Image-----
              self.left = ImageTk.PhotoImage(file=r'E:\pyhton login database project\database_project_image6.jpg')
              left = Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)

              #------Register Frame------
              frame1 = Frame(self.root,bg='white')
              frame1.place(x=480,y=100,width=700,height=500)

              title = Label(frame1,text="REGISTER HERE",font=('times new roman',25),fg='green',bg='white').place(x=50,y=30)
              #------row one--------
              f_name = Label(frame1,text="First Name",font=('times new roman',15),fg='gray',bg='white').place(x=50,y=100)
              self.f_txt_frame = Entry(frame1,font=('times new roman',15),bg='lightgray')
              self.f_txt_frame.place(x=50,y=130,width=250)

              l_name = Label(frame1,text="Last Name",font=('times new roman',15),fg='gray',bg='white').place(x=400,y=100)
              self.l_txt_frame = Entry(frame1,font=('times new roman',15),bg='lightgray')
              self.l_txt_frame.place(x=400,y=130,width=250)

              #------row two--------
              contact_no = Label(frame1,text="Contact",font=('times new roman',15),fg='gray',bg='white').place(x=50,y=170)
              self.contact_frame = Entry(frame1,font=('times new roman',15),bg='lightgray')
              self.contact_frame.place(x=50,y=200,width=250)

              email = Label(frame1,text="Email",font=('times new roman',15),fg='gray',bg='white').place(x=400,y=170)
              self.email_frame = Entry(frame1,font=('times new roman',15),bg='lightgray')
              self.email_frame.place(x=400,y=200,width=250)

              #------row three--------
              question = Label(frame1,text="Question",font=('times new roman',15),fg='gray',bg='white').place(x=50,y=240)
              self.quest_frame = ttk.Combobox(frame1,font=('times new roman',15))
              self.quest_frame['values']=('Select','Your first pet name','your best friend name','Your birth place')
              self.quest_frame.current(0)
              self.quest_frame.place(x=50,y=270,width=250)
              

              answer = Label(frame1,text="Answer",font=('times new roman',15),fg='gray',bg='white').place(x=400,y=240)
              self.ans_frame = Entry(frame1,font=('times new roman',15),bg='lightgray')
              self.ans_frame.place(x=400,y=270,width=250)

              #------row four--------
              password = Label(frame1,text="Password",font=('times new roman',15),fg='gray',bg='white').place(x=50,y=310)
              self.password_frame = Entry(frame1,font=('times new roman',15),bg='lightgray')
              self.password_frame.place(x=50,y=340,width=250)

              cpassword = Label(frame1,text="Confirm Password",font=('times new roman',15),fg='gray',bg='white').place(x=400,y=310)
              self.cpassword_frame = Entry(frame1,font=('times new roman',15),bg='lightgray')
              self.cpassword_frame.place(x=400,y=340,width=250)

              #-----terms conditons---------
              self.var_check = IntVar()
              chk = Checkbutton(frame1,text='Agree all terms and conditions',variable=self.var_check,onvalue=1,offvalue=0,
                                font=('times new roman',15)).place(x=50,y=380)

              register_btn = Button(frame1,text='Register',command=self.register_data,font=('times new roman',15),bd=0,
                                    bg='green').place(x=250,y=420,width=250)
              login_btn = Button(self.root,text='Sign In',command=self.sign_in,font=('times new roman',15),bd=0,
                                 bg='white').place(x=220,y=460,width=100)

       def sign_in(self):
              self.root.destroy()
              import Tkinter_login_system_database

       def clear(self):
              self.f_txt_frame.delete(0,END)
              self.l_txt_frame.delete(0,END)
              self.contact_frame.delete(0,END)
              self.email_frame.delete(0,END)
              self.password_frame.delete(0,END)
              self.cpassword_frame.delete(0,END)
              self.quest_frame.current(0)
              self.ans_frame.delete(0,END)

       def register_data(self):
              if self.f_txt_frame.get()=='' or self.contact_frame.get()=='' or self.email_frame.get()==''or self.quest_frame.get()=='' or self.ans_frame.get()=='':
                     messagebox.showerror('Error','All fields are required',parent=self.root)
              elif self.password_frame.get()!=self.cpassword_frame.get():
                     messagebox.showerror('Error','Password should be same',parent=self.root)
              elif self.var_check.get() == 0:
                     messagebox.showerror('Error','Please Agree on terms and conditions',parent=self.root)
              else:
                     try:
                            con = mysql.connect(host='localhost',user='root',password='',database='employee')
                            cur = con.cursor()
                            cur.execute('select * from employeee where email=%s',self.email_frame.get())
                            row = cur.fetchone()
                            #print(row)
                            if row!=None:
                                   messagebox.showerror('Error','User Already Exist! Try with another email',parent=self.root)
                              
                            cur.execute('insert into employeee (f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)',
                                        (self.f_txt_frame.get(),
                                        self.l_txt_frame.get(),
                                        self.contact_frame.get(),
                                        self.email_frame.get(),
                                        self.quest_frame.get(),
                                        self.ans_frame.get(),
                                        self.password_frame.get()))
                            con.commit()
                            con.close()
                            messagebox.showinfo('Success','Registration successfully',parent=self.root) 
                            self.clear()
                            

                     except Expectation as es:
                            messagebox.showerror('Error',f'error is {str(es)}',parent=self.root)                       
              


root = Tk()
obj = Register(root)
root.mainloop() 
              

