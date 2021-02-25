from tkinter import *
import tkinter.font as font

expression = "" 
 
def press(num): 
    global expression 
 
    expression = expression + str(num) 
 
    equation.set(expression) 
 

def equalpress(): 
    try: 
 
        global expression 
 
        total = str(eval(expression)) 
 
        equation.set(total) 
 
        expression = "" 
 
    except: 
 
        equation.set(" error ") 
        expression = "" 
 
def clear(): 
    global expression 
    expression = "" 
    equation.set("")

def square():
    global expression
    expression = expression + str(num)
    equation.set(expression*expression)

def changeOnHover(button, colorOnHover, colorOnLeave): 

    # adjusting backgroung of the widget 
    # background on entering widget 
    button.bind("<Enter>", func=lambda e: button.config( 
        background=colorOnHover)) 

    # background color on leving widget 
    button.bind("<Leave>", func=lambda e: button.config( 
        background=colorOnLeave)) 
 
if __name__ == "__main__": 
    gui = Tk()
    frame=Frame(gui)
 
    #gui.configure(background="light green")
    gui.attributes('-alpha',0.9) 
 
    gui.title("Blaze") 

    gui.iconbitmap("images/jarvis.ico")

    gui.geometry("355x450") 
 
    equation = StringVar()

    Grid.columnconfigure(gui, 0, weight=1)
    Grid.columnconfigure(gui, 1, weight=1)
    Grid.columnconfigure(gui, 2, weight=1)
    Grid.rowconfigure(gui, 1, weight=1)
    Grid.rowconfigure(gui, 2, weight=1)
    Grid.rowconfigure(gui, 3, weight=1)
    Grid.rowconfigure(gui, 4, weight=1)
    Grid.rowconfigure(gui, 5, weight=1)
    Grid.rowconfigure(gui, 6, weight=1)
    
    expression_field = Entry(gui, textvariable=equation) 
    expression_field.grid(columnspan=10, ipadx=150)

    button1 = Button(gui, text=' 1 ', fg='black', bg='red', command=lambda: press(1), height=2, width=6) 
    button1.grid(row=1, column=0, sticky=N+S+E+W)
 
    button2 = Button(gui, text=' 2 ', fg='black', bg='red', 
                    command=lambda: press(2), height=2, width=6) 
    button2.grid(row=1, column=1, sticky=N+S+E+W)

    button3 = Button(gui, text=' 3 ', fg='black', bg='red', 
                    command=lambda: press(3), height=2, width=6) 
    button3.grid(row=1, column=2, sticky=N+S+E+W) 

    button4 = Button(gui, text=' 4 ', fg='black', bg='red', 
                    command=lambda: press(4), height=2, width=6) 
    button4.grid(row=2, column=0, sticky=N+S+E+W) 
 
    button5 = Button(gui, text=' 5 ', fg='black', bg='red', 
                    command=lambda: press(5), height=2, width=6) 
    button5.grid(row=2, column=1, sticky=N+S+E+W) 
 
    button6 = Button(gui, text=' 6 ', fg='black', bg='red', 
                    command=lambda: press(6), height=2, width=6) 
    button6.grid(row=2, column=2, sticky=N+S+E+W) 
 
    button7 = Button(gui, text=' 7 ', fg='black', bg='red', 
                    command=lambda: press(7), height=2, width=6) 
    button7.grid(row=3, column=0, sticky=N+S+E+W) 
 
    button8 = Button(gui, text=' 8 ', fg='black', bg='red', 
                    command=lambda: press(8), height=2, width=6) 
    button8.grid(row=3, column=1, sticky=N+S+E+W) 
 
    button9 = Button(gui, text=' 9 ', fg='black', bg='red', 
                    command=lambda: press(9), height=2, width=6) 
    button9.grid(row=3, column=2, sticky=N+S+E+W) 
 
    button0 = Button(gui, text=' 0 ', fg='black', bg='red', 
                    command=lambda: press(0), height=2, width=6) 
    button0.grid(row=4, column=1, sticky=N+S+E+W) 
 
    plus = Button(gui, text=' + ', fg='black', bg='red', 
                command=lambda: press("+"), height=2, width=6) 
    plus.grid(row=5, column=0, sticky=N+S+E+W) 
 
    minus = Button(gui, text=' - ', fg='black', bg='red', 
                command=lambda: press("-"), height=2, width=6) 
    minus.grid(row=5, column=2, sticky=N+S+E+W) 

    multiply = Button(gui, text=' * ', fg='black', bg='red', 
                    command=lambda: press("*"), height=2, width=6) 
    multiply.grid(row=4, column=0, sticky=N+S+E+W) 
 
    divide = Button(gui, text=' / ', fg='black', bg='red', 
                    command=lambda: press("/"), height=2, width=6) 
    divide.grid(row=4, column=2, sticky=N+S+E+W) 
 
    equal = Button(gui, text=' = ', fg='black', bg='red', 
                            command=equalpress, height=2, width=6) 
    equal.grid(row=5, column=1, sticky=N+S+E+W)

    point = Button(gui, text=' . ', fg='black', bg='red', 
                            command=lambda: press("."), height=2, width=6) 
    point.grid(row=6, column=1, sticky=N+S+E+W)

    clear = Button(gui, text=' C ', fg='black', bg='red', 
                            command=clear, height=2, width=6) 
    clear.grid(row=6, column=0, sticky=N+S+E+W)

    exitbutton = Button(gui, text=' Exit ', fg='black', bg='red', 
                            command=gui.quit, height=2, width=6) 
    exitbutton.grid(row=6, column=2, sticky=N+S+E+W) 
    
    changeOnHover(button1,"grey", "red")
    changeOnHover(button2,"grey", "red")
    changeOnHover(button3,"grey", "red")
    changeOnHover(button4,"grey", "red")
    changeOnHover(button5,"grey", "red")
    changeOnHover(button6,"grey", "red")
    changeOnHover(button7,"grey", "red")
    changeOnHover(button8,"grey", "red")
    changeOnHover(button9,"grey", "red")
    changeOnHover(button0,"grey", "red")
    changeOnHover(minus,"grey", "red")
    changeOnHover(plus,"grey", "red")
    changeOnHover(multiply,"grey", "red")
    changeOnHover(divide,"grey", "red")
    changeOnHover(equal,"grey", "red")
    changeOnHover(point,"grey", "red")
    changeOnHover(clear,"grey", "red")
    changeOnHover(exitbutton,"grey", "red")

    gui.mainloop() 
