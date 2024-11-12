# import sklearn
# print("hello")

# from tkinter import *
# from tkinter.ttk import *
#
# # writing code needs to
# # create the main window of
# # the application creating
# # main window object named root
# root = Tk()
#
# # giving title to the main window
# root.title("First_Program")
#
# # Label is what output will be
# # show on the window
# label = Label(root, text="Hello World !").pack()
#
# # calling mainloop method which is used
# # when your application is ready to run
# # and it tells the code to keep displaying
# root.mainloop()

# from tkinter import *
# # create a tkinter window
# root = Tk()
# # Open window having dimension 100x100
# root.geometry('100x100')
# # Create a Button
# btn = Button(root, text = 'Click me !', bd = '5', command = root.destroy)
#
# # Set the position of button on the top of window.
# btn.pack(side = 'top')
# root.mainloop()


from tkinter import *
root = Tk()
root.geometry("300x200")
w = Label(root, text ='SMEC', font = "50")
w.pack()

Checkbutton1 = IntVar()
Checkbutton2 = IntVar()
Checkbutton3 = IntVar()

Button1 = Checkbutton(root, text = "Tutorial",
                      variable = Checkbutton1,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 10)

Button2 = Checkbutton(root, text = "Student",
                      variable = Checkbutton2,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 10)

Button3 = Checkbutton(root, text = "Courses",
                      variable = Checkbutton3,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 10)

Button1.pack()
Button2.pack()
Button3.pack()
mainloop()