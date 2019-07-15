from tkinter import *
import random
import string

def pass_generate(string_length):
	from_string = string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@$%&_" # strong password
	return ''.join(random.choice(from_string) for i in range(string_length))

def get_str_length():
	return int(spin_box.get())
def show_pass():
	master = Tk()
	master.geometry('400x150')
	master.title('Genrated!')
	password = pass_generate(get_str_length()) # generated password
	lb = Label(master, text = 'Password Generated : \n' + password, font=('comicsans', 15), fg = 'green')
	exit_btn = Button(master, text = 'Exit', width = 15, command = master.destroy)
	lb.pack()
	exit_btn.pack()
	master.mainloop()
window = Tk()
window.title('Password Generator')
window.geometry('300x150')
lb = Label(window, text = 'Password_Generator\n', font=('comicsans', 10))
#SpinBox for selecting no. of characters
spin_box = Spinbox(window, from_=0, to = 20, width = 4)
lb1 = Label(window, text = 'Select No. of characters in password')
button = Button(window, text = 'select', width = 15, command = show_pass)
exit_btn = Button(window, text = 'Exit', width = 15, command = window.destroy) 
lb.pack()
lb1.pack()
spin_box.pack()
button.pack(side = LEFT,pady = 10, padx = 15)
exit_btn.pack(side = RIGHT, padx = 20)
window.mainloop()