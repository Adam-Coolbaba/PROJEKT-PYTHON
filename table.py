from tkinter import *


class Table:

    def __init__(self, root):
        self.table_frame = Frame(master=root)
        # code for creating table
        self.value_label_list = []
        for i in range(total_rows):
            for j in range(total_columns):
                label = Label(self.table_frame, width=20, fg='blue',
                              font=('Arial', 16, 'bold'))

                label.grid(row=i, column=j)
                label.config(text=lst[i][j])
                if j == 1:
                    self.value_label_list.append(label)

    def update(self, updated_list):
        for i in range(len(self.value_label_list)):
            text = ''
            if isinstance(updated_list[i],float):
                text = '{:.2f}'.format(updated_list[i])
            else:
                text = updated_list[i]
            self.value_label_list[i].config(text=text)

lst = [("x [m]", "0"),
        ("y [m]", "0"),
        ("v [m/s]", "0"),
        ("a [m/s^2]", "0"),
        ("Ek [J]", "0"),
        ("Ep [J]", "0"),
        ("R [m]" , "0")]

total_rows = len(lst)
total_columns = len(lst[0])

if __name__ == '__main__':
    root = Tk()
    t = Table(root)
    root.mainloop()



