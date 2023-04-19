from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1366x768+0+0")

        # ============ Variables =================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_email=StringVar()
        self.var_question=StringVar()
        self.var_answer=StringVar()
        self.var_pwd=StringVar()
        self.var_cpwd=StringVar()
        self.var_check=IntVar()

        self.bg=ImageTk.PhotoImage(file=r"/home/pi/Desktop/Golden Eye/Pics_GUI/Register/background.jpg")
        
        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0, relwidth=1,relheight=1)

        frame= Frame(self.root,bg="#F2F2F2")
        frame.place(x=100,y=80,width=900,height=580)
        

        get_str = Label(frame,text="Registration",font=("times new roman",30,"bold"),fg="#002B53",bg="#F2F2F2")
        get_str.place(x=350,y=130)

        #label1 
        fname =lb1= Label(frame,text="First Name:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        fname.place(x=100,y=200)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.txtuser.place(x=103,y=225,width=270)


        #label2 
        lname =lb1= Label(frame,text="Last Name:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        lname.place(x=100,y=270)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=103,y=295,width=270)

        # ==================== section 2 -------- 2nd Columan===================


        #label1
        email =lb1= Label(frame,text="Email:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        email.place(x=530,y=270)

        #entry1
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=533,y=295,width=270)

        # ========================= Section 3 --- 1 Columan=================

        #label1 
        question =lb1= Label(frame,text="Select Security Question:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        question.place(x=100,y=350)

        #Combo Box1
        self.combo_security = ttk.Combobox(frame,textvariable=self.var_question,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security["values"]=("Select","Your Date of Birth","Your nickname","Your Favorite Book")
        self.combo_security.current(0)
        self.combo_security.place(x=103,y=375,width=270)


        #label2 
        answer =lb1= Label(frame,text="Security Answer:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        answer.place(x=100,y=420)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_answer,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=103,y=445,width=270)

        # ========================= Section 4-----Column 2=============================

        #label1 
        pwd =lb1= Label(frame,text="Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        pwd.place(x=530,y=350)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_pwd,font=("times new roman",15,"bold"))
        self.txtuser.place(x=533,y=375,width=270)


        #label2 
        cpwd =lb1= Label(frame,text="Confirm Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
        cpwd.place(x=530,y=420)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_cpwd,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=533,y=445,width=270)

        # Checkbutton
        checkbtn = Checkbutton(frame,variable=self.var_check,text="I Agree the Terms & Conditions",font=("times new roman",13,"bold"),fg="#002B53",bg="#F2F2F2")
        checkbtn.place(x=100,y=480,width=270)


        # Creating Button Register
        loginbtn=Button(frame,command=self.reg,text="Register",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=103,y=510,width=270,height=35)

        # Creating Button Login
        loginbtn=Button(frame,text="Login",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=533,y=510,width=270,height=35)




    def reg(self):
        if (self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_email.get()=="" or self.var_question.get()=="" or self.var_answer.get()=="" or self.var_pwd.get()=="" or self.var_cpwd.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif(self.var_pwd.get() != self.var_cpwd.get()):
            messagebox.showerror("Error","Please Enter Password & Confirm Password are Same!")
        elif(self.var_check.get()==0):
            messagebox.showerror("Error","Please Check the Agree Terms and Conditons!")
        else:
            # messagebox.showinfo("Successfully","Successfully Register!")
            try:
                conn = mysql.connector.connect(host="localhost", username="Aadil", password="prime2", database="Golden_EyeDB")
                mycursor = conn.cursor()
                query=("select * from student_register where email=%s")
                value=(self.var_email.get(),)
                mycursor.execute(query,value)
                row = mycursor.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exist,please try another email")
                else:
                    mycursor.execute("insert into student values(%s, %s, %s, %s, %s,  %s)",(
                                                                                            self.var_fname.get(),
                                                                                            self.var_lname.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_question.get(),
                                                                                            self.var_answer.get(),
                                                                                            self.var_pwd.get()
                                                                                            ))

                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","Successfully Registered!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)




if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()
