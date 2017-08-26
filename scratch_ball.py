import tkinter

def print_hello(event):
    print('5')

root = tkinter.Tk()

button = tkinter.Button(root, text = "Button")
button.bind("<Button-1>", print_hello)

button.pack

root.mainloop()
