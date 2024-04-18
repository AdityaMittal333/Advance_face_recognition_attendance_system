from tkinter import*    
from tkinter import ttk   
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendence:  
  def __init__(self, root):  
    self.root = root
    self.root.geometry("1530x790+0+0")
    self.root.title("Face_Recognition_System")

    
    self.var_Employee_Id=StringVar()
    self.var_Name=StringVar()
    self.var_Department=StringVar()
    self.var_Roll=StringVar()
    self.var_Time=StringVar()
    self.var_Date=StringVar()
    self.var_Attendence=StringVar()

  

     #image 1
    img=Image.open("S1.jpg")
    img = img.resize((750, 200)) 
    self.photoimg=ImageTk.PhotoImage(img) 

    f_lbl=Label(self.root,image=self.photoimg) 
    f_lbl.place(x=0,y=0,width=750,height=200) 

    #image 2
    img=Image.open("S2.jpg")
    img1 = img.resize((800, 200))   
    self.photoimg1=ImageTk.PhotoImage(img1)  

    f_lbl=Label(self.root,image=self.photoimg1) 
    f_lbl.place(x=750,y=0,width=800,height=200)

     #background image
    img= Image.open("Web%20Application%20Firewall%20vs.webp")
    img3 = img.resize((1530, 790))  
    self.photoimg3=ImageTk.PhotoImage(img3)  
    bg_img=Label(self.root,image=self.photoimg3)
    bg_img.place(x=0,y=200,width=1530,height=710)  
    
    title_lbl=Label(bg_img,text="Student Attendence System",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
    title_lbl.place(x=0,y=0,width=1530,height=45)

    main_frame=Frame(bg_img,bd=2,bg="white")  
    main_frame.place(x=10,y=55,width=1415,height=600) 

    #left frame
    Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendece Details",font=("times new roman",12,"bold"),fg="black")
    Left_frame.place(x=10,y=10,width=690,height=550)

    img_left=Image.open("S4.webp")
    img_left = img_left.resize((680, 130))   
    self.photo_left=ImageTk.PhotoImage(img_left)

    f_lbl=Label(Left_frame,image=self.photo_left) 
    f_lbl.place(x=5,y=0,width=680,height=150) 

    #Class Student Information
    class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"),fg="black")
    class_student_frame.place(x=5,y=160,width=680,height=360)
     
     #Employee_Id
    Employee_Id_label=Label(class_student_frame,text="EmployeeId",font=("times new roman",12,"bold"),bg="white",fg="black") 
    Employee_Id_label.grid(row=0,column=0,padx=10,sticky=W)
 
    Employee_Id_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_Employee_Id,font=("times new roman ",13,"bold"))
    Employee_Id_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

    #Roll
    Roll_label=Label(class_student_frame,text="Roll:",font=("times new roman",12,"bold"),bg="white",fg="black") 
    Roll_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
 
    Roll_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_Name,font=("times new roman ",13,"bold"))
    Roll_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

    #Name
    Name_label=Label(class_student_frame,text="Name:",font=("times new roman",12,"bold"),bg="white",fg="black") 
    Name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
 
    Name_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_Name,font=("times new roman ",13,"bold"))
    Name_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)

    #Department
    Department_label=Label(class_student_frame,text="Department:",font=("times new roman",12,"bold"),bg="white",fg="black") 
    Department_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
 
    Department_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_Department,font=("times new roman ",13,"bold"))
    Department_entry.grid(row=1,column=3,padx=10,pady=10,sticky=W)

    #Time
    Time_label=Label(class_student_frame,text="Time:",font=("times new roman",12,"bold"),bg="white",fg="black") 
    Time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
 
    Time_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_Time,font=("times new roman ",13,"bold"))
    Time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

    #Date
    Date_label=Label(class_student_frame,text="Date:",font=("times new roman",12,"bold"),bg="white",fg="black") 
    Date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
 
    Date_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_Date,font=("times new roman ",13,"bold"))
    Date_entry.grid(row=2,column=3,padx=10,pady=10,sticky=W)

    #Attendence
    Attendence_label=Label(class_student_frame,text="Attendence Status:",font=("times new roman",12,"bold"),bg="white",fg="black") 
    Attendence_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
 
    Attendence_combo=ttk.Combobox(class_student_frame,textvariable=self.var_Attendence,font=("times new roman",12,"bold"),state="readyonly",width=18)
    Attendence_combo["values"]=("Present","Absent")
    Attendence_combo.current(0)  
    Attendence_combo.grid(row=3,column=1,padx=10,pady=10,sticky=W)

     #button frame
    btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
    btn_frame.place(x=0,y=190,width=675,height=40)
    
    import_btn=Button(btn_frame,text="Import CSV",command=self.importCsv,font=("times,new roman",13,"bold"),bg="white",fg="black",width=14,padx=5,pady=5)
    import_btn.grid(row=0,column=0)

    Export_btn=Button(btn_frame,text="Export CSV",command=self.exportCsv,font=("times,new roman",13,"bold"),bg="white",fg="black",width=14,padx=5,pady=5)
    Export_btn.grid(row=0,column=1)

    Update_btn=Button(btn_frame,text="Update",font=("times,new roman",13,"bold"),bg="white",fg="black",width=14,padx=5,pady=5)
    Update_btn.grid(row=0,column=2)

    reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=13,font=("times,new roman",13,"bold"),bg="darkblue",fg="black",padx=5,pady=5)
    reset_btn.grid(row=0,column=3)

    #Right label frame
    Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendence Details",font=("times new roman",12,"bold"),fg="black")
    Right_frame.place(x=710,y=10,width=690,height=550)

    #table frame
   
    table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
    table_frame.place(x=10, y=15, width=670, height=500)
 
    scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL) 
    scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

    self.AttendenceReportTable = ttk.Treeview(table_frame, column=("Attendence Id", "Roll", "Name", "Department", "Time", "Date", "Attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set) 

    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)
    
    scroll_x.config(command=self.AttendenceReportTable.xview)
    scroll_y.config(command=self.AttendenceReportTable.yview)

    self.AttendenceReportTable.heading("Attendence Id", text="Attendence Id")
    self.AttendenceReportTable.heading("Roll", text="Roll")
    self.AttendenceReportTable.heading("Name", text="Name")
    self.AttendenceReportTable.heading("Department", text="Department")
    self.AttendenceReportTable.heading("Time", text="Time")
    self.AttendenceReportTable.heading("Date", text="Date")
    self.AttendenceReportTable.heading("Attendance", text="Attendance")


    self.AttendenceReportTable["show"] = "headings" 
    self.AttendenceReportTable.pack(fill=BOTH, expand=1)
    self.AttendenceReportTable.bind("<ButtonRelease>",self.get_cursor)


   #fetch data
  def fetchData(self,rows):
     self.AttendenceReportTable.delete(*self.AttendenceReportTable.get_children())
     for i in rows:
        self.AttendenceReportTable.insert("",END,values=i)
  #import csv
  def importCsv(self):
     global mydata
     mydata.clear()
     fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="open csv",filetypes=(("CVS File","*.csv"),("ALl File","*.*")),parent=self.root)
     with open(fln) as myfile:
        cvsread=csv.reader(myfile,delimiter=",")
        for i in cvsread: 
           mydata.append(i)
        self.fetchData(mydata)

 
#exponent csv
  def exportCsv(self):
     try:
        if len(mydata)<1:
           messagebox.showerror("No Data","No data found to export",parent=self.root)
           return False
        fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="open csv",filetypes=(("CVS File","*.csv"),("ALl File","*.*")),parent=self.root)
        with open(fln,mode="w",newline="") as myfile:
           exp_write=csv.writer(myfile,delimiter=",")
           for i in mydata:
              exp_write.writerow(i)
              messagebox.showinfo("Data Export","data exported to"+os.path.basename(fln)+"successfully")

     except Exception as es:
        messagebox.showerror("error",f"Due To :{str(es)}",parent=self.root)

  def get_cursor(self,event=""):
     cursor_row=self.AttendenceReportTable.focus()
     content=self.AttendenceReportTable.item(cursor_row)
     rows=content['values']
     if rows:
        if len(rows) >= 7:  
            self.var_Employee_Id.set(rows[0])
            self.var_Name.set(rows[1])
            self.var_Department.set(rows[2])
            self.var_Roll.set(rows[3])
            self.var_Time.set(rows[4])
            self.var_Date.set(rows[5])
            self.var_Attendence.set(rows[6])
        else:
            messagebox.showwarning("Warning", "Selected row doesn't contain enough data.")
     else:
        messagebox.showwarning("Warning", "No row selected.")

  def reset_data(self):
     self.var_Employee_Id.set("")
     self.var_Name.set("")
     self.var_Department.set("")
     self.var_Roll.set("")
     self.var_Time.set("")
     self.var_Date.set("")
     self.var_Attendence.set("")
   

  
     
 


if __name__ == "__main__":   
      root = Tk()    
      obj = Attendence(root)  
      root.mainloop() 
