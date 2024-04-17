from tkinter import*    #library for gui development
from tkinter import ttk  #have stylish 
# importing pillow library using this command = pip install pillow
from PIL import Image,ImageTk # using to crop or edit image
import subprocess
from student import Student  
import os
from train import Train
from face_recognizer import Face_recognizer 
from developer import Developer
from attendence import Attendence
from help import Help


class Face_Recognition_System: #class name Face_Recognition_System
  def __init__(self, root): #constructor 
    self.root = root
    self.root.geometry("1530x790+0+0")
    self.root.title("Face_Recognition_System")
  
     #image 1
    img=Image.open("vassar-college-thompson-memorial-library.webp")
    img = img.resize((500, 130)) # doing resizeing ANTIALIAS convert high level image to low level image  
    self.photoimg=ImageTk.PhotoImage(img)  #img varoiable to photoimg 
    f_lbl=Label(self.root,image=self.photoimg) #label is given 
    f_lbl.place(x=0,y=0,width=500,height=130)  #adjusting l,b,h and cordinates 

    #image 2
    img=Image.open("images.jpeg")
    img1 = img.resize((500, 130))   
    self.photoimg1=ImageTk.PhotoImage(img1)  
    f_lbl=Label(self.root,image=self.photoimg1) 
    f_lbl.place(x=500,y=0,width=500,height=130)  

    #image 2
    img=Image.open("oklahoma-state-university-student-union.webp")
    img2 = img.resize((500, 130))   
    self.photoimg2=ImageTk.PhotoImage(img2)  
    f_lbl=Label(self.root,image=self.photoimg2)
    f_lbl.place(x=1000,y=0,width=500,height=130)  
    
    #background image
    img= Image.open("Web%20Application%20Firewall%20vs.webp")
    img3 = img.resize((1530, 790))  
    self.photoimg3=ImageTk.PhotoImage(img3)  
    bg_img=Label(self.root,image=self.photoimg3)
    bg_img.place(x=0,y=130,width=1530,height=790)  
    title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red") #making lable of above background image 
    title_lbl.place(x=0,y=0,width=1530,height=45)  #setting the place where to display the label 
    
    #student button
    img4=Image.open("istockphoto-1368965646-612x612.jpg")
    img4 = img4.resize((220, 220)) # doing resizeing ANTIALIAS convert high level image to low level image  
    self.photoimg4=ImageTk.PhotoImage(img4)  #img varoiable to photoimg 

    b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
    b1.place(x=200,y=100,width=220,height=220)

    b1_1=Button(bg_img,text="Student details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="blue")
    b1_1.place(x=200,y=300,width=220,height=40)

    #detech face buttom
    img5=Image.open("b2.jpeg")
    img5 = img5.resize((220, 220))  
    self.photoimg5=ImageTk.PhotoImage(img5)  

    b1=Button(bg_img,image=self.photoimg5,command=self.face_data,cursor="hand2")
    b1.place(x=500,y=100,width=220,height=220)
     
    b1_1=Button(bg_img,text="Face detection",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="blue")
    b1_1.place(x=500,y=300,width=220,height=40)
    
    #Attendence face buttom
    img6=Image.open("b3.jpg.webp")
    img6 = img6.resize((220, 220))  
    self.photoimg6=ImageTk.PhotoImage(img6) 

    b1=Button(bg_img,image=self.photoimg6,command=self.Attendence_data,cursor="hand2")
    b1.place(x=800,y=100,width=220,height=220)
     
    b1_1=Button(bg_img,text="Attendence",command=self.Attendence_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="blue")
    b1_1.place(x=800,y=300,width=220,height=40)

    #help face buttom
    img7=Image.open("b4.png")
    img7 = img7.resize((220, 220))  
    self.photoimg7=ImageTk.PhotoImage(img7) 

    b1=Button(bg_img,image=self.photoimg7,command=self.help_data,cursor="hand2")
    b1.place(x=1100,y=100,width=220,height=220)
     
    b1_1=Button(bg_img,text="Help Desk",command=self.help_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="blue")
    b1_1.place(x=1100,y=300,width=220,height=40)

     #Train face buttom
    img8=Image.open("b5.png")
    img8 = img8.resize((220, 220))  
    self.photoimg8=ImageTk.PhotoImage(img8) 

    b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_details)
    b1.place(x=200,y=380,width=220,height=220)
     
    b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_details,font=("times new roman",15,"bold"),bg="darkblue",fg="blue")
    b1_1.place(x=200,y=580,width=220,height=40)
    
    #Developer face buttom
    img10=Image.open("b7.jpg")
    img10 = img10.resize((220, 220))  
    self.photoimg9=ImageTk.PhotoImage(img10) 

    b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.Developer_data)
    b1.place(x=600,y=380,width=220,height=220)
     
    b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.Developer_data,font=("times new roman",15,"bold"),bg="darkgreen",fg="blue")
    b1_1.place(x=600,y=580,width=220,height=40)

    #Photo  buttom
    img11=Image.open("8x10-photo-collage-small.jpg")
    img11 = img11.resize((220, 220))  
    self.photoimg11=ImageTk.PhotoImage(img11) 

    b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.open_img)
    b1.place(x=1000,y=380,width=220,height=220)
     
    b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="blue")
    b1_1.place(x=1000,y=580,width=220,height=40)

  def open_img(self):
      subprocess.Popen(["open", "data"])
       

    #function button
  def student_details(self): #function for student detial     
       self.new_window=Toplevel(self.root) 
       self.app=Student(self.new_window) 

  def train_details(self): #function for student detial     
       self.new_window=Toplevel(self.root) 
       self.app=Train(self.new_window) 

  def face_data(self): #function for student detial     
       self.new_window=Toplevel(self.root) 
       self.app=Face_recognizer(self.new_window)

  def Attendence_data(self): #function for student detial     
       self.new_window=Toplevel(self.root) 
       self.app=Attendence(self.new_window)
  def Developer_data(self): #function for student detial     
       self.new_window=Toplevel(self.root) 
       self.app=Developer(self.new_window)

  def help_data(self): #function for student detial     
       self.new_window=Toplevel(self.root) 
       self.app=Help(self.new_window)



if __name__ == "__main__":   #main started from here 
      root = Tk()    #tk to root
      obj = Face_Recognition_System(root)  #making object of class by passing root 
      root.mainloop()  #main ends here 