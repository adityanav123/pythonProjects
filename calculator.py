from tkinter import *
expression = ''
def press(value):
	global expression
	expression = expression + str(value)
	equation.set(expression)

def equals(): # checking for errors.
	try:
		global expression
		total = str(eval(expression))
		equation.set(total)
		expression = ''
	except:
		equation.set('error, check the expression again!')
		expression = ''
def clear():
	global expression
	expression = ''
	equation.set('')
def create_calcuator():
	cal = Tk()
	#creating a Top Down Menu
	menu = Menu(cal)
	cal.config(menu = menu)
	first_menu = Menu(menu)
	menu.add_cascade(label = 'Option', menu = first_menu)
	first_menu.add_command(label = 'Exit', command = cal.destroy)

	other_menu = Menu(menu)
	menu.add_cascade(label = 'Other', menu = other_menu)
	other_menu.add_command(label = 'Version 1.0')

	cal.configure(background = "turquoise")
	cal.title('Calculator!')
	cal.geometry("300x150")
	equation = StringVar() # Entering the expression
	expression_field = Entry(cal, textvariable = equation)
	expression_field.grid(columnspan = 4, ipadx = 78, ipady = 9)
	equation.set('Enter Expression:')


#creating all the buttons 
	b1 = Button(cal, text = '1', command = lambda: press(1), height = 1, width = 7).grid(row = 2, column = 0)
	b2 = Button(cal, text = '2', command = lambda: press(2), height = 1, width = 7).grid(row = 2, column = 1)
	b3 = Button(cal, text = '3', command = lambda: press(3), height = 1, width = 7).grid(row = 2, column = 2)
	b4 = Button(cal, text = '4', command = lambda: press(4), height = 1, width = 7).grid(row = 3, column = 0)
	b5 = Button(cal, text = '5', command = lambda: press(5), height = 1, width = 7).grid(row = 3, column = 1)
	b6 = Button(cal, text = '6', command = lambda: press(6), height = 1, width = 7).grid(row = 3, column = 2)
	b7 = Button(cal, text = '7', command = lambda: press(7), height = 1, width = 7).grid(row = 4, column = 0)
	b8 = Button(cal, text = '8', command = lambda: press(8), height = 1, width = 7).grid(row = 4, column = 1)
	b9 = Button(cal, text = '9', command = lambda: press(9), height = 1, width = 7).grid(row = 4, column = 2)
	b0 = Button(cal, text = '0', command = lambda: press(0), height = 1, width = 7).grid(row = 5, column = 0)
	bplus = Button(cal, text = '+', command = lambda: press('+'), height = 1, width = 7).grid(row = 2, column = 3)
	bsub = Button(cal, text = '-', command = lambda: press('-'), height = 1, width = 7).grid(row = 3, column = 3)
	bmul = Button(cal, text = '*', command = lambda: press('*'), height = 1, width = 7).grid(row = 4, column = 3)
	bdiv = Button(cal, text = '/', command = lambda: press('/'), height = 1, width = 7).grid(row = 5, column = 3)
	bequal = Button(cal, text = '=', command = equals, height = 1, width = 7).grid(row = 5, column = 2)
	clearButton = Button(cal, text = 'AC', command = clear, height = 1, width = 7).grid(row = 5, column=1)
	cal.mainloop()
def main():
	master = Tk()
	master.title('Calculator')
	master.geometry("300x180")
	master.configure(background = 'cyan')
	lb = Label(master, text = 'Calculator',fg = 'green', bg = 'cyan',font=('comicsans', 20))
	entry_button = Button(master, text = 'Enter',bg = 'cyan', fg = 'black',font=('arial', 12), command = create_calcuator)
	exit_button = Button(master, text = 'QUIT',bg = 'cyan', fg = 'black',font=('arial', 12), command = master.destroy)
	lb.pack()
	entry_button.pack(side = LEFT,padx = 55, pady = 10)
	exit_button.pack(side = RIGHT, padx = 40, pady = 10)
	master.mainloop()

main()