import math
import tkinter as tk
from functools import partial
from tkinter import ttk

import numpy as np

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import animation

import dynamics
from custom_widgets import EntryBox, Table

GRAPH_SIZE = 4
FONT_SIZE = 10
INTERVAL = 30
IS_RUNNING = True


def update_graphs():
    update_line()
    plot_potential()
    update_axis(subplot)
    fig.canvas.draw()
    potential_fig.canvas.draw()
    update_animation()


def update_animation():
    global time_p
    xdata[:], ydata[:] = [], []
    anim_subplot.set_xlim(subplot.get_xlim())
    anim_subplot.set_ylim(subplot.get_ylim())
    update_axis(anim_subplot)
    time_p = time


def update_line():
    global w_x, w_y, A_x, A_y, f
    line.set_ydata(A_y.value * np.sin(w_y.value * t + np.pi / 6 * f.value))
    line.set_xdata(A_x.value * np.sin(w_x.value * t))


def update_axis(plot):
    plot.set_aspect('equal', adjustable='datalim')
    plot.relim()
    plot.autoscale_view()


def set_up_canvas(figure, parent, column, row):
    c = FigureCanvasTkAgg(figure, master=parent)
    c.get_tk_widget().grid(column=column, row=row)
    c.draw()


def plot_potential():
    potential_subplot.cla()
    a = A_x.value if A_x.value > A_y.value else A_y.value
    x = np.arange(-a - .5, a + .5, 0.1)
    y = np.arange(-a - .5, a + .5, 0.1)
    x, y = np.meshgrid(x, y)
    z = dynamics.calc_potential_energy(A_x.value, w_x.value, x) + dynamics.calc_potential_energy(A_y.value, w_y.value, y)
    potential_subplot.plot_surface(x, y, z)
    potential_subplot.set_xlabel("X [m]")
    potential_subplot.set_ylabel("Y [m]")
    potential_subplot.set_zlabel("E [J]")


def update_table(time):
    x = dynamics.calc_deviation(A_x.value, w_x.value, time, 0)
    y = dynamics.calc_deviation(A_y.value, w_y.value, time, f.value)
    v_x = dynamics.calc_osc_speed(time, w_x.value, A_x.value, 0)
    v_y = dynamics.calc_osc_speed(time, w_y.value, A_y.value, f.value)
    a_x = dynamics.calc_osc_acceleration_magnitude(time, w_x.value, A_x.value, 0)
    a_y = dynamics.calc_osc_acceleration_magnitude(time, w_y.value, A_y.value, f.value)
    a_t = abs(dynamics.calc_tangential_acceleration(v_x, v_y, a_x, a_y))
    a_n = abs(dynamics.calc_centripetal_acceleration(v_x, v_y, a_x, a_y))
    e_t = dynamics.calc_total_energy(1, w_x.value, A_x.value) + dynamics.calc_total_energy(1, w_y.value, A_y.value)
    e_k = dynamics.calc_kinetic_energy(1, (v_x ** 2 + v_y ** 2)**(1/2))
    e_p = dynamics.calc_potential_energy(1, w_x.value, x) + dynamics.calc_potential_energy(1, w_y.value, y)
    k = dynamics.calc_curvature(v_x,v_y,a_x,a_y)
    list = [x, y, (v_x ** 2 + v_y ** 2) ** (1 / 2), (a_x ** 2 + a_y ** 2) ** (1 / 2), a_t, a_n, e_t,  e_k, e_p, k]
    table.update(list)


def animate(i):
    global time, xdata, ydata, time_p
    time = (0.01 * i)
    if time - time_p > np.pi*2/np.gcd(int(w_x.value*100), int(w_y.value*100))*100:
        xdata.clear()
        ydata.clear()
        time_p = time
    x = dynamics.calc_deviation(A_x.value, w_x.value, time, 0)
    y = dynamics.calc_deviation(A_y.value, w_y.value, time, f.value)
    xdata.append(x)
    ydata.append(y)
    point.set_data(x, y)
    anim_line.set_data(xdata, ydata)
    update_table(time)
    return point,


def _quit():
    root.quit()
    root.destroy()


def change_running():
    global IS_RUNNING
    if IS_RUNNING:
        anim2.pause()
        stop_button.config(text='\u23f5')
    else:
        anim2.resume()
        stop_button.config(text='\u23f8')
    IS_RUNNING = not IS_RUNNING


def change_speed(a):
    anim2._interval = INTERVAL / a


def gcd(x, y):
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x
    return x


root = tk.Tk()
root.wm_title("Wykres drgan prostopadlych")
root.resizable(False, False)

main_frame = tk.Frame(master=root)
graphs_frame = tk.Frame(master=main_frame)
entry_frame = tk.Frame(master=main_frame)
animation_frame = tk.Frame(master=graphs_frame)
time_p = 0
A_y = EntryBox(entry_frame, "A\u2082:", 1, update_graphs)
A_x = EntryBox(entry_frame, "A\u2081:", 1, update_graphs)
w_y = EntryBox(entry_frame, "\u03C9\u2082:", 1, update_graphs)
w_x = EntryBox(entry_frame, "\u03C9\u2081:", 1, update_graphs)
f = EntryBox(entry_frame, "\u0394\u03C6 (*\u03C0/6):", 3, update_graphs)

t = np.arange(0, 100, 0.01)
x = A_x.value * np.sin(w_y.value * t)
y = A_y.value * np.sin(w_x.value * t + np.pi / 6 * f.value)

fig = Figure(figsize=(GRAPH_SIZE, GRAPH_SIZE), dpi=100)
subplot = fig.add_subplot(111)
line, = subplot.plot(x, y, 'g-')

fig.supxlabel("x [m]", fontsize=FONT_SIZE)
fig.supylabel("y [m]", fontsize=FONT_SIZE)
fig.suptitle(f'Wykres toru', fontsize=FONT_SIZE)

set_up_canvas(fig,graphs_frame, 1, 1)

potential_fig = Figure(figsize=(GRAPH_SIZE, GRAPH_SIZE), dpi=100)
potential_subplot = potential_fig.add_subplot(111, projection='3d')

plot_potential()
potential_fig.suptitle(f'Wykres potencjału', fontsize=FONT_SIZE)
set_up_canvas(potential_fig, graphs_frame, 2, 1)

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

table = Table(graphs_frame, lst)
table.table_frame.grid(column=2, row=2)
main_frame.pack(fill=tk.BOTH, expand=True)
button = ttk.Button(master=root, text="Zamknij", command=_quit)
speed_frame = tk.Frame(master=animation_frame)
animation_frame.grid(row=2,column=1)
#
stop_button = ttk.Button(master=speed_frame, text="\u23f8", command=change_running, width=3)
stop_button.pack(side=tk.LEFT)
for i in range(5):
    speed = 2**i*0.25
    speed_button_025 = ttk.Button(master=speed_frame, text=f"x{speed}", command=partial(change_speed, speed))
    speed_button_025.pack(side=tk.LEFT)

speed_frame.pack(side=tk.BOTTOM)
button.pack(side=tk.BOTTOM)


anim_fig = Figure(figsize=(GRAPH_SIZE, GRAPH_SIZE), dpi=100)
anim_subplot = anim_fig.add_subplot(111)
anim_subplot.set_xlim([-1.2, 1.2])
anim_subplot.set_ylim([-1.2, 1.2])
anim_line, = anim_subplot.plot([], [], lw=2)
xdata, ydata = [], []
point, = anim_subplot.plot(0, 0, 'o')
c = FigureCanvasTkAgg(anim_fig, master=animation_frame)
c.get_tk_widget().pack()
c.draw()

time_p = 0
time = 0

anim_fig.supxlabel("x [m]", fontsize=FONT_SIZE)
anim_fig.supylabel("y [m]", fontsize=FONT_SIZE)
anim_fig.suptitle(f'Animacja', fontsize=FONT_SIZE)

fig.supxlabel("x [m]", fontsize=FONT_SIZE)
fig.supylabel("y [m]", fontsize=FONT_SIZE)
fig.suptitle(f'Wykres toru', fontsize=FONT_SIZE)

graphs_frame.pack(side=tk.LEFT)
entry_frame.pack(side=tk.LEFT)
fig.tight_layout()
potential_fig.tight_layout()
anim_fig.tight_layout()

anim2 = animation.FuncAnimation(anim_fig, animate, interval=INTERVAL)
tk.mainloop()



