from tkinter import*
from tkinter import ttk
from train import Train
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import os
from helpsupport import Helpsupport

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face_Recognition_System")

# This part is image labels setting start 
        # first header image  
        img=Image.open(r"/home/pi/Desktop/Golden Eye/Pics_GUI/Main/banner.jpg")
        img=img.resize((1366,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        # backgorund image 
        bg1=Image.open(r"/home/pi/Desktop/Golden Eye/Pics_GUI/Main/bg3.jpg")
        bg1=bg1.resize((1366,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Golden Eye Facial Recognition System",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        img2 = Image.open(r"/home/pi/Desktop/Golden Eye/Pics_GUI/Login/profile.jpg")
        img2 = img2.resize((220, 220), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
		
        b1 = Button(bg_img, image = self.photoimg2, command = self.student_details, cursor = "hand2")
        b1.place(x = 200, y = 100, width = 220, height = 220)
		
		
        b1_1 = Button(bg_img, text = "Student Details", command = self.student_details, cursor = "hand2", font = ("times new roman", 15, "bold"),bg = "darkblue", fg = "white")
        b1_1.place(x = 200, y = 300, width = 220, height = 40)
		
		
        # ============================================ Detect face button ===============================================
		
        img3 = Image.open(r"/home/pi/Desktop/Golden Eye/Pics_GUI/Login/det1.jpg")
        img3 = img3.resize((220, 220), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
		
        b1 = Button(bg_img, image = self.photoimg3, command = self.detect_data, cursor = "hand2")
        b1.place(x = 500, y = 100, width = 220, height = 220)
		
		
        b1_1 = Button(bg_img, text = "Face Detector", command = self.detect_data, cursor = "hand2", font = ("times new roman", 15, "bold"),bg = "darkblue", fg = "white")
        b1_1.place(x = 500, y = 300, width = 220, height = 40)
		
		
        # ================================================= Attendance face button =========================================
	
        img4 = Image.open(r"/home/pi/Desktop/Golden Eye/Pics_GUI/Login/Attendance.jpg")
        img4 = img4.resize((220, 220), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
		
        b1 = Button(bg_img, image = self.photoimg4, command = self.attendance_sheet_details, cursor = "hand2")
        b1.place(x = 800, y = 100, width = 220, height = 220)
		
		
        b1_1 = Button(bg_img, text = "Attendance", command = self.attendance_sheet_details, cursor = "hand2", font = ("times new roman", 15, "bold"),bg = "darkblue", fg = "white")
        b1_1.place(x = 800, y = 300, width = 220, height = 40)
		
		
        # ================================ Chatbot button ==============================================================
		
        img5 = Image.open(r"/home/pi/Desktop/Golden Eye/Pics_GUI/Main/chatbot.jpg")
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
		
        b1 = Button(bg_img, image = self.photoimg5, command = self.chatbot_program, cursor = "hand2")
        b1.place(x = 1100, y = 100, width = 220, height = 220)
		
		
        b1_1 = Button(bg_img, text = "Chatbot Help Desk", command = self.chatbot_program, cursor = "hand2", font = ("times new roman", 15, "bold"),bg = "darkblue", fg = "white")
        b1_1.place(x = 1100, y = 300, width = 220, height = 40)
		
				
		
        # ====================================== Generate Warning List Details button ======================================================
		
        img10 = Image.open(r"/home/pi/Desktop/Golden Eye/Pics_GUI/Main/warning.jpg")
        img10 = img10.resize((220, 220), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)
		
        b1 = Button(bg_img, image = self.photoimg10, cursor = "hand2")
        b1.place(x =200, y = 380, width = 220, height = 220)
		
		
        b1_1 = Button(bg_img, text = "Warning List Details", cursor = "hand2", font = ("times new roman", 15, "bold"),bg = "darkblue", fg = "white")
        b1_1.place(x = 200, y = 580, width = 220, height = 40)
		
		
		# ============================================= Exit face button ===================================================
		
        img11 = Image.open(r"/home/pi/Desktop/Golden Eye/Pics_GUI/Login/exit.jpg")
        img11 = img11.resize((220, 220), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)
		
        b1 = Button(bg_img, image = self.photoimg11, command = self.terminate_application, cursor = "hand2")
        b1.place(x = 500, y = 380, width = 220, height = 220)
		
		
        b1_1 = Button(bg_img, text = "Exit", command = self.terminate_application, cursor = "hand2", font = ("times new roman", 15, "bold"),bg = "darkblue", fg = "white")
        b1_1.place(x = 500, y = 580, width = 220, height = 40)
		
		
		# =============================================================== Functions Buttons ===========================================
	

# ==================Functions Buttons=====================
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def detect_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_sheet_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def chatbot_program(self):
        self.new_window = Toplevel(self.root)
        self.app = Chatbot(self.new_window)

    def terminate_application(self):
        self.root.destroy()
       
	    

					
if __name__ == "__main__":
     root = Tk()
     obj = Face_Recognition_System(root)
     root.mainloop()
