from tkinter import *
from tkinter import messagebox
import sys
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import read_excel





def destroy():
    #window.destroy()
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
    x = ["Open", "High", "Low"]
    open = check["Open"]
    high = check["High"]
    low = check["Low"]
    y = [open, high, low]
    plt.plot(x, y)
    plt.show()
    line_graph_2()


def line_graph_2():
    input_value = entry.get()
    destroy()
    df = pd.read_excel('National_Stock_Exchange_of_India_Ltd.xlsx', sheet_name='National_Stock_Exchange_of_Indi')
    df_1 = pd.DataFrame(df)
    # print(df_1)
    check = df_1[df_1["Symbol"] == "HDFC"]
    print(check)
    x = ["Month", "Year"]
    month = check["30 d % chng"]
    year = check["365 d % chng"]

    y = [month, year]
    plt.plot(x, y)
    plt.show()


def bar_graph():
    input_value = entry.get()
    destroy()

    #name = column_name.get()
    df = pd.read_excel('National_Stock_Exchange_of_India_Ltd.xlsx', sheet_name='National_Stock_Exchange_of_Indi')
    df_1 = pd.DataFrame(df)
    #print(df_1)
    check = df_1[df_1["Symbol"] == input_value]
    print(check)
    x = ["Open", "High", "Low"]
    open = check["Open"]
    high = check["High"]
    low = check["Low"]
    y = [open, high, low]
    #y = pd.DataFrame(new)
    #y = [x["Open"], x["High"], x["Low"]]
    #plt.xlabel("Symbol")
    #plt.ylabel("Open")
    plt.bar(x, y)

    plt.show()


def pie_chart():

    input_value = entry.get()
    destroy()
    #name = column_name.get()
    df = pd.read_excel('National_Stock_Exchange_of_India_Ltd.xlsx', sheet_name='National_Stock_Exchange_of_Indi')
    df_1 = pd.DataFrame(df)
    #print(df_1)
    check = df_1[df_1["Symbol"] == input_value]
    print(check)
    x = ["Open", "High", "Low"]
    open = check["Open"]
    high = check["High"]
    low = check["Low"]
    y = [open, high, low]
    fig = plt.figure(figsize=(10, 7))
    plt.pie(y, labels=list(x))

    plt.show()

def num_column():
    global Spinbox
    number = Spinbox.get()
    print(number)





def spin():
    spin = Spinbox(from_= 0, to = 20)
    spin.grid(row=4, column=3)





    #print(vis_list)

### regarding work before 10th


window = Tk()
window.title("DATA VISUALIZATION")
window.config(padx=50, pady=50)
type = Label(text= "Company Name",font=("Arial",12,"normal"))
type.grid(column=2, row= 2)

entry = Entry()
entry.grid(column=3, row=2)

type_1 = Label(text="No of columns", font=("Arial", 12, "normal"))
type_1.grid(column=2, row=4)
spin()

#f number != 0:
#   for i in number:
#       column = i
#       column_name = Entry()
#       column_name.grid(row=5, column=column)
line_button = Button(text="Line Graph", command=line_chart)
line_button.grid(row=7, column=1)
bar_button = Button(text="Bar Graph", command=bar_graph)
bar_button.grid(row=7, column=2)
pie_button = Button(text="Pie Graph", command=pie_chart)
pie_button.grid(row=7, column=3)
input_value = entry.get()

window.mainloop()



