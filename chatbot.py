from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk



class Chatbot:
	
	def __init__(self, root):
		self.root = root
		self.root.geometry("730x620+0+0")
		self.root.title("Help Desk Chatbot System")
		self.root.bind("<Return>", self.enter_functionality)
		
		main_frame = Frame(self.root, bd = 4, bg = "lightblue", width = 610)
		main_frame.pack()
		
		img_bot = Image.open(r"/home/pi/Desktop/Project_Golden_Eye/FINAL PROJECT INTERFACE IMAGES/chatbot.jpg")
		img_bot = img_bot.resize((200, 70), Image.ANTIALIAS)
		self.photoimg = ImageTk.PhotoImage(img_bot)
		
		Title_label = Label(main_frame, bd = 3, relief = RAISED, anchor = 'nw', width = 730, compound = LEFT, image = self.photoimg, text = "How May I Help You", font = ("ariel", 30, "bold"), fg = "green", bg = "white")
		Title_label.pack(side = TOP)
		
		self.scroll_y = ttk.Scrollbar(main_frame, orient = VERTICAL)
		self.text = Text(main_frame, width = 65, height = 20, bd = 3, relief = RAISED, font = ("arial", 14), yscrollcommand = self.scroll_y.set)
		self.scroll_y.pack(side = RIGHT, fill = Y)
		self.text.pack()
		
		
		btn_frame = Frame(self.root, bg = "white", width = 730)
		btn_frame.pack()
		
		
		lbl = Label(btn_frame, text = "What is your question ?", font = ("ariel", 14, "bold"), fg = "green", bg = "white")
		lbl.grid(row = 0, column = 0, padx = 5, sticky = W)
		
		self.entry1_var = StringVar()
		self.entry = ttk.Entry(btn_frame, textvariable = self.entry1_var, width = 40, font = ("times new roman", 16, "bold"))
		self.entry.grid(row = 0, column = 1, padx = 5, sticky = W)
		
		self.send = Button(btn_frame, text = "Send >>", command = self.send, font = ("arial", 15, "bold"), width = 8, bg = "green")
		self.send.grid(row = 0, column = 2, padx = 5, sticky = W)
		
		self.clear = Button(btn_frame, text = "Reset", command = self.clear_data, font = ("arial", 15, "bold"), width = 8, bg = "red", fg = "white")
		self.clear.grid(row = 1, column = 0, padx = 5, sticky = W)
		
		self.msg = " "
		self.lbl_1 = Label(btn_frame, text = self.msg, font = ("ariel", 14, "bold"), fg = "red", bg = "white")
		self.lbl_1.grid(row = 1, column = 1, padx = 5, sticky = W)
		
		
		
		
		
		# Function Declaration
	def enter_functionality(self, event):
		self.send.invoke()
		self.entry.set("")
	
	def clear_data(self):
		self.text.delete("1.0", END)
		self.entry.set("")
	
	def send(self):
		send = "\t\t\t" + "You: " + self.entry.get()
		self.text.insert(END, "\n" + send)
		self.text.yview(END)
		
		if (self.entry.get() == ""):
			self.msg = "Oops! I am unable to understand this request. Please ask the question again in lower case."
			self.lbl_1.config(text = self.msg, fg = "red")
			
		else:
			self.msg = ""
			self.lbl_1.config(text = self.msg, fg = "red")
		
		if (self.entry.get() == ("hello")):
			self.text.insert(END, "\n\n" + "BOT: Hi")
			
		if (self.entry.get() == "hello"):
			self.text.insert(END, "\n\n" + "BOT: Hi")
		
		elif (self.entry.get() == "hi"):
			self.text.insert(END, "\n\n" + "BOT: Hello")	
		
		elif (self.entry.get() == "how are you?"):
			self.text.insert(END, "\n\n" + "BOT: Fine and you?")
		
		elif (self.entry.get() == "great"):
			self.text.insert(END, "\n\n" + "BOT: That is wonderful to hear!")
		
		elif (self.entry.get() == "who created you?"):
			self.text.insert(END, "\n\n" + "BOT: I was created using python by the members of Tech Geeks Software Solutions !")
		
		elif (self.entry.get() == "what is your name?"):
			self.text.insert(END, "\n\n" + "BOT: My name is Robertoo! Nice to meet you!")	
		
		elif (self.entry.get() == "how do you edit student information?"):
			self.text.insert(END, "\n\n" + "BOT: From the main menu, click the Student Details Button. Where you will then be taken student management system feature where all student information once already added into the localised datbase whill show up on the right hand side of the pannel. Search for the student name and once found click it and it will be shown to the left pannel where the information can be edited and updated.")	
		
		elif (self.entry.get() == "what is the purpose for the student details?"):
			self.text.insert(END, "\n\n" + "BOT: With the options available it will allow you to save, delete, reset, update student`s information in the database.")	
		
		elif (self.entry.get() == "how do you take attendance?"):
			self.text.insert(END, "\n\n" + "BOT: From the main menu, click the Facial Recognition Button. When the feature window pop up click the botton to run the program. A window will pop up showing the video feed for your session. When you are ready to end the session close the window.")	
		
		elif (self.entry.get() == "what is the purpose for the attendance sheet?"):
			self.text.insert(END, "\n\n" + "BOT: With the options available it will allow you to modify past and present attendance records without having to access the database.")	
		
		elif (self.entry.get() == "what is the purpose for the warning list?"):
			self.text.insert(END, "\n\n" + "BOT: With the options available it will allow you view students who missed the class session and email them a warning about their attendance.")	
		
		elif (self.entry.get() == "bye"):
			self.text.insert(END, "\n\n" + "BOT: Thank you for using me I hope that my service has been useful")			
			
		else:
			self.text.insert(END, "\n\n" + "BOT: I am sorry> I am unable to answer this question.")	
			
		
if __name__ == "__main__":
	root = Tk()
	obj = Chatbot(root)
	root.mainloop()
