from tkinter import*    
from tkinter import ttk   
from PIL import Image,ImageTk 
from tkinter import messagebox
import mysql.connector 
import cv2
import subprocess
import os
import numpy as np 




class Train:  
  def __init__(self, root):
    self.root = root
    self.root.geometry("1530x790+0+0")
    self.root.title("Face_Recognition_System") 

    title_lbl=Label(self.root,text="Train Data set",font=("times new roman",35,"bold"),bg="white",fg="red") 
    title_lbl.place(x=0,y=0,width=1530,height=45)

    img_top=Image.open("t1.jpg")
    img_top = img_top.resize((1530,325))   
    self.photo_top=ImageTk.PhotoImage(img_top)

    f_lbl=Label(self.root,image=self.photo_top) 
    f_lbl.place(x=0,y=46,width=1530,height=325)  

    img_bottom=Image.open("t2.jpg")
    img_bottom = img_bottom.resize((1530,325))   
    self.photo_bottom=ImageTk.PhotoImage(img_bottom)

    f_lbl=Label(self.root,image=self.photo_bottom) 
    f_lbl.place(x=0,y=440,width=1530,height=325) 
    
    #button
    b1_1 = Button(self.root, text="Train data",command=self.train_classifier,cursor="hand2", font=("times new roman",100,"bold"),bg="green", fg="blue")
    b1_1.place(x=0, y=350, width=1530, height=90)


     

  def train_classifier(self):
        data_dir = "data"
        result = subprocess.run(["ls", data_dir], capture_output=True, text=True)
        if result.returncode == 0:
            path = [os.path.join(data_dir, file) for file in result.stdout.splitlines()]
        else:
            messagebox.showerror("Error", "Error listing directory: " + result.stderr)
            return

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

        ids = np.array(ids)

        # Train LBPH face recognizer
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.save("classifier.xml")
        messagebox.showinfo("Result", "Training data set completed")



if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()  
