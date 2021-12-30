import tkinter as tk
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import dynamics
from custom_widgets import EntryBox


def update_graph():
    update_line()
    plot_potential()
    update_axis()
    fig.canvas.draw()
    potential_fig.canvas.draw()


def update_line():
    global w_x, w_y, a_x, a_y, f
    line.set_ydata(a_y.value * np.sin(w_y.value * t + np.pi / 6 * f.value))
    line.set_xdata(a_x.value * np.sin(w_x.value * t))


def update_axis():
    subplot.set_aspect('equal', adjustable='datalim')
    subplot.relim()
    subplot.autoscale_view()


def set_up_canvas(figure):
    c = FigureCanvasTkAgg(figure, master=main_frame)
    c.get_tk_widget().pack(side=tk.LEFT)
    c.draw()


def plot_potential():
    potential_subplot.cla()
    a = a_x.value if a_x.value > a_y.value else a_y.value
    x = np.arange(-a - .5, a + .5, 0.1)
    y = np.arange(-a - .5, a + .5, 0.1)
    x, y = np.meshgrid(x, y)
    z = dynamics.calc_potential_energy(a_x.value, w_x.value, x) + dynamics.calc_potential_energy(a_y.value, w_y.value, y)
    potential_subplot.plot_surface(x, y, z)


def _quit():
    root.quit()
    root.destroy()


GRAPH_SIZE = 6
FONT_SIZE = 15

root = tk.Tk()
root.wm_title("Wykres drgan prostopadlych")
root.resizable(False, False)

main_frame = tk.Frame(master=root)
entry_frame = tk.Frame(master=main_frame)

a_y = EntryBox(entry_frame, "A\u2082:", 1, update_graph)
a_x = EntryBox(entry_frame, "A\u2081:", 1, update_graph)
w_y = EntryBox(entry_frame, "\u03C9\u2082:", 1, update_graph)
w_x = EntryBox(entry_frame, "\u03C9\u2081:", 1, update_graph)
f = EntryBox(entry_frame, "\u0394\u03C6 (*\u03C0/6):", 3, update_graph)

t = np.arange(0, 100, 0.001)
x = a_x.value*np.sin(w_y.value*t)
y = a_y.value*np.sin(w_x.value*t + np.pi/6*f.value)

fig = Figure(figsize=(GRAPH_SIZE, GRAPH_SIZE), dpi=100)
subplot = fig.add_subplot(111)
line, = subplot.plot(x, y, 'g-')

fig.supxlabel("x [m]", fontsize=FONT_SIZE)
fig.supylabel("y [m]", fontsize=FONT_SIZE)
fig.suptitle(f'Wykres toru', fontsize=FONT_SIZE)

set_up_canvas(fig)

potential_fig = Figure(figsize=(GRAPH_SIZE, GRAPH_SIZE), dpi=100)
potential_subplot = potential_fig.add_subplot(111, projection='3d')

plot_potential()
potential_fig.suptitle(f'Wykres potencjału', fontsize=FONT_SIZE)
set_up_canvas(potential_fig)

entry_frame.pack(side=tk.LEFT)

main_frame.pack(fill=tk.BOTH,expand=True)
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

