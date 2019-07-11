from tkinter import *
#
#

class Calc(Tk):
   def __init__(self):
       self.total = 0
       self.current = ""
       self.new_num = True
       self.op_pending = False
       self.op = ""
       self.eq = False
       
       
   def sum(self):
       if self.op == "addition":
           self.total += self.current
       if self.op == "subtraction":
           self.total -= self.current
       if self.op == "multiplication":
           self.total *= self.current
       if self.op == "division":
           self.total /= self.current
       self.new_num = True
       self.op_pending = False
       self.display(self.total)
       

   def calc_total(self):
       self.eq = True
       self.current = float(self.current)
       if self.op_pending == True:
           self.sum()
       else:
           self.total = float(text_box.get())
           
           
   def num_press(self, num):
       self.eq = False
       temp = text_box.get()
       temp2 = str(num)      
       if self.new_num:
           self.current = temp2
           self.new_num = False
       else:
           if temp2 == '.':
               if temp2 in temp:
                   return
           self.current = temp + temp2
       self.display(self.current)


   def display(self, value):
       text_box.delete(0, END)
       text_box.insert(0, value)

   def sign(self):
       self.eq = False
       self.current = -(float(text_box.get()))
       self.display(self.current)
       

   def operation(self, op): 
       self.current = float(self.current)
       if self.op_pending:
           self.sum()
       elif not self.eq:
           self.total = self.current
       self.new_num = True
       self.op_pending = True
       self.op = op
       self.eq = False
       

   def cancel(self):
       self.eq = False
       self.current = "0"
       self.display(0)
       self.new_num = True
       

   def all_cancel(self):
       self.cancel()
       self.total = 0



total = Calc()
main = Tk()
calc = Frame(main)
calc.grid()

# text_box

main.title("*Calculator*")
main.geometry("20x160")
text_box = Entry(calc, justify=LEFT, fg = "black",)
text_box.grid(row = 0, column = 0, columnspan = 4, pady = 5)
text_box.insert(0, "0")

# number box's 1-9
# lambda example: [map(lambda x: (float(5)/9)*(x-32), Fahrenheit)]
# use lambda for calculations

numbers = "789456123"
num = 0
bttn = []
for num1 in range(1,4):
   for num2 in range(3):
       bttn.append(Button(calc, fg = "blue", text = numbers[num]))
       bttn[num].grid(row = num1, column = num2, padx = 5)
       bttn[num]["command"] = lambda x = numbers[num]: total.num_press(x)
       num += 1

# button 0

bttn0 = Button(calc, text = "0", fg = "blue")
bttn0["command"] = lambda: total.num_press(0)
bttn0.grid(row = 4, column = 1)

# button plus

plus = Button(calc, text = "+", fg = "blue")
plus["command"] = lambda: total.operation("addition")
plus.grid(row = 4, column = 3)

# button minus

minus = Button(calc, text = "-", fg = "blue")
minus["command"] = lambda: total.operation("subtraction")
minus.grid(row = 3, column = 3)

# button multiplication

multiply = Button(calc, text = "x", fg = "blue")
multiply["command"] = lambda: total.operation("multiplication")
multiply.grid(row = 2, column = 3)

# button divide

divide = Button(calc, text = "/", fg = "blue")
divide["command"] = lambda: total.operation("division")
divide.grid(row = 1, column = 3)

# button decimal

decimal = Button(calc, text = ".", fg = "blue")
decimal["command"] = lambda: total.num_press(".")
decimal.grid(row = 4, column = 2)

# blank button/ no function

blank = Button(calc, text = (""))
blank.grid(row = 4, column = 0)

# button positive/negative

posNeg= Button(calc, text = "+/-", fg = "blue")
posNeg["command"] = total.sign
posNeg.grid(row = 5, column = 0)

# button cancel

cancel = Button(calc, text = "C", fg = "blue")
cancel["command"] = total.cancel
cancel.grid(row = 5, column = 1)

# button all clear

allClear = Button(calc, text = "AC", fg = "blue")
allClear["command"] = total.all_cancel
allClear.grid(row = 5, column = 2)

# button equals

equal = Button(calc, text = "=", fg = "blue")
equal["command"] = total.calc_total
equal.grid(row = 5, column = 3)

main.mainloop()