import tkinter as tk
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from custom_widgets import EntryBox

#TODO:
# 1)Poprawa funkcji down_action() (powinna pozwalać na ustawienie do 0)
# 2)Poprwa grafiki (kszatałt i wielkość przycisków i pól do wpisywania, pobawienie się z rozszerzaniem)
# 3)Potencjalnie zamiast używania mein_frame i entry_frame zrobić kształy przy użyciu .grid()
# 4)Jeśli się da, sprawienie aby okienka nie dało się zmnijeszyć bardziej niż wielkość wykresu


def update_graph():
    update_line()
    update_axis()
    fig.canvas.draw()


def update_line():
    global w_x, w_y, a_x, a_y, f
    line.set_ydata(a_y.value * np.sin(w_y.value * t + np.pi / 6 * f.value))
    line.set_xdata(a_x.value * np.sin(w_x.value * t))


def update_axis():
    subplot.set_aspect('equal', adjustable='datalim')
    subplot.relim()
    subplot.autoscale_view()


def _quit():
    root.quit()
    root.destroy()


GRAPH_SIZE = 6
FONT_SIZE = 15
root = tk.Tk()
root.wm_title("Wykres drgan prostopadlych")

main_frame = tk.Frame(master=root)
entry_frame = tk.Frame(master=main_frame)

a_y = EntryBox(entry_frame, "A\u2082", 1, update_graph)
a_x = EntryBox(entry_frame, "A\u2081", 1, update_graph)
w_y = EntryBox(entry_frame, "\u03C9\u2082", 1, update_graph)
w_x = EntryBox(entry_frame, "\u03C9\u2081", 1, update_graph)
f = EntryBox(entry_frame, "\u0394\u03C6 (*\u03C0/6)", 3, update_graph)

t = np.arange(0, 100, 0.001)
x = a_x.value*np.sin(w_y.value*t)
y = a_y.value*np.sin(w_x.value*t + np.pi/6*f.value)

fig = Figure(figsize=(GRAPH_SIZE, GRAPH_SIZE), dpi=100)
subplot = fig.add_subplot(111)
line, = subplot.plot(x, y, 'g-')

fig.supxlabel("x [m]", fontsize=FONT_SIZE)
fig.supylabel("y [m]", fontsize=FONT_SIZE)
fig.suptitle(f'Wykres', fontsize=FONT_SIZE)

canvas = FigureCanvasTkAgg(fig, master=main_frame)
canvas.get_tk_widget().pack(side=tk.LEFT)
canvas.draw()

entry_frame.pack(side=tk.LEFT)

main_frame.pack()
button = tk.Button(master=root, text="Zamknij", command=_quit)
button.pack(side=tk.BOTTOM)

tk.mainloop()


#Propozycja jak będziemy mieli za dużo czasu:
def Td():
    ax = plt.axes(projection='3d')

    t = np.arange(0,10,0.01)
    x = np.sin(2*t)
    y = np.sin(4*t)
    z = np.sin(6*t)

    ax.plot3D(x,y,z,'g-')
    plt.show()

#Td()

