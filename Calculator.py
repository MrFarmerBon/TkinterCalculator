#imports
from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import math
calculator = Tk()
calculator.title("Benulator")
calculator.geometry("570x244")
inputList = []
outputList=[0]
ShownInputList = []
pi = math.pi
InputOutputBox = Label(calculator, text="Enter An Equation")
InputOutputBox.grid(row=0, column=0,columnspan=6)
def ButtonPressed(button_press,button_shown):
    inputList.append(button_press)
    ShownInputList.append(button_shown)
    print(inputList)
    InputOutputBox.config(text=ShownInputList)
def equals(binary,hexidec,octal,percent):
    equation = ''.join([str(elem) for elem in inputList])
    print(equation)
    if "**" in equation:
        equation = equation.replace("**", "*")
    if "&2" in equation:
        equation = equation.replace("&2", "**2")
    if "&3" in equation:
        equation = equation.replace("&3", "**3")
    if "math.sin*" in equation :
        equation = equation.replace("math.sin*(", "math.sin(")
    if "math.cos*" in equation :
        equation = equation.replace("math.cos*(", "math.cos(")
    if "math.tan*" in equation :
        equation = equation.replace("math.tan*(", "math.tan(")
    if "//" in equation:
        print("Error Syntax")
        messagebox.showerror(title="Syntax Error", message="Invaild Syntax")  
        inputList.clear()
        ShownInputList.clear()
    print(equation)
    try:
        if percent == True:
            answer = eval(equation)
            answer = answer*100
            InputOutputBox.config(text=str(answer)+"%")
            outputList.append(answer)
            inputList.clear()
            ShownInputList.clear()

        if binary == True:
            try:
                answer = bin(eval(equation))
                answer = answer.replace("0b","")
                print(answer)
                InputOutputBox.config(text=answer)
                outputList.append(answer)
                inputList.clear()
                ShownInputList.clear()
            except:
                print("Binary Error")
                messagebox.showerror(title="Binary Error", message="Please Enter a Whole Number")  
                inputList.clear()
                ShownInputList.clear()
        if octal == True:
            try:
                answer = oct(eval(equation))
                answer = answer.replace("0o","")
                print(answer)
                outputList.append(answer)
                InputOutputBox.config(text=answer)
                inputList.clear()
                ShownInputList.clear()
            except:
                print("Octal Error")
                messagebox.showerror(title="Octal Error", message="Please Enter a Whole Number")  
                inputList.clear()
                ShownInputList.clear()
        if hexidec == True:
            try:
                answer = hex(eval(equation))
                answer = answer.replace("0x","")
                outputList.append(answer)
                print(answer)
                InputOutputBox.config(text=answer)
                inputList.clear()
                ShownInputList.clear()
            except TypeError:
                print("Hex Error")
                messagebox.showerror(title="Hex Error", message="Please Enter a Whole Number")  
                inputList.clear()
                ShownInputList.clear()

        if  percent == False and binary == False and hexidec == False and octal == False:
            answer = eval(equation)
            print(answer)
            outputList.append(answer)
            InputOutputBox.config(text=answer)
            inputList.clear()
            ShownInputList.clear()       
    except ZeroDivisionError:
        print("Error Dividing By 0")
        messagebox.showerror(title="Division Error", message="Division By 0 Is Impossible")
        inputList.clear()
        ShownInputList.clear()
        InputOutputBox.config(text=ShownInputList)
    except SyntaxError or AttributeError:
        print("Error Syntax")
        messagebox.showerror(title="Syntax Error", message="Invaild Syntax")  
        inputList.clear()
        ShownInputList.clear()
        InputOutputBox.config(text=ShownInputList)
    except ValueError:
        print("Error Value")
        messagebox.showerror(title="Value Error", message="Value to large to print")  
        inputList.clear()
        ShownInputList.clear()
        InputOutputBox.config(text=ShownInputList)

def clear():
    inputList.clear()
    ShownInputList.clear()
    InputOutputBox.config(text=ShownInputList)
def backspace():
    try:
        inputList.pop()
        ShownInputList.pop()
        InputOutputBox.config(text=ShownInputList)
    except IndexError:
        pass
def destroy():
    calculator.destroy()
#1 Button:
button1 = Button(calculator, text='1', height=3, width=7,command=lambda sign="1",text="1" : ButtonPressed(sign,text))
button1.grid(row=2, column=0)
#2 Button
button2 = Button(calculator, text='2', height=3, width=7,command=lambda sign="2",text="2": ButtonPressed(sign,text))
button2.grid(row=2, column=1)
#3 Button
button3 = Button(calculator, text='3', height=3, width=7,command=lambda sign="3",text="3": ButtonPressed(sign,text))
button3.grid(row=2, column=2)
#4 Button
button4 = Button(calculator, text='4',  height=3, width=7,command=lambda sign="4",text="4": ButtonPressed(sign,text))
button4.grid(row=3, column=0)
#5 Button
button5 = Button(calculator, text='5', height=3, width=7,command=lambda sign="5",text="5": ButtonPressed(sign,text))
button5.grid(row=3, column=1)
#6 Button
button6 = Button(calculator, text='6', height=3, width=7,command=lambda sign="6",text="6": ButtonPressed(sign,text))
button6.grid(row=3, column=2)
#7 Button
button7 = Button(calculator, text='7', height=3, width=7,command=lambda sign="7",text="7": ButtonPressed(sign,text))
button7.grid(row=4, column=0)
#8 Button
button8 = Button(calculator, text='8', height=3, width=7,command=lambda sign="8",text="8": ButtonPressed(sign,text))
button8.grid(row=4, column=1)
#9 Button
button9 = Button(calculator, text='9', height=3, width=7,command=lambda sign="9",text="9": ButtonPressed(sign,text))
button9.grid(row=4, column=2)
#0 Button
button0 = Button(calculator, text='0', height=3, width=7,command=lambda sign="0",text="0": ButtonPressed(sign,text))
button0.grid(row=5, column=1)
#+ Button
buttonPlus = Button(calculator, text='+', height=3, width=7,command=lambda sign="+",text="+": ButtonPressed(sign,text))
buttonPlus.grid(row=5, column=3)
#- Button
buttonMinus= Button(calculator, text='-', height=3, width=7,command=lambda sign="-",text="-": ButtonPressed(sign,text))
buttonMinus.grid(row=5, column=2)
#* Button
buttonMultipy= Button(calculator, text='x', height=3, width=7,command=lambda sign="*",text="x": ButtonPressed(sign,text))
buttonMultipy.grid(row=4, column=3)
# ÷ Button 
buttonDivide= Button(calculator, text='÷', height=3, width=7,command=lambda sign="/",text="÷": ButtonPressed(sign,text))
buttonDivide.grid(row=3, column=3)
#. Button
buttonDecimal= Button(calculator, text='.', height=3, width=7,command=lambda sign=".",text=".": ButtonPressed(sign,text))
buttonDecimal.grid(row=5, column=0)
#Clear Button
buttonClear= Button(calculator, text='Clear', height=3, width=7,command=lambda: clear())
buttonClear.grid(row=5, column=5)
#Backspace Button
buttonBackSpace= Button(calculator, text='←', height=3, width=7,command=lambda: backspace())
buttonBackSpace.grid(row=2, column=4)
#= Button
buttonEquals= Button(calculator, text='=', height=3, width=7,command=lambda: equals(percent=False,binary=False,hexidec=False,octal=False))
buttonEquals.grid(row=2, column=3)
#( Button
buttonOpenBracket= Button(calculator, text='(', height=3, width=7,command=lambda sign="*(",text="(": ButtonPressed(sign,text))
buttonOpenBracket.grid(row=3, column=5)
#) Button
buttonCloseBracket= Button(calculator, text=')', height=3, width=7,command=lambda sign=")",text=")": ButtonPressed(sign,text))
buttonCloseBracket.grid(row=4, column=5)	
#Sin Button
buttonSin= Button(calculator, text='Sin', height=3, width=7,command=lambda sign="math.sin(",text="Sin(": ButtonPressed(sign,text))
buttonSin.grid(row=3, column=4)
#Cos Button
buttonCos= Button(calculator, text='Cos', height=3, width=7,command=lambda sign="math.cos(",text="Cos(": ButtonPressed(sign,text))
buttonCos.grid(row=4, column=4)
#Tan Button
buttonTan= Button(calculator, text='Tan', height=3, width=7,command=lambda sign="math.tan(",text="Tan(": ButtonPressed(sign,text))
buttonTan.grid(row=5, column=4)
#Pi Button
buttonPi= Button(calculator, text='π', height=3, width=7,command=lambda sign="pi",text="π": ButtonPressed(sign,text))
buttonPi.grid(row=2, column=5)
#Squared Button
buttonSquared= Button(calculator, text='x²', height=3, width=7,command=lambda sign="&2",text="²": ButtonPressed(sign,text))
buttonSquared.grid(row=2, column=6)
#Cubed Button
buttonCubed= Button(calculator, text='x³', height=3, width=7,command=lambda sign="&3",text="³": ButtonPressed(sign,text))
buttonCubed.grid(row=3, column=6)
#Ans Button
buttonAns = Button(calculator, text='Ans', height=3, width=7, command=lambda: ButtonPressed(outputList[-1],button_shown="Ans")) 
buttonAns.grid(row=4, column=6)
#Root Button
buttonRoot= Button(calculator, text='√', height=3, width=7,command=lambda sign="math.sqrt(",text="√(": ButtonPressed(sign,text))
buttonRoot.grid(row=5, column=6)
#Bin Button
buttonBin= Button(calculator, text='Bin', height=3, width=7,command=lambda : equals(percent=False,binary=True,hexidec=False,octal=False))
buttonBin.grid(row=5, column=7)
#Hex Button
buttonHex= Button(calculator, text='Hex', height=3, width=7,command=lambda : equals(percent=False,hexidec=True,binary=False,octal=False))
buttonHex.grid(row=4, column=7)
#Oct Button
buttonOct= Button(calculator, text='Oct', height=3, width=7,command=lambda : equals(percent=False,octal=True,hexidec=False,binary=False))
buttonOct.grid(row=3, column=7)
#Percent Button
buttonPercent = Button(calculator, text='%', height=3, width=7,command=lambda : equals(percent = True,octal=False,hexidec=False,binary=False))
buttonPercent.grid(row=5, column=8)
#Factorial Button
buttonFactorial = Button(calculator, text='!', height=3, width=7,command=lambda sign="math.factorial(",text="!(": ButtonPressed(sign,text) )
buttonFactorial.grid(row=4, column=8)
#Log Button
buttonLog = Button(calculator, text='Log', height=3, width=7,command=lambda sign="math.log10(",text="log(": ButtonPressed(sign,text) )
buttonLog.grid(row=3, column=8)
#Exit Button
buttonExit= Button(calculator, text="Exit", command=calculator.destroy)
buttonExit.grid(row=2, column=7)
calculator.mainloop()	
print(outputList)
