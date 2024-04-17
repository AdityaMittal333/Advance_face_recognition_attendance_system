from tkinter import*    #library for gui development
from tkinter import ttk  #have stylish 
# importing pillow library using this command = pip install pillow
from PIL import Image,ImageTk # using to crop or edit image 


class Face_Recognition_System: #class name Face_Recognition_System
  def _init__(self,root): #constructor 
    self.root=root
    self.root.geometry("1400x790+0+0")
    self.root.title("Face_Recognition_System")














    if __name__ == "__main__":
      root=tk()
      obj=Face_Recognition_System(root)
      root.mainloop()