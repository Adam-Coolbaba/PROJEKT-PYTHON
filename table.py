from tkinter import *


class Table:

    def __init__(self, root):
        self.table_frame = Frame(master=root)
        # code for creating table
        self.value_label_list = []
        for i in range(total_rows):
            for j in range(total_columns+1):
                label = Label(self.table_frame, width=20,
                              font=('Arial', 16, 'bold'), anchor='w')

                label.grid(row=i, column=j)
                if j == 0:
                    label.config(text=' '*4)
                else:
                    label.config(text=lst[i][j-1])
                    if j == 2:
                        self.value_label_list.append(label)

    def update(self, updated_list):
        for i in range(len(self.value_label_list)):
            self.value_label_list[i].config(text='{:.2f}'.format(updated_list[i]))

lst = [("x [m]:", "0"),
        ("y [m]:", "0"),
        ("v [m/s]:", "0"),
        ("a [m/s^2]:", "0"),
        ("Ek [J]:", "0"),
        ("Ep [J]:", "0"),
        ("\u03BA [m]" , "0")]

total_rows = len(lst)
total_columns = len(lst[0])

if __name__ == '__main__':
    root = Tk()
    t = Table(root)
    root.mainloop()



