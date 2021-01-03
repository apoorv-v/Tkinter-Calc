from tkinter import *

root = Tk()

text_box = Entry(root, width=40)
text_box.grid(row=0, column=0, columnspan="3")
text_box.delete(0, END)
button_values = {
    "button_one": 1,
    "button_two": 2,
    "button_three": 3,
    "button_four": 4,
    "button_five": 5,
    "button_six": 6,
    "button_seven": 7,
    "button_eight": 8,
    "button_nine": 9,
    "button_zero": 0
}

button_operator = {
    "button_add": "+",
    "button_sub": "-",
    "button_mul": "*",
    "button_div": "/",
    "button_equate": "="
}

cordinates = {"row": 1, "col": 0}


def grid_increment(cordinates):
    if cordinates["col"] < 2:
        cordinates["col"] += 1

    else:
        cordinates["col"] -= cordinates["col"]
        cordinates["row"] += 1



buttons = []
to_clear = False

def evaluate(sign):
    global firstnumber
    global last_sign
    if sign == '=':
        """check the last sign"""
        if last_sign == '+':
            answer = firstnumber + int(text_box.get())
        elif last_sign == '-':
            answer = firstnumber - int(text_box.get())
        elif last_sign == '*':
            answer = firstnumber * int(text_box.get())
        elif last_sign == '/':
            try:
                answer = firstnumber / int(text_box.get())
            except:
                text_box.insert(0, 'can not divide by 0!')
        text_box.delete(0, END)
        text_box.insert(0, str(answer))

    else:
        firstnumber = int(text_box.get())
        last_sign = sign

        to_clear= True
        clear()


def clear():
    text_box.delete(0, END)

def put_num(number = 0, to_clear= False):
    if to_clear:
        clear()
        return
    existing = text_box.get()
    text_box.delete(0, END)
    text_box.insert(0, str(existing) + str(number))




#button_values[butts]
# for butts in button_values.keys():
#     buttons.append(
#         Button(root, text=str(button_values[butts]), padx=30, pady=20))
#     # print(button_values[butts]
#     buttons[-1].grid(row=cordinates["row"], column=cordinates["col"])
#     grid_increment(cordinates)



temp_button = Button(root, text='1', padx=30, pady=20, command= lambda : put_num(1))
temp_button.grid(row=cordinates["row"], column=cordinates["col"])
grid_increment(cordinates)
buttons.append(temp_button)
temp_button = Button(root, text='2', padx=30, pady=20, command= lambda : put_num(2))
temp_button.grid(row=cordinates["row"], column=cordinates["col"])
grid_increment(cordinates)
buttons.append(temp_button)
temp_button = Button(root, text='3', padx=30, pady=20, command= lambda : put_num(3))
temp_button.grid(row=cordinates["row"], column=cordinates["col"])
grid_increment(cordinates)
buttons.append(temp_button)
temp_button = Button(root, text='4', padx=30, pady=20, command= lambda : put_num(4))
temp_button.grid(row=cordinates["row"], column=cordinates["col"])
grid_increment(cordinates)
buttons.append(temp_button)
temp_button = Button(root, text='5', padx=30, pady=20, command= lambda : put_num(5))
temp_button.grid(row=cordinates["row"], column=cordinates["col"])
grid_increment(cordinates)
buttons.append(temp_button)
temp_button = Button(root, text='6', padx=30, pady=20, command= lambda : put_num(6))
temp_button.grid(row=cordinates["row"], column=cordinates["col"])
grid_increment(cordinates)
buttons.append(temp_button)
temp_button = Button(root, text='7', padx=30, pady=20, command= lambda : put_num(7))
temp_button.grid(row=cordinates["row"], column=cordinates["col"])
grid_increment(cordinates)
buttons.append(temp_button)
temp_button = Button(root, text='8', padx=30, pady=20, command= lambda : put_num(8))
temp_button.grid(row=cordinates["row"], column=cordinates["col"])
grid_increment(cordinates)
buttons.append(temp_button)
temp_button = Button(root, text='9', padx=30, pady=20, command= lambda : put_num(9))
temp_button.grid(row=cordinates["row"], column=cordinates["col"])
grid_increment(cordinates)
buttons.append(temp_button)
temp_button = Button(root, text='0', padx=30, pady=20, command= lambda : put_num(0))
temp_button.grid(row=cordinates["row"], column=cordinates["col"])
grid_increment(cordinates)
buttons.append(temp_button)


temp_button = Button(root, text='+', padx=30, pady=20, command= lambda : evaluate('+'))
temp_button.grid(row=cordinates["row"], column=cordinates["col"])
grid_increment(cordinates)
buttons.append(temp_button)
temp_button = Button(root, text='-', padx=30, pady=20, command= lambda : evaluate('-'))
temp_button.grid(row=cordinates["row"], column=cordinates["col"])
grid_increment(cordinates)
buttons.append(temp_button)
temp_button = Button(root, text='*', padx=30, pady=20, command= lambda : evaluate('*'))
temp_button.grid(row=cordinates["row"], column=cordinates["col"])
grid_increment(cordinates)
buttons.append(temp_button)
temp_button = Button(root, text='/', padx=30, pady=20, command= lambda : evaluate('/'))
temp_button.grid(row=cordinates["row"], column=cordinates["col"])
grid_increment(cordinates)
buttons.append(temp_button)
temp_button = Button(root, text='=', padx=30, pady=20, command= lambda : evaluate('='))
temp_button.grid(row=cordinates["row"], column=cordinates["col"])
grid_increment(cordinates)
buttons.append(temp_button)
# appearance is set up

clear_button = Button(root, text="clear", padx = 90, pady= 20, command= clear)
clear_button.grid(row = cordinates['row'], column=cordinates['col'], columnspan=3)
root.mainloop()
