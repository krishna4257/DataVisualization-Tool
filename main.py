from tkinter import *
from tkinter import messagebox, simpledialog
import sys
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import read_excel

final_names = []

def destroy():

    entry.destroy()

    type.destroy()


## To Draw the Line diagram
def line_chart():
    input_value = entry.get()
    destroy()

    df = pd.read_excel('National_Stock_Exchange_of_India_Ltd.xlsx', sheet_name='National_Stock_Exchange_of_Indi')
    df_1 = pd.DataFrame(df)
    final_input = str(input_value)
    check = df_1[df_1["Symbol"] == input_value]
    print(check)
    x=final_names

    y = []

    for i in range(len(final_names)):

        open = check[final_names[i]]
        y.append(open)

    plt.plot(x, y)
    plt.show()



#def bar_graph():
#    df = pd.read_excel("National_Stock_Exchange_of_India_Ltd.xlsx", sheet_name="National_Stock_Exchange_of_Indi")
#
#    x = df["Symbol"]
#    y = df["High"]
#    x_1 = list(x)
#    y_1 = list(y)
#    print(x_1)
#    print(y_1)
#
#    # fig = plt.figure(figsize=(100, 5))
#    # y_1 = float(y)
#    # y = df["Open"].apply(lambda x: float(x))
#    plt.bar(x=x_1, y=y_1, height=0.8, width=0.2)
#    plt.show()
#
#    # sys.stdout.flush()
#    # input_value = entry.get()
#    # destroy()


#
##name = column_name.get()
# df = pd.read_excel('National_Stock_Exchange_of_India_Ltd.xlsx', sheet_name='National_Stock_Exchange_of_Indi')
##df_1 = pd.DataFrame(df)
##print(df_1)
# company_names  = df["Symbol"]
#
# x = [company_names]
# print(x)
# y = df["Open"]
#
# print(float(y))
#
# plt.xlabel("Symbol")
# plt.ylabel("Open")
# plt.bar(x, y)
# plt.show()
#

def pie_chart():
    input_value = entry.get()
    column_name = simpledialog.askstring(title="Column Name",
                                         prompt="Enter the Column Name for which you need the pie chart")
    destroy()

    df = pd.read_excel('National_Stock_Exchange_of_India_Ltd.xlsx', sheet_name='National_Stock_Exchange_of_Indi')
    df_1 = pd.DataFrame(df)
    check = df["Symbol"]
    print(check)
    x = check

    y = df[column_name]
    print(y)
    fig = plt.figure(figsize=(10, 7))
    plt.pie(y, labels=x, autopct='%1.2f%%', textprops={'fontsize': 8})
    #plt.legend(title="Symbols")

    plt.show()


def num_column():
    global Spinbox
    number = Spinbox.get()
    print(number)


column_names = []

#def next_1():
#    num_boxes = int(spin.get())
#    name = entry_1.get()
#
#
#    if len(name) != 0:
#        final_names.append(name)
#    print(final_names)
#    num_boxes-=1
#
#    if num_boxes!= 0:
#        boxes()
#    else:
#        print(final_names)
#
#
#
#
#def boxes():
#
#    global entry_1
#
#    i=1
#    num = [1,2,3,4,5,6,7,8,9,10]
#
#    name = Label(text=f"enter your {num[i]} column name")
#    name.grid(row=6, column=2)
#    entry_1 = Entry()
#    entry_1.grid(row=6, column=3)
#    col = Button(text="next", command=next_1)
#    col.grid(row=6, column=4)
#Open	High	Low	LTP	Chng	% Chng	Volume (lacs)	Turnover (crs.)	52w H	52w L	365 d % chng	30 d % chng

def col_na():
    num_boxes = int(spin.get())
    for i in range(1, num_boxes+1):
        if i == 1:
            column_1 = simpledialog.askstring(title="Column Name",
                                          prompt=f"Enter the {i}st Column Name")
            final_names.append(column_1)
        if i == 2:
            column_1 = simpledialog.askstring(title="Column Name",
                                          prompt=f"Enter the {i}nd Column Name")
            final_names.append(column_1)
        if i == 3:
            column_1 = simpledialog.askstring(title="Column Name",
                                          prompt=f"Enter the {i}rd Column Name")
            final_names.append(column_1)
        if i >= 4:
            column_1 = simpledialog.askstring(title="Column Name",
                                          prompt=f"Enter the {i}th Column Name")
            final_names.append(column_1)


### regarding work before 10th


window = Tk()
window.title("DATA VISUALIZATION")
window.config(padx=50, pady=50)

type = Label(text="Company Name", font=("Arial", 12, "normal"))
type.grid(column=2, row=2)

entry = Entry()
entry.grid(column=3, row=2)

type_1 = Label(text="No of columns", font=("Arial", 12, "normal"))
type_1.grid(column=2, row=4)
spin = Entry()
spin.grid(row=4, column=3)



button = Button(text="click here to enter column names", command=col_na)
button.grid(row=5, column=3)

line_button = Button(text="Line Graph", command=line_chart)
line_button.grid(row=7, column=1)
#bar_button = Button(text="Bar Graph", command=bar_graph)
#bar_button.grid(row=7, column=2)
pie_button = Button(text="Pie Graph", command=pie_chart)
pie_button.grid(row=7, column=3)
input_value = entry.get()

window.mainloop()
