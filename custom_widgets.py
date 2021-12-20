import tkinter as tk


class EntryBox:

    entry = None
    value = 0
    on_change_fun = lambda: print("Changed")

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
        self.entry = tk.Entry(master=frame, textvariable=self.entry_text,
                              validate='key', validatecommand=(val_cmd, '%P'), width=5, font=20, justify='center')

        up_button = tk.Button(master=buttons_frame, text="+", command=self.up_action, width=2, height=1)
        down_button = tk.Button(master=buttons_frame, text="-", command=self.down_action, width=2, height=1)

        name.pack(side=tk.TOP)
        self.entry.pack(side=tk.LEFT)
        down_button.pack(side=tk.LEFT)
        up_button.pack(side=tk.LEFT)
        buttons_frame.pack(side=tk.LEFT)
        frame.pack(side=tk.BOTTOM, fill=tk.NONE)

    def up_action(self):
        self.value = int(self.value+1)
        self.entry.delete(0, tk.END)
        self.entry.insert(0, str(self.value))

    def down_action(self):
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
            try:
                float(v)
                return True
            except ValueError:
                return False
        return True
