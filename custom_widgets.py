import tkinter as tk
from tkinter import ttk


class EntryBox:

    entry = None
    value = 0
    on_change_fun = None

    def __init__(self, parent, name, value, fun):
        self.value = value
        self.on_change_fun = fun
        frame = tk.Frame(master=parent, padx=10, pady=5)
        name = tk.Label(master=frame, text=name, font=15)
        buttons_frame = tk.Frame(master=frame)

        val_cmd = frame.register(self.is_valid)
        self.entry_text = tk.StringVar()
        self.entry_text.set(value)
        self.entry_text.trace_add("write", self.on_entry_change)
        self.entry = ttk.Entry(master=frame, textvariable=self.entry_text,
                              validate='key', validatecommand=(val_cmd, '%P'), width=5, font=20, justify='center')

        up_button = ttk.Button(master=buttons_frame, text="+", command=self.increase, width=2)
        down_button = ttk.Button(master=buttons_frame, text="-", command=self.decrease, width=2)

        name.pack(side=tk.TOP)
        self.entry.pack(side=tk.LEFT)
        down_button.pack(side=tk.LEFT)
        up_button.pack(side=tk.LEFT)
        buttons_frame.pack(side=tk.LEFT)
        frame.pack(side=tk.BOTTOM, fill=tk.NONE)

    def increase(self):
        self.value = int(self.value+1)
        self.entry.delete(0, tk.END)
        self.entry.insert(0, str(self.value))

    def decrease(self):
        if self.value == int(self.value) and self.value > 0:
            self.value = int(self.value-1)
        else:
            self.value = int(self.value)
        self.entry.delete(0, tk.END)
        self.entry.insert(0, str(self.value))

    def on_entry_change(self, *args):
        if self.entry.get() != '':
            self.value = float(self.entry.get())
        self.on_change_fun()

    def is_valid(self, v):
        if v:
            if len(v) > 4:
                return False
            try:
                v = float(v)
                if v < 0 or v > 50:
                    return False
                return True
            except ValueError:
                return False
        return True


class Table:

    def __init__(self, root):
        self.table_frame = tk.Frame(master=root)
        # code for creating table
        self.value_label_list = []
        for i in range(total_rows):
            for j in range(total_columns):
                label = tk.Label(self.table_frame, font=('Arial', 16, 'bold'), anchor='w')
                label.grid(row=i, column=j, sticky='w')
                label.config(text=lst[i][j])
                if j == 1:
                    self.value_label_list.append(label)
                    label.config(width=4)

    def update(self, updated_list):
        for i in range(len(self.value_label_list)):
            self.value_label_list[i].config(text='{:.2f}'.format(updated_list[i]))

lst = [("x [m]:", "0"),
        ("y [m]:", "0"),
        ("v [m/s]:", "0"),
        ("a [m/s²]:", "0"),
        ("a_t [m/s²]:", "0"),
        ("a_n [m/s²]:", "0"),
        ("E_c [J]", "0"),
        ("E_k [J]:", "0",),
        ("E_p [J]:", "0"),
        ("\u03BA [m]" , "0")]

total_rows = len(lst)
total_columns = len(lst[0])