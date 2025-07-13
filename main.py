#-----------Created By Atharv Sawant on 10th September,2023
from logging import root
from tkinter import *          #----------tkinter use for creating an interferance window-------------
import qrcode as qr             #----------which will create qr code----------------
from PIL import Image,ImageTk   #------------will convert in image form--------------
from resizeimage import resizeimage #---------use for resizing the image----------------


class Qr_Generator: #------------class has been used----------------------


    def __init__(self, root):
        self.root=root
        self.root.geometry("900x500+200+50")   #-----------dimension for window------------
        self.root.title("QR CODE GENERATOR")
        self.root.resizable(False,False) #---------it will not maximize the window------------
        #self.root.configure(bg="#d8bfd8")
        self.root.configure(bg="white")

        title=Label(self.root,text="Qr  Code  Generator",font=("times new roman",40),bg="#CE71AF",fg="#89138A").place(x=0,y=0,relwidth=1)

        self.var_bk_name=StringVar()
        self.var_bk_author=StringVar()
        self.var_bk_link=StringVar()
        self.var_bk_id=StringVar()
        self.var_bk_med=StringVar()

        #-------------Book Information Window---------------

        bk_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        bk_frame.place(x=50,y=100,width=500,height=380)

        bk_title=Label(bk_frame,text="BOOK   DETAILS",font=("goudy old style",30),bg="#CE71AF",fg="#89138A").place(x=0,y=0,relwidth=1)

        lbl_bk_name=Label(bk_frame,text="Book Name",font=("times new roman",15),bg="white",fg="black").place(x=20,y=70)
        lbl_bk_author=Label(bk_frame,text="Author Name",font=("times new roman",15),bg="white",fg="black").place(x=20,y=110)
        lbl_bk_link=Label(bk_frame,text="Book Drive Link",font=("times new roman",15),bg="white",fg="black").place(x=20,y=150)

        txt_bk_name=Entry(bk_frame,font=("times new roman",15),textvariable=self.var_bk_name,bg="light yellow",fg="black").place(x=250,y=70)
        txt_bk_author=Entry(bk_frame,font=("times new roman",15),textvariable=self.var_bk_author,bg="light yellow",fg="black").place(x=250,y=110)
        txt_bk_link=Entry(bk_frame,font=("times new roman",15),textvariable=self.var_bk_link,bg="light yellow",fg="black").place(x=250,y=150)
        #-----------------buttons functionality----------------------
        btn_generator=Button(bk_frame,text="Generate QR",command=self.generate,font=("times new roman",18,"bold"),bg="#CE71AF",fg="#89138A").place(x=60,y=210,width=200,height=30)
        btn_reset=Button(bk_frame,text="Reset",command=self.Reset,font=("times new roman",18,"bold"),bg="#CE71AF",fg="#89138A").place(x=300,y=210,width=150,height=30)
        btn_Save=Button(bk_frame,text="Save QR",command=self.save,font=("times new roman",18,"bold"),bg="#CE71AF",fg="#89138A").place(x=190,y=270,width=150,height=30)
        #--------------Message Display Screen-----------------------
        self.msg="Please Enter the detalis for QR Code"
        self.lbl_msg=Label(bk_frame,text=self.msg,font=("times new roman",20),bg="white",fg="green")
        self.lbl_msg.place(x=0,y=320,relwidth=1)

        #---------------Book QR Code Window------------------

        qr_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        qr_frame.place(x=600,y=100,width=250,height=380)

        bk_title=Label(qr_frame,text="BOOK  QR",font=("goudy old style",30),bg="#CE71AF",fg="#89138A").place(x=0,y=0,relwidth=1)

        self.qr_code=Label(qr_frame,text="QR Code \nNot Available",font=("times new roman",20),bg="#CE71AF",fg="white",bd=1,relief=RIDGE)
        self.qr_code.place(x=40,y=100,width=180,height=180)

    def Reset(self):     #-------------Object for rest button-----------------
        self.var_bk_name.set("")
        self.var_bk_author.set("")
        self.var_bk_link.set("")
        #self.var_bk_med.set("")
        self.msg="Please Enter the detalis for QR Code"
        self.lbl_msg.configure(text=self.msg,fg="green")
        self.qr_code.config(image="")


    def generate(self):     #-----------------Object for generate qr code button--------------
        if self.var_bk_name.get()=="" or self.var_bk_author.get()=="" or self.var_bk_link.get()=="":
            self.msg="All Fields are Required"
            self.lbl_msg.configure(text=self.msg,fg="red")
        else:
            qr_data=(f"{self.var_bk_link.get()}") #----------use of F string---------- syntax = name {variable.get()}
            qr_code=qr.make(qr_data)   #--------------this function will generate qr code--------------
            qr_code=resizeimage.resize_cover(qr_code,[180,180])  #----------will resize the image----------
            self.im=ImageTk.PhotoImage(qr_code)  #---------the image will be add in the tkwinter -----------
            self.qr_code.config(image=self.im)
            self.msg="QR Code Generated Sucessfully"
            self.lbl_msg.configure(text=self.msg,fg="green")


    def save(self):  #-----------Object for Save the qr code----------------
        if self.var_bk_name.get()=="" or self.var_bk_author.get()=="" or self.var_bk_link.get()=="":
            self.msg="All Fields are Required"
            self.lbl_msg.configure(text=self.msg,fg="red")
        else:
            qr_data=(f"link:- {self.var_bk_link.get()}")
            qr_code=qr.make(qr_data)
            qr_code.save("BK_"+str(self.var_bk_name.get())+"_AU_"+str(self.var_bk_author.get())+'.png')
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            self.im=ImageTk.PhotoImage(qr_code)
            self.qr_code.config(image=self.im)
            self.msg="QR Code Saved Sucessfully "
            self.lbl_msg.configure(text=self.msg,fg="green")


root=Tk()
obj = Qr_Generator(root)
root.mainloop()
