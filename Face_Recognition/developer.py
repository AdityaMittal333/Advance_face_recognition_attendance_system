from tkinter import*    
from tkinter import ttk   
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2

class Developer:  
  def __init__(self, root): 
    self.root = root
    self.root.geometry("1530x790+0+0")
    self.root.title("Face_Recognition_System")

    title_lbl=Label(self.root,text="Developer",font=("times new roman",35,"bold"),bg="white",fg="red") 
    title_lbl.place(x=0,y=0,width=1530,height=45)

    img_top=Image.open("d1.jpeg")
    img_top = img_top.resize((1530,720))   
    self.photo_top=ImageTk.PhotoImage(img_top)

    f_lbl=Label(self.root,image=self.photo_top) 
    f_lbl.place(x=0,y=46,width=1530,height=720)
     
    #frame
    main_frame=Frame(f_lbl,bd=2,bg="white")
    main_frame.place(x=1000,y=0,width=500,height=600)

    img_top1=Image.open("photo.jpeg")
    img_top1 = img_top1.resize((200,200))   
    self.photo_top1=ImageTk.PhotoImage(img_top1)

    f_lbl=Label(main_frame,image=self.photo_top1) 
    f_lbl.place(x=240,y=0,width=200,height=200)

     #developer
    dev_label=Label(main_frame,text="Hello my name, Aditya",font=("times new roman",20,"bold"),bg="white",fg="black") 
    dev_label.place(x=0,y=5)

    dev_label1=Label(main_frame,text="I am a full Satck Developer",font=("times new roman",20,"bold"),bg="white",fg="black") 
    dev_label1.place(x=0,y=40)

    img_top2=Image.open("d2.png")
    img_top2= img_top2.resize((500,390))   
    self.photo_top2=ImageTk.PhotoImage(img_top2)

    f_lbl=Label(main_frame,image=self.photo_top2) 
    f_lbl.place(x=0,y=210,width=500,height=390)


if __name__ == "__main__":   
      root = Tk()    
      obj = Developer(root)  
      root.mainloop()  