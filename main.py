from tkinter import *
from tkinter import messagebox, simpledialog
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px


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
    columns = df_1.columns
    column_name = df_1[columns[0]]

    final_input = str(input_value)
    check = df_1[column_name == input_value]

    x=final_names

    y = []

    for i in range(len(final_names)):

        open = check[final_names[i]]
        y.append(open)

    plt.plot(x, y)
    plt.show()



def bar_graph():
    df = pd.read_excel("National_Stock_Exchange_of_India_Ltd.xlsx", sheet_name="National_Stock_Exchange_of_Indi")

    column_names = df.columns

    column_name = simpledialog.askstring(title="Column Name",
                                         prompt="Enter the Column Name for which you need the bar chart")
    column = df[column_name]

    x_axis = df[column_names[0]]

    fig = px.bar(x=x_axis, y=column)
    fig.show()




def pie_chart():
    input_value = entry.get()
    column_name = simpledialog.askstring(title="Column Name",
                                         prompt="Enter the Column Name for which you need the pie chart")
    destroy()

    df = pd.read_excel('National_Stock_Exchange_of_India_Ltd.xlsx', sheet_name='National_Stock_Exchange_of_Indi')
    column = df[column_name]

    fig = px.pie(names=df.Symbol, values=column)
    fig.show()



def num_column():
    global Spinbox
    number = Spinbox.get()
    print(number)


column_names = []


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
bar_button = Button(text="Bar Graph", command=bar_graph)
bar_button.grid(row=7, column=2)
pie_button = Button(text="Pie Graph", command=pie_chart)
pie_button.grid(row=7, column=3)
input_value = entry.get()

window.mainloop()
