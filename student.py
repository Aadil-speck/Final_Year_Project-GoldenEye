from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
	
	def __init__(self, root):
		self.root = root
		self.root.geometry("1530x790+0+0")
		self.root.title("Golden-Eye Face Recognition System")
		
		# variables
		self.var_dep = StringVar()
		self.var_course = StringVar()
		self.var_year = StringVar()
		self.var_semester = StringVar()
		self.var_std_id = StringVar()
		self.var_std_name = StringVar()
		self.var_gender = StringVar()
		self.var_email = StringVar()
		self.var_dob = StringVar()
		self.var_lecturer = StringVar()	
		
		# bg image
		

		title_lbl = Label(text = "STUDENT MANAGEMENT SYSTEM", font = ("times new roman", 35, "bold"),bg = "white", fg = "darkgreen")
		title_lbl.place(x = 0, y = 0, width = 1530, height = 45)
		
		main_frame = Frame( bd = 2, bg = "white")
		main_frame.place(x = 20, y = 50, width = 1480, height = 600)
		
		# Left label frame
		Left_frame = LabelFrame(main_frame, bd = 2, bg = "white", relief = RIDGE, text = "Student Details", font = ("times new roman", 12, "bold"))
		Left_frame.place(x = 10, y = 10, width = 730, height = 580)
		
	
		
		
		# Current course information
		current_course_frame = LabelFrame(Left_frame, bd = 2, bg = "white", relief = RIDGE, text = "Current Course Information", font = ("times new roman", 12, "bold"))
		current_course_frame.place(x = 5, y = 135, width = 720, height = 115)
		
		
		# Department
		dep_label = Label(current_course_frame, text = "Department", font = ("times new roman", 13, "bold"), bg = "white")
		dep_label.grid(row = 0, column = 0, padx = 10, sticky = W)
		
		 # textvariable = self.var_dep,
		dep_combo = ttk.Combobox(current_course_frame, textvariable = self.var_dep, font = ("times new roman", 13, "bold"), state = "readonly", width = 20)
		dep_combo["values"] = ("Select Department:","Computer and Information Technology", "Chemistry", "Life Sciences", "Mathematics and Statistics", "Physics")
		dep_combo.current(0)
		dep_combo.grid(row = 0, column = 1, padx = 2, pady = 10, sticky = W)
		
		
		# Course Code
		course_label = Label(current_course_frame, text = "Course Code", font = ("times new roman", 13, "bold"), bg = "white")
		course_label.grid(row = 0, column = 2, padx = 10, sticky = W)
		
		# textvariable = self.var_course,
		course_combo = ttk.Combobox(current_course_frame, textvariable = self.var_course, font = ("times new roman", 13, "bold"), state = "readonly", width = 20)
		course_combo["values"] = ("Select Courses:","CHEM 1062", "CHEM 1066", "CHEM 1070", "CHEM 2170", "CHEM 2270", "COMP 1600", "COMP 1601", "COMP 1602", "COMP 1603", "COMP 1604", "INFO 1600", "INFO 1601", "INFO 1602", "INFO 1604", "MATH 1142", "MATH 1152", "MATH 1194", "MATH 1141", "MATH 1151", "PHYS 1001", "PHYS 1221", "PHYS 1222", "PHYS 2150", "PHYS 2152")
		course_combo.current(0)
		course_combo.grid(row = 0, column = 3, padx = 2, pady = 10, sticky = W)
		
		
		# Year
		year_label = Label(current_course_frame, text = "Year", font = ("times new roman", 13, "bold"), bg = "white")
		year_label.grid(row = 1, column = 0, padx = 10, sticky = W)
		
		# textvariable = self.var_year,
		year_combo = ttk.Combobox(current_course_frame, textvariable = self.var_year, font = ("times new roman", 13, "bold"), state = "readonly", width = 20)
		year_combo["values"] = ("Select Year:","2022-2023", "2023-2024", "2024-2025")
		year_combo.current(0)
		year_combo.grid(row = 1, column = 1, padx = 2, pady = 10, sticky = W)
		
		
		# Semester
		semester_label = Label(current_course_frame, text = "Semester", font = ("times new roman", 13, "bold"), bg = "white")
		semester_label.grid(row = 1, column = 2, padx = 10, sticky = W)
		
		#  textvariable = self.var_semester,
		semester_combo = ttk.Combobox(current_course_frame, textvariable = self.var_semester, font = ("times new roman", 13, "bold"), state = "readonly", width = 20)
		semester_combo["values"] = ("Select Semester:","Semester-1", "Semester-2", "Semester-3 (Summer)")
		semester_combo.current(0)
		semester_combo.grid(row = 1, column = 3, padx = 2, pady = 10, sticky = W)
		
		
		# Class student information
		class_Student_frame = LabelFrame(Left_frame, bd = 2, bg = "white", relief = RIDGE, text = "Class Student Information", font = ("times new roman", 12, "bold"))
		class_Student_frame.place(x = 5, y = 250, width = 720, height = 300)
		
		
		# Student ID
		studentId_label = Label(class_Student_frame, text = "Student ID:", font = ("times new roman", 13, "bold"), bg = "white")
		studentId_label.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = W)
		
		# textvariable = self.var_std_id,
		studentID_entry = ttk.Entry(class_Student_frame, textvariable = self.var_std_id, width = 20, font = ("times new roman", 13, "bold"))
		studentID_entry.grid(row = 0, column = 1, padx = 2, pady = 10, sticky = W)
		
		
		# Student Name
		studentName_label = Label(class_Student_frame, text = "Student Name:", font = ("times new roman", 13, "bold"), bg = "white")
		studentName_label.grid(row = 1, column = 0, padx = 10, pady = 5, sticky = W)
		
		# self.var_std_name,
		studentName_entry = ttk.Entry(class_Student_frame, textvariable = self.var_std_name, width = 20, font = ("times new roman", 13, "bold"))
		studentName_entry.grid(row = 1, column = 1, padx = 2, pady = 10, sticky = W)
		
		
		# Student Gender
		gender_label = Label(class_Student_frame, text = "Student Gender:", font = ("times new roman", 13, "bold"), bg = "white")
		gender_label.grid(row = 2, column = 0, padx = 10, pady = 5, sticky = W)
		
		# textvariable = self.var_gender,
		gender_combo = ttk.Combobox(class_Student_frame, textvariable = self.var_gender, font = ("times new roman", 13, "bold"), state = "readonly", width = 20)
		gender_combo["values"] = ("Select Gender:","Male", "Female")
		gender_combo.current(0)
		gender_combo.grid(row = 2, column = 1, padx = 2, pady = 10, sticky = W)
		
		# Student date of birth
		dob_label = Label(class_Student_frame, text = "Student Date of Birth:", font = ("times new roman", 13, "bold"), bg = "white")
		dob_label.grid(row = 0, column = 2, padx = 10, pady = 5, sticky = W)
		
		# textvariable = self.var_dob,
		dob_entry = ttk.Entry(class_Student_frame, textvariable = self.var_dob, width = 20, font = ("times new roman", 13, "bold"))
		dob_entry.grid(row = 0, column = 3, padx = 2, pady = 10, sticky = W)
		
		
		# Student email
		email_label = Label(class_Student_frame, text = "Student Email:", font = ("times new roman", 13, "bold"), bg = "white")
		email_label.grid(row = 3, column = 0, padx = 10, pady = 5, sticky = W)
		
		# textvariable = self.var_email,
		email_entry = ttk.Entry(class_Student_frame, textvariable = self.var_email, width = 20, font = ("times new roman", 13, "bold"))
		email_entry.grid(row = 3, column = 1, padx = 2, pady = 10, sticky = W)
		
		
		# Lecturer name
		lecturer_label = Label(class_Student_frame, text = "Lecturer Name:", font = ("times new roman", 13, "bold"), bg = "white")
		lecturer_label.grid(row = 1, column = 2, padx = 10, pady = 5, sticky = W)
		
		# textvariable = self.var_lecturer,
		lecturer_entry = ttk.Entry(class_Student_frame, textvariable = self.var_lecturer, width = 20, font = ("times new roman", 13, "bold"))
		lecturer_entry.grid(row = 1, column = 3, padx = 2, pady = 10, sticky = W)
		
		
		# Buttons Frame
		btn_frame = Frame(class_Student_frame, bd = 2, relief = RIDGE, bg = "white")
		btn_frame.place(x = 0, y = 200, width = 715, height = 70)
		
		save_btn = Button(btn_frame, text = "Save", command = self.add_data, width = 17, font = ("times new roman", 13, "bold"), bg = "blue", fg = "white")
		save_btn.grid(row = 0, column = 0)
		
		update_btn = Button(btn_frame, text = "Update", command = self.update_data, width = 17, font = ("times new roman", 13, "bold"), bg = "blue", fg = "white")
		update_btn.grid(row = 0, column = 1)
		
		delete_btn = Button(btn_frame, text = "Delete", command = self.delete_data, width = 17, font = ("times new roman", 13, "bold"), bg = "blue", fg = "white")
		delete_btn.grid(row = 0, column = 2)
		
		reset_btn = Button(btn_frame, text = "Reset", command = self.reset_data, width = 17, font = ("times new roman", 13, "bold"), bg = "blue", fg = "white")
		reset_btn.grid(row = 0, column = 3)
		
		btn_frame1 = Frame(class_Student_frame, bd = 2, relief = RIDGE, bg = "white")
		btn_frame1.place(x = 0, y = 235, width = 715, height = 35)
		
		take_photo_btn = Button(btn_frame1, command = self.generate_dataset, text = "Take Photo Sample", width = 35, font = ("times new roman", 13, "bold"), bg = "blue", fg = "white")
		take_photo_btn.grid(row = 0, column = 0)
		
		update_photo_btn = Button(btn_frame1, text = "Update Photo Sample", width = 35, font = ("times new roman", 13, "bold"), bg = "blue", fg = "white")
		update_photo_btn.grid(row = 0, column = 1)
		
		
		
		# Right label frame
		Right_frame = LabelFrame(main_frame, bd = 2, bg = "white", relief = RIDGE, text = "Student Search Details", font = ("times new roman", 12, "bold"))
		Right_frame.place(x = 750, y = 10, width = 720, height = 580)
		
		
		
		# Search Sytem
		Search_frame = LabelFrame(Right_frame, bd = 2, bg = "white", relief = RIDGE, text = "Search System", font = ("times new roman", 12, "bold"))
		Search_frame.place(x = 5, y = 135, width = 710, height = 70)
		
		search_label = Label(Search_frame, text = "Search By:", font = ("times new roman", 15, "bold"), bg = "blue", fg = "white")
		search_label.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = W)
		
		search_combo = ttk.Combobox(Search_frame, font = ("times new roman", 13, "bold"), state = "readonly", width = 15)
		search_combo["values"] = ("Select", "Student Id", "Student Name", "Student Email")
		search_combo.current(0)
		search_combo.grid(row = 0, column = 1, padx = 2, pady = 10, sticky = W)
		
		search_entry = ttk.Entry(Search_frame, width = 15, font = ("times new roman", 13, "bold"))
		search_entry.grid(row = 0, column = 2, padx = 10, pady = 5, sticky = W)
		
		
		search_btn = Button(Search_frame, text = "Search", width = 12, font = ("times new roman", 12, "bold"), bg = "blue", fg = "white")
		search_btn.grid(row = 0, column = 3, padx = 4)
		
		showAll_btn = Button(Search_frame, text = "Show All", width = 12, font = ("times new roman", 12, "bold"), bg = "blue", fg = "white")
		showAll_btn.grid(row = 0, column = 4, padx = 4)
		
		
		# Table Frame
		table_frame = Frame(Right_frame, bd = 2, bg = "white", relief = RIDGE)
		table_frame.place(x = 5, y = 210, width = 710, height = 350)
		
		scroll_x = ttk.Scrollbar(table_frame, orient = HORIZONTAL)
		scroll_y = ttk.Scrollbar(table_frame, orient = VERTICAL)
		
		self.student_table = ttk.Treeview(table_frame, column = ("dep", "course", "year", "sem", "id", "name", "gender", "email", "dob", "lecturer"), xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)
		
		scroll_x.pack(side = BOTTOM, fill = X)
		scroll_y.pack(side = RIGHT, fill = Y)
		scroll_x.config(command = self.student_table.xview)
		scroll_y.config(command = self.student_table.yview)
		
		
		self.student_table.heading("dep", text = "Department")
		self.student_table.heading("course", text = "Course Code")
		self.student_table.heading("year", text = "Year")
		self.student_table.heading("sem", text = "Semester")
		self.student_table.heading("id", text = "Student Id")
		self.student_table.heading("name", text = "Name")
		self.student_table.heading("gender", text = "Gender")
		self.student_table.heading("email", text = "Email")
		self.student_table.heading("dob", text = "Date Of Birth")
		self.student_table.heading("lecturer", text = "Lecturer")
		self.student_table["show"] = "headings"
		
		self.student_table.column("dep", width = 300)
		self.student_table.column("course", width = 100)
		self.student_table.column("year", width = 100)
		self.student_table.column("sem", width = 100)
		self.student_table.column("id", width = 150)
		self.student_table.column("name", width = 250)
		self.student_table.column("gender", width = 100)
		self.student_table.column("email", width = 250)
		self.student_table.column("dob", width = 150)
		self.student_table.column("lecturer", width = 250)
		
		
		self.student_table.pack(fill = BOTH, expand = 1)
		self.student_table.bind("<ButtonRelease>", self.get_cursor)
		self.fetch_data()
		
		# Function declaration
	def add_data(self):
		if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
			messagebox.showerror("Error", "All Fields are required", parent = self.root)
		else:
			try:
				conn = mysql.connector.connect(host="localhost", username="Aadil", password="prime2", database="Golden_EyeDB")
				my_cursor = conn.cursor()
				my_cursor.execute("insert into student values(%s, %s, %s, %s, %s,  %s,  %s,  %s,  %s,  %s)",(
																													self.var_dep.get(),
																													self.var_course.get(),
																													self.var_year.get(),
																													self.var_semester.get(),
																													self.var_std_id.get(),
																													self.var_std_name.get(),
																													self.var_gender.get(),
																													self.var_email.get(),
																													self.var_dob.get(),
																													self.var_lecturer.get()
																												))
				conn.commit()
				self.fetch_data()
				conn.close()
				messagebox.showinfo("Success", "Student details has been added Successfully!", parent = self.root)
			except Exception as es:
				messagebox.showerror("Error", f"Due To:{str(es)}", parent = self.root)
				
				
	# ===============================================fetch data===================================================================================================
		
	def fetch_data(self):
		conn = mysql.connector.connect(host = "localhost", username = "Aadil", password = "prime2", database = "Golden_EyeDB")
		my_cursor = conn.cursor()
		my_cursor.execute("SELECT * FROM student")
		data = my_cursor.fetchall()
		
		if len(data) != 0:
			self.student_table.delete(*self.student_table.get_children())
			for i in data:
				self.student_table.insert("", END, value = i)
			conn.commit()
		conn.close()
				
	#=================================================Get Cursor===========================================================================================================
	
	def get_cursor(self, event = ""):
		cursor_focus = self.student_table.focus()
		content = self.student_table.item(cursor_focus)
		data = content["values"]
		
		self.var_dep.set(data[0]),
		self.var_course.set(data[1]),
		self.var_year.set(data[2]),
		self.var_semester.set(data[3]),
		self.var_std_id.set(data[4]),
		self.var_std_name.set(data[5]),
		self.var_gender.set(data[6]),
		self.var_email.set(data[7]),
		self.var_dob.set(data[8]),
		self.var_lecturer.set(data[9])
		
	#================================================Update Function=======================================================================
	
	def update_data(self):
		if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
			messagebox.showerror("Error", "All Fields are required", parent = self.root)
		else:
			try:
				Update= messagebox.askyesno("Update", "Do you want to update this stuudent details", parent = self.root)
				if Update > 0:
					conn = mysql.connector.connect(host="localhost", username="Aadil", password="prime2", database="Golden_EyeDB")
					my_cursor = conn.cursor()
					my_cursor.execute("update student set Dep = %s, course = %s, Year = %s, Semester = %s, Name = %s, Gender = %s, Email = %s, Dob = %s, Lecturer = %s WHERE Student_id = %s", (
					
																																									self.var_dep.get(),
																																									self.var_course.get(),
																																									self.var_year.get(),
																																									self.var_semester.get(),
																																									self.var_std_name.get(),
																																									self.var_gender.get(),
																																									self.var_email.get(),
																																									self.var_dob.get(),
																																									self.var_lecturer.get(),
																																									self.var_std_id.get()
					
																																								))
				else:
					if not Update:
						return
				messagebox.showinfo("Success", "Student details successfully update completed", parent = self.root)
				conn.commit()
				self.fetch_data()
				conn.close()
			except Exception as es:
				messagebox.showerror("Error", f"Due To:{str(es)}", parent = self.root)		
				
				
	
	#===========================================================Delete Function===================================================================
	
	def delete_data(self):
		if self.var_std_id.get()=="":
			messagebox.showerror("Error", "Student ID must be required", parent = self.root)
		else:
			try:
				Delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this student?", parent = self.root)
				if Delete >0:
					conn = mysql.connector.connect(host="localhost", username="Aadil", password="prime2", database="Golden_EyeDB")
					my_cursor = conn.cursor()
					sql = "DELETE FROM student WHERE Student_id = %s"
					val = (self.var_std_id.get(),)
					my_cursor.execute(sql,val)
				else:
					if not Delete:
						return
				conn.commit()
				self.fetch_data()
				conn.close()
				messagebox.showinfo("Delete", "Successfully deleted student details", parent = self.root)
			except Exception as es:
				messagebox.showerror("Error", f"Due To:{str(es)}", parent = self.root)	
				
	#=========================================================== Reset==================================================================================
	
	def reset_data(self):
		self.var_dep.set("Select Department:"),
		self.var_course.set("Select Courses:"),
		self.var_year.set("Select Year:"),
		self.var_semester.set("Select Semester:"),
		self.var_std_id.set(""),
		self.var_std_name.set(""),
		self.var_gender.set("Select Gender:"),
		self.var_email.set(""),
		self.var_dob.set(""),
		self.var_lecturer.set("")
		
	#========================================================Generate data set or Take photo samples=================================================================================
	
	def generate_dataset(self):
		if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
			messagebox.showerror("Error", "All Fields are required", parent = self.root)
		else:
			try:
				conn = mysql.connector.connect(host="localhost", username="Aadil", password="prime2", database="Golden_EyeDB")
				my_cursor = conn.cursor()
				my_cursor.execute("SELECT * FROM student")
				myresult = my_cursor.fetchall()
				id = 0
				for x in myresult:
					id += 1
				my_cursor.execute("update student set Dep = %s, course = %s, Year = %s, Semester = %s, Name = %s, Gender = %s, Email = %s, Dob = %s, Lecturer = %s WHERE Student_id = %s", (
					
																																									self.var_dep.get(),
																																									self.var_course.get(),
																																									self.var_year.get(),
																																									self.var_semester.get(),
																																									self.var_std_name.get(),
																																									self.var_gender.get(),
																																									self.var_email.get(),
																																									self.var_dob.get(),
																																									self.var_lecturer.get(),
																																									self.var_std_id.get()
																																								))
				conn.commit()
				self.fetch_data()
				self.reset_data()
				conn.close()
				 
															
				#==============================Load predifiend data on face frontals from opencv==============================
				
				face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
				
				def face_cropped(img):
					gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
					faces = face_classifier.detectMultiScale(gray, 1.3, 5)
					#scaling factor = 1.3
					#Minimum Neighbor = 5 
					
					for (x, y, w, h) in faces:
						face_cropped = img[y: y+h, x: x+w]
						return face_cropped
						
				cap = cv2.VideoCapture(0)
				img_id = 0
				while True:
					ret, my_frame = cap.read()
					if face_cropped(my_frame) is not None:
						img_id += 1
						face = cv2.resize(face_cropped(my_frame), (450, 450))
						face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
						file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
						cv2.imwrite(file_name_path, face)
						cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0,255, 0), 2)
						cv2.imshow("Cropped Face", face)
					
					if cv2.waitKey(1) == 13 or int(img_id) == 100:
						break
				cap.release()
				cv2.destroyAllWindows()
				messagebox.showinfo("Result", "Generating data sets compled!")
			except Exception as es:
				messagebox.showerror("Error", f"Due To:{str(es)}", parent = self.root) 
				
				
					
				
				
				
if __name__ == "__main__":
	root = Tk()
	obj = Student(root)
	root.mainloop()
