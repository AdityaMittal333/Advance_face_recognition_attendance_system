from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import subprocess
import os
import numpy as np

class Face_recognizer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_Recognition_System")

        title_lbl = Label(self.root, text="Face Detection", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=51)

        img_left = Image.open("f1.jpeg")
        img_left = img_left.resize((650, 700))
        self.photo_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(self.root, image=self.photo_left)
        f_lbl.place(x=0, y=55, width=650, height=700)

        img_right = Image.open("f2.jpg.webp")
        img_right = img_right.resize((950, 700))
        self.photo_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(self.root, image=self.photo_right)
        f_lbl.place(x=650, y=55, width=950, height=700)

        # button
        b1_1 = Button(f_lbl, text="Face Recognition", cursor="hand2", font=("times new roman", 18, "bold"), bg="green", fg="green", command=self.face_recog)
        b1_1.place(x=365, y=620, width=200, height=40)

        
        self.train_classifier()

    def mark_attendence(self,i,r,n,d):
        with open("Aditya.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList: 
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list) ):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Preset")

                 

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

    #face recoginition
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighors)

            coord=[]  

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="amittal123",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where Student_Id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select RollNO from student where Student_Id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dep from student where Student_Id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select Student_Id from student where Student_Id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                if confidence>85:
                    cv2.putText(img,f"Id:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Dep:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendence(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,y]

            return coord
     
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"face",clf) 
            return img
     
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create() 
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:  
            ret, img = video_cap.read()
            if not ret:
                print("Error: Failed to capture frame")
                break

            if img is None:
                print("Error: Empty frame received")
                continue

            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to face recognition", img)

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__": 
    root = Tk()
    obj = Face_recognizer(root)
    root.mainloop()  
