import tkinter as tk
from tkinter import *

root = tk.Tk() # Opent a window
root.geometry("490x450") # window dimension
root.title("Calculator") # window title
result = tk.Entry(font = ("Arial", 26)) # geting entry and font size and type
result.grid(row=0,column=0, padx=10, pady=10,ipadx=40 , ipady=20) # size of window for type and show results
result.config(justify=tk.RIGHT) # start tipping point

buttonplaces=tk.Frame() # button place
buttonplaces.grid(row=1,column=0, padx=5, pady=5) # button place in row and column

def creatButton(text,fram,row,column,command,bg="white"): # button function with details.
    button=tk.Button(fram,text=text,command=command, font=("Arial",26),width=3,height=0) # button details
    button.config(bg=bg) # details of bg
    button.grid(row=row,column=column, padx=5,pady=5) # distance bitween button

def addNumber(number): # number action function in result window
    current=result.get() # text in result window.
    current+= str(number) # new text in result window
    result.delete(0,tk.END) # delete last text 
    result.insert(0,current) # enter new text

def addopration(opration): # operation function
    current=result.get() # text in result window
    current+=opration # operation sign in the window
    result.delete(0,tk.END) # delete last text 
    result.insert(0,current) # insert new text

def calculate(): # calculate function
    current=result.get() # text in result
    result.delete(0,tk.END) # delete last text
    result.insert(0,eval(current)) # insert new text as a result

def clear(): # delete text function
    result.delete(0,tk.END) # clear text 
# buttons 
creatButton("7", buttonplaces,0,0,lambda:addNumber(7))
creatButton("8",buttonplaces,0,1, lambda:addNumber(8))
creatButton("9",buttonplaces,0,2, lambda:addNumber(9))
creatButton("+",buttonplaces,0,3, lambda:addopration("+"))
creatButton(".",buttonplaces,0,4, lambda:addNumber("."))

creatButton("4",buttonplaces,1,0, lambda:addNumber(4))
creatButton("5",buttonplaces,1,1, lambda:addNumber(5))
creatButton("6",buttonplaces,1,2, lambda:addNumber(6))
creatButton("-",buttonplaces,1,3, lambda:addopration("-"))

creatButton("1",buttonplaces,2,0, lambda:addNumber(1))
creatButton("2",buttonplaces,2,1, lambda:addNumber(2))
creatButton("3",buttonplaces,2,2, lambda:addNumber(3))
creatButton("x",buttonplaces,2,3, lambda:addopration("*"))

creatButton("C",buttonplaces,3,0, clear,bg="red")
creatButton("0",buttonplaces,3,1, lambda:addNumber(0))
creatButton("/",buttonplaces,3,3, lambda:addopration("/"))

creatButton("=",buttonplaces,3,2, calculate)
# ^ buttons 
root.mainloop() # repeat all of these process