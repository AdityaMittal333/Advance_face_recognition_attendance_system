from tkinter import*    
from tkinter import ttk   
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2

class Help:  
  def __init__(self, root): 
    self.root = root
    self.root.geometry("1530x790+0+0")
    self.root.title("Face_Recognition_System")

    title_lbl=Label(self.root,text="Help desk",font=("times new roman",35,"bold"),bg="white",fg="red") 
    title_lbl.place(x=0,y=0,width=1530,height=45)

    img_top=Image.open("h1.jpg")
    img_top = img_top.resize((1530,720))   
    self.photo_top=ImageTk.PhotoImage(img_top)

    f_lbl=Label(self.root,image=self.photo_top) 
    f_lbl.place(x=0,y=46,width=1530,height=720)

    dev_label=Label(f_lbl,text="Email:ag332003@gmail.com",font=("times new roman",20,"bold"),bg="white",fg="black") 
    dev_label.place(x=630,y=250)



if __name__ == "__main__":   
      root = Tk()    
      obj = Help(root)  
      root.mainloop() 