from tkinter import *


class Table:

    def __init__(self, root):

        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=20, fg='blue',
                               font=('Arial', 16, 'bold'))

                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])

lst = [("x[m]", "value1"),
        ("y[m]", "value2"),
        ("v [m/s]", "value3"),
        ("a[m/s^2]", "value4"),
        ("Ek [J]", "value5"),
        ("Ep [J]", "value6"),
        ("R [m]" , "value7")]

total_rows = len(lst)
total_columns = len(lst[0])

# root = Tk()
# t = Table(root)
# root.mainloop()



