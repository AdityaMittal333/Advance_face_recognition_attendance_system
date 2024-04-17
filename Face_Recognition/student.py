from tkinter import*    
from tkinter import ttk   
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2

#open cv= ek open source libraray h es m more tha 2500 algorithm h classic and machine learning alogrithm h
#maily use for face detection

class Student: #class name Face_Recognition_System  
  def __init__(self, root): #constructor 
    self.root = root
    self.root.geometry("1530x790+0+0")
    self.root.title("Face_Recognition_System")

    #variables
    self.var_Dep=StringVar()
    self.var_Course=StringVar()
    self.var_Year=StringVar()
    self.var_Sem=StringVar()
    self.var_Student_Id=StringVar()
    self.var_Name=StringVar()
    self.var_Divison=StringVar()
    self.var_RollNO=StringVar()
    self.var_Gender=StringVar()
    self.var_Dob=StringVar()
    self.var_Email=StringVar()
    self.var_Phone=StringVar()
    self.var_Address=StringVar()
    self.var_Teacher=StringVar()
    
    

     #image 1
    img=Image.open("S1.jpg")
    img = img.resize((500, 130)) # doing resizeing ANTIALIAS convert high level image to low level image  
    self.photoimg=ImageTk.PhotoImage(img)  #img varoiable to photoimg 
    f_lbl=Label(self.root,image=self.photoimg) #label is given 
    f_lbl.place(x=0,y=0,width=500,height=130)  #adjusting l,b,h and cordinates 

    #image 2
    img=Image.open("S2.jpg")
    img1 = img.resize((500, 130))   
    self.photoimg1=ImageTk.PhotoImage(img1)  
    f_lbl=Label(self.root,image=self.photoimg1) 
    f_lbl.place(x=500,y=0,width=500,height=130)  

    #image 3
    img=Image.open("S3.jpeg")
    img2 = img.resize((500, 130))   
    self.photoimg2=ImageTk.PhotoImage(img2)  
    f_lbl=Label(self.root,image=self.photoimg2)
    f_lbl.place(x=1000,y=0,width=500,height=130)

    #background image
    img= Image.open("Web%20Application%20Firewall%20vs.webp")
    img3 = img.resize((1530, 790))  
    self.photoimg3=ImageTk.PhotoImage(img3)  
    bg_img=Label(self.root,image=self.photoimg3)
    bg_img.place(x=0,y=130,width=1530,height=710)  
    
    title_lbl=Label(bg_img,text="Student Management System",font=("times new roman",35,"bold"),bg="white",fg="darkgreen") #making lable of above background image 
    title_lbl.place(x=0,y=0,width=1530,height=45)  #setting the place where to display the label

    main_frame=Frame(bg_img,bd=2,bg="white") #bd means border frame on background 
    main_frame.place(x=10,y=55,width=1415,height=750) #coordinates of main frame
    
    #left label frame
    Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"),fg="black")
    Left_frame.place(x=10,y=10,width=690,height=640)
    
    img_left=Image.open("S4.webp")
    img_left = img_left.resize((680, 130))   
    self.photo_left=ImageTk.PhotoImage(img_left)

    f_lbl=Label(Left_frame,image=self.photo_left) 
    f_lbl.place(x=5,y=0,width=680,height=150)  
    
    #current course
    current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Infromation",font=("times new roman",12,"bold"),fg="black")
    current_course_frame.place(x=5,y=135,width=680,height=120)

    #department
    dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white",fg="black") 
    dep_label.grid(row=0,column=0,padx=10,sticky=W)

    dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Dep,font=("times new roman",12,"bold"),state="read only",width=20)
    dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")
    dep_combo.current(0) #first select ek andr likha hoga select departemnt 
    dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

    #course
    course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white",fg="black") 
    course_label.grid(row=0,column=2,padx=10,sticky=W)

    course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Course,font=("times new roman",12,"bold"),state="readyonly",width=20)
    course_combo["values"]=("Select Course","FE","SE","TE","BE")
    course_combo.current(0) #first select ek andr likha hoga select departemnt 
    course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

    #Year
    year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white",fg="black") 
    year_label.grid(row=1,column=0,padx=10,sticky=W)

    year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Year,font=("times new roman",12,"bold"),state="readyonly",width=20)
    year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
    year_combo.current(0) #first select ek andr likha hoga select departemnt 
    year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

     #Semester
    semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white",fg="black") 
    semester_label.grid(row=1,column=2,padx=10,sticky=W)

    semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_Sem,font=("times new roman",12,"bold"),state="readyonly",width=20)
    semester_combo["values"]=("Select Semester","Semester-1","Semester-2")
    semester_combo.current(0) #first select ek andr likha hoga select departemnt 
    semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

     #Class Student Information
    class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"),fg="black")
    class_student_frame.place(x=5,y=260,width=680,height=360)
     
     #student id
    studentid_label=Label(class_student_frame,text="StudentID",font=("times new roman",12,"bold"),bg="white",fg="black") 
    studentid_label.grid(row=0,column=0,padx=10,sticky=W)
 
    studentid_entry=ttk.Entry(class_student_frame,textvariable=self.var_Student_Id,width=20,font=("times new roman ",13,"bold"))
    studentid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

    #student name
    studentname_label=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white",fg="black") 
    studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
 
    studentname_entry=ttk.Entry(class_student_frame,textvariable=self.var_Name,width=20,font=("times new roman ",13,"bold"))
    studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

    #class division
    class_div_label=Label(class_student_frame,text="Class Divison:",font=("times new roman",12,"bold"),bg="white",fg="black") 
    class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

    div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_Divison,font=("times new roman",12,"bold"),state="readyonly",width=18)
    div_combo["values"]=("A","B","C")
    div_combo.current(0) 
    div_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)


    #Roll no
    roll_no_label=Label(class_student_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white",fg="black") 
    roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
 
    roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_RollNO,width=20,font=("times new roman ",13,"bold"))
    roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

    #Gender
    gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white",fg="black") 
    gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
 
    gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_Gender,font=("times new roman",12,"bold"),state="readyonly",width=18)
    gender_combo["values"]=("Male","Female","Other")
    gender_combo.current(0) #first select ek andr likha hoga select departemnt 
    gender_combo.grid(row=2,column=1,padx=10,pady=10,sticky=W)

    #DOB
    dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white",fg="black") 
    dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
 
    dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_Dob,width=20,font=("times new roman ",13,"bold"))
    dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

    #email
    email_label=Label(class_student_frame,text="EMAIL:",font=("times new roman",12,"bold"),bg="white",fg="black") 
    email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
 
    email_entry=ttk.Entry(class_student_frame,textvariable=self.var_Email,width=20,font=("times new roman ",13,"bold"))
    email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

     #phone no
    phone_label=Label(class_student_frame,text="Phone No:",font=("times new roman",12,"bold"),bg="white",fg="black") 
    phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
 
    phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_Phone,width=20,font=("times new roman ",13,"bold"))
    phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

     #address
    address_label=Label(class_student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white",fg="black") 
    address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
 
    address_entry=ttk.Entry(class_student_frame,textvariable=self.var_Address,width=20,font=("times new roman ",13,"bold"))
    address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

    #teacher name
    teacher_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",12,"bold"),bg="white",fg="black") 
    teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
 
    teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_Teacher,width=20,font=("times new roman ",13,"bold"))
    teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
    
    #radio Buttons
    #textvariable=self.var_radio1
    
    self.var_radio1=StringVar()
    Radiobutton1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo sample",value="Yes")
    Radiobutton1.grid(row=6,column=0)

    self.var_radio2=StringVar()
    Radiobutton2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo sample",value="NO")
    Radiobutton2.grid(row=6,column=1,padx=5)

    #button frame
    btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
    btn_frame.place(x=0,y=225,width=675,height=40)
    
    save_btn=Button(btn_frame,text="Save",command=self.add_data,font=("times,new roman",13,"bold"),bg="white",fg="black",width=14,padx=5,pady=5)
    save_btn.grid(row=0,column=0)

    update_btn=Button(btn_frame,text="Update",command=self.update_data,font=("times,new roman",13,"bold"),bg="white",fg="black",width=14,padx=5,pady=5)
    update_btn.grid(row=0,column=1)

    delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,font=("times,new roman",13,"bold"),bg="white",fg="black",width=14,padx=5,pady=5)
    delete_btn.grid(row=0,column=2)

    reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=13,font=("times,new roman",13,"bold"),bg="darkblue",fg="black",padx=5,pady=5)
    reset_btn.grid(row=0,column=3)
     
    btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
    btn_frame1.place(x=0,y=267,width=675,height=43) 

    take_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",font=("times,new roman",13,"bold"),bg="white",fg="black",width=32,padx=5,pady=5)
    take_btn.grid(row=0,column=0)
    
    take2_btn=Button(btn_frame1,text="Update Photo Sample",font=("times,new roman",13,"bold"),bg="white",fg="black",width=32,padx=5,pady=5)
    take2_btn.grid(row=0,column=1)

      
    #Right label frame
    Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"),fg="black")
    Right_frame.place(x=710,y=10,width=690,height=640)
    
    #image on right side
    img_right=Image.open("r1.jpg")
    img_right = img_right.resize((680, 120))   
    self.photo_right=ImageTk.PhotoImage(img_right)

    f_lbl=Label(Right_frame,image=self.photo_right) 
    f_lbl.place(x=5,y=0,width=680,height=135) 

    #search system
    search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"),fg="black")
    search_frame.place(x=5,y=135,width=680,height=60)

    search_frame1=Label(search_frame,text="Search By",font=("times new roman",12,"bold"),bg="red",fg="white") 
    search_frame1.grid(row=0,column=0,padx=10,pady=5,sticky=W)
    
    search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readyonly",width=12 )
    search_combo["values"]=("Select","Roll_No")
    search_combo.current(0) #first select ek andr likha hoga select departemnt 
    search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


    search_entry=ttk.Entry(search_frame,width=15,font=("times new roman ",13,"bold"))
    search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

    search_btn=Button(search_frame,text="Search",font=("times,new roman",13,"bold"),bg="white",fg="black",width=12,padx=5,pady=5)
    search_btn.grid(row=0,column=3,padx=3)

    showall_btn=Button(search_frame,text="Show ALL",width=12,font=("times,new roman",13,"bold"),bg="darkblue",fg="black",padx=5,pady=5)
    showall_btn.grid(row=0,column=4,padx=3)
    
    #table frame
    table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
    table_frame.place(x=5, y=200, width=680, height=350)
 
    scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL) #scroll bar
    scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

    self.student_table = ttk.Treeview(table_frame, column=("Dep", "Course", "Year", "semester", "Student_Id", "Name", "Divison", "RollNO", "Gender", "Dob", "Email", "Phone", "Address", "Teacher", "Photo_Sample"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set) #to set the element of search system
    #part of scroll bar
    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_x.config(command=self.student_table.xview)
    scroll_y.config(command=self.student_table.yview)

    #all heading in scroll bar
    self.student_table.heading("Dep", text="Department")
    self.student_table.heading("Course", text="Course")
    self.student_table.heading("Year", text="Year")
    self.student_table.heading("semester", text="Semester")
    self.student_table.heading("Student_Id", text="StudentId")
    self.student_table.heading("Name", text="Name")
    self.student_table.heading("Divison", text="Divison")
    self.student_table.heading("RollNO", text="RollNo")
    self.student_table.heading("Gender", text="Gender")
    self.student_table.heading("Dob", text="DOB")
    self.student_table.heading("Email", text="Email")
    self.student_table.heading("Phone", text="Phone")
    self.student_table.heading("Address", text="Address")  
    self.student_table.heading("Teacher", text="Teacher") 
    self.student_table.heading("Photo_Sample",text="PhotoSampleStatus")
    self.student_table["show"] = "headings"


    self.student_table.pack(fill=BOTH,expand=1)
    #function jab ham right side ke data pe click kare toh uss ki details left side m automatically fill hojayeg
    self.student_table.bind("<ButtonRelease>",self.get_cursor) 

    self.fetch_data()

  #function declartion for saving data in mysql
  def add_data(self):
     if self.var_Dep.get()=="Select Department" or self.var_Name.get()=="" or self.var_Student_Id.get()=="":
        messagebox.showerror("Error","All Fields are required",parent=self.root) #parent is used to show message window on parent window sometime message go on other window  
     else:
        try:
          conn=mysql.connector.connect(host="localhost",username="root",password="amittal123",database="face_recognizer")
          my_cursor=conn.cursor()
          my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                          self.var_Dep.get(),
                                                                                                          self.var_Course.get(),
                                                                                                          self.var_Year.get(),
                                                                                                          self.var_Sem.get(),
                                                                                                          self.var_Student_Id.get(),
                                                                                                          self.var_Name.get(),
                                                                                                          self.var_Divison.get(),
                                                                                                          self.var_RollNO.get(),
                                                                                                          self.var_Gender.get(),
                                                                                                          self.var_Dob.get(),
                                                                                                          self.var_Email.get(),
                                                                                                          self.var_Phone.get(),
                                                                                                          self.var_Address.get(),
                                                                                                          self.var_Teacher.get(),
                                                                                                          self.var_radio1.get()


                                                                                                        ))
          conn.commit() 
          self.fetch_data()   #function to show data on screen
          conn.close()
          messagebox.showinfo("Success","student details has been added succesfully",parent=self.root)
        except Exception as es:
           messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


  # fetch data , function to show data on screen 
  def fetch_data(self):
     conn=mysql.connector.connect(host="localhost",username="root",password="amittal123",database="face_recognizer")
     my_cursor=conn.cursor() #conn.cursor ko my_cursor mai store kar re h
     my_cursor.execute("select * from student")
     data=my_cursor.fetchall() #ab my-cursor ko data m store kar re h

     if len(data)!=0:  #agar data ki length zero nahi h toh loop run karega 
        self.student_table.delete(*self.student_table.get_children())
        for i in data:
           self.student_table.insert("",END,values=i)
        conn.commit()
        conn.close()  

#get cursore #function jab ham right side ke data pe click kare toh uss ki details left side m automatically fill hojayeg
  def get_cursor(self,event=""):
      cursor_focus=self.student_table.focus()
      content=self.student_table.item(cursor_focus)
      data=content.get("values", []) #storing values of data in data variable
      
      if data:  # Check if data is not empty
        self.var_Dep.set(data[0])
        self.var_Course.set(data[1])
        self.var_Year.set(data[2])
        self.var_Sem.set(data[3])
        self.var_Student_Id.set(data[4])
        self.var_Name.set(data[5])
        self.var_Divison.set(data[6])
        self.var_RollNO.set(data[7])
        self.var_Gender.set(data[8])
        self.var_Dob.set(data[9])
        self.var_Email.set(data[10])
        self.var_Phone.set(data[11])
        self.var_Address.set(data[12])
        self.var_Teacher.set(data[13])
        self.var_radio1.set(data[14])
      else:
        print("No data available for the selected item.")
        

   #update function
  def update_data(self): 
      if self.var_Dep.get()=="Select Department" or self.var_Name.get()=="" or self.var_Student_Id.get()=="":
        messagebox.showerror("Error","All Fields are required",parent=self.root) 
      else:
          try:
              Update=messagebox.askyesno("update","do you want to update this student details",parent=self.root)
              if Update>0:
                 conn=mysql.connector.connect(host="localhost",username="root",password="amittal123",database="face_recognizer")
                 my_cursor=conn.cursor()
                 my_cursor.execute("Update student set Dep=%s,Course=%s,Year=%s,semester=%s,Name=%s,Divison=%s,RollNO=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photo_Sample=%s where Student_Id=%s",(
                                                                                                          self.var_Dep.get(),
                                                                                                          self.var_Course.get(),
                                                                                                          self.var_Year.get(),
                                                                                                          self.var_Sem.get(),
                                                                                                          self.var_Name.get(),
                                                                                                          self.var_Divison.get(),
                                                                                                          self.var_RollNO.get(),
                                                                                                          self.var_Gender.get(),
                                                                                                          self.var_Dob.get(),
                                                                                                          self.var_Email.get(),
                                                                                                          self.var_Phone.get(),
                                                                                                          self.var_Address.get(),
                                                                                                          self.var_Teacher.get(),
                                                                                                          self.var_radio1.get(),
                                                                                                          self.var_Student_Id.get()


                                                                                                        ))
              else:
                 if not Update:
                     return
              messagebox.showinfo("Success","Student details succesfully update",parent=self.root)
              conn.commit()
              self.fetch_data()
              conn.close
                 
                 
          except  Exception as es:
             messagebox.showerror("Error",f"DUe To:{str(es)}",parent=self.root)

  #delete function
  def delete_data(self):
     if self.var_Student_Id.get()=="":
        messagebox.showerror("Error","student id must required",parent=self.root)
     else:
        try:
           delete=messagebox.askyesno("Student Delete PAge","Do you want to delete this studen",parent=self.root)
           if delete>0:
               conn=mysql.connector.connect(host="localhost",username="root",password="amittal123",database="face_recognizer")
               my_cursor=conn.cursor()
               sql="delete from student where Student_id=%s"
               val=(self.var_Student_Id.get(),)
               my_cursor.execute(sql,val)
           else:
              if not delete:
                  return    
           conn.commit()
           self.fetch_data()
           conn.close()
           messagebox.showinfo("delete","Successfully deleted",parent=self.root)
        except Exception as es:
           messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

   #reset function
  def reset_data(self):
     self.var_Dep.set("Select Department")
     self.var_Course.set("Select Course")
     self.var_Year.set("Select Year")
     self.var_Sem.set("Select Semester")
     self.var_Student_Id.set("")
     self.var_Name.set("")
     self.var_Divison.set("Select Division")
     self.var_RollNO.set("")
     self.var_Email.set("")
     self.var_Phone.set("")
     self.var_Address.set("")
     self.var_Teacher.set("")
     self.var_radio1.set("")
     self.var_Dob.set("")

   #generate data set or Take photo samples
  def generate_dataset(self):
     if self.var_Dep.get()=="Select Department" or self.var_Name.get()=="" or self.var_Student_Id.get()=="":
        messagebox.showerror("Error","All Fields are required",parent=self.root) 
     else:
         try:
             conn=mysql.connector.connect(host="localhost",username="root",password="amittal123",database="face_recognizer")
             my_cursor=conn.cursor()
             my_cursor.execute("Select * from Student")
             myresult=my_cursor.fetchall()
             id=0
             for x in myresult:
                 id+=1
             my_cursor.execute("Update student set Dep=%s,Course=%s,Year=%s,semester=%s,Name=%s,Divison=%s,RollNO=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photo_Sample=%s where Student_Id=%s",(
                                                                                                          self.var_Dep.get(),
                                                                                                          self.var_Course.get(),
                                                                                                          self.var_Year.get(),
                                                                                                          self.var_Sem.get(),
                                                                                                          self.var_Name.get(),
                                                                                                          self.var_Divison.get(),
                                                                                                          self.var_RollNO.get(),
                                                                                                          self.var_Gender.get(),
                                                                                                          self.var_Dob.get(),
                                                                                                          self.var_Email.get(),
                                                                                                          self.var_Phone.get(),
                                                                                                          self.var_Address.get(),
                                                                                                          self.var_Teacher.get(),
                                                                                                          self.var_radio1.get(),
                                                                                                          self.var_Student_Id.get()==id+1


                                                                                                        ))
             conn.commit()
             self.fetch_data()
             self.reset_data()
             conn.close()
             # we are use Haar Cascades alogrithm (interview se pehle haar cascades ko sahi padh lena ) 

              #load predifiend data on frontal from opencv
             face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #face_classifier my algorithm safe karli

             def face_cropped(img):# function h ye
                 gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #convert photo into gray
                 faces=face_classifier.detectMultiScale(gray,1.3,5) #gray photo faces m leli
                 #color=gray
                 #scaling factor =1.3
                 #minimum neighbor=5

                 for(x,y,w,h) in faces:
                    face_cropped=img[y:y+h,x:x+w] #photo ko crop karlia 
                    return face_cropped
                 
             cap =cv2.VideoCapture(0)
             img_id=0
             while True: #loop run kiya 100 photo ke liye
                ret,my_frame=cap.read()
                if face_cropped(my_frame) is not None:
                   img_id+=1
                   face=cv2.resize(face_cropped(my_frame),(450,450))
                   face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                   file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                   cv2.imwrite(file_name_path,face)
                   cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                   cv2.imshow("Crooped face",face)

                if cv2.waitKey(1)==13 or int(img_id)==100:
                   break
             cap.release()
             cv2.destroyAllWindows()
             messagebox.showinfo("Result","Generating data sets completed")
         except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

            

if __name__ == "__main__":   #main started from here 
      root = Tk()    #tk to root
      obj = Student(root)  #making object of class by passing root 
      root.mainloop()  #main ends here  