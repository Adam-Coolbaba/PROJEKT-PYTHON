
import tkinter as tk
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import animation

import dynamics
from custom_widgets import EntryBox


def update_graphs():
    update_line()
    plot_potential()
    animate(0)
    update_animation()
    update_axis()
    fig.canvas.draw()
    potential_fig.canvas.draw()


def update_animation():
    xdata[:], ydata[:] = [], []
    anim_subplot.set_xlim(subplot.get_xlim())
    anim_subplot.set_ylim(subplot.get_ylim())


def update_line():
    global w_x, w_y, a_x, a_y, f
    line.set_ydata(a_y.value * np.sin(w_y.value * t + np.pi / 6 * f.value))
    line.set_xdata(a_x.value * np.sin(w_x.value * t))


def update_axis():
    subplot.set_aspect('equal', adjustable='datalim')
    subplot.relim()
    subplot.autoscale_view()
    print(subplot.get_ylim(), subplot.get_xlim())


def set_up_canvas(figure, parent ,side):
    c = FigureCanvasTkAgg(figure, master=parent)
    c.get_tk_widget().pack(side=side)
    c.draw()


def plot_potential():
    potential_subplot.cla()
    a = a_x.value if a_x.value > a_y.value else a_y.value
    x = np.arange(-a - .5, a + .5, 0.1)
    y = np.arange(-a - .5, a + .5, 0.1)
    x, y = np.meshgrid(x, y)
    z = dynamics.calc_potential_energy(a_x.value, w_x.value, x) + dynamics.calc_potential_energy(a_y.value, w_y.value, y)
    #potential_subplot.plot_surface(x, y, z)
    potential_subplot.pcolor(x,y,z)


def animate(i):
    x = a_x.value * np.sin(w_x.value * (0.01*i))
    y = a_y.value * np.sin(w_y.value * (0.01*i) + np.pi/6*f.value)
    point.set_data(x, y)
    return point,


def animate2(i):
    if i%10 == 0 :
        print(i)
    x = a_x.value * np.sin(w_x.value * (0.01*i))
    y = a_y.value * np.sin(w_y.value * (0.01*i) + np.pi/6*f.value)
    xdata.append(x)
    ydata.append(y)
    point2.set_data(x, y)
    anim_line.set_data(xdata, ydata)
    return point2,


def _quit():
    root.quit()
    root.destroy()


GRAPH_SIZE = 5
FONT_SIZE = 15

root = tk.Tk()
root.wm_title("Wykres drgan prostopadlych")
root.resizable(False, False)

main_frame = tk.Frame(master=root)
top_frame = tk.Frame(master=main_frame)
bot_frame = tk.Frame(master=main_frame)
entry_frame = tk.Frame(master=main_frame)

a_y = EntryBox(entry_frame, "A\u2082:", 1, update_graphs)
a_x = EntryBox(entry_frame, "A\u2081:", 1, update_graphs)
w_y = EntryBox(entry_frame, "\u03C9\u2082:", 1, update_graphs)
w_x = EntryBox(entry_frame, "\u03C9\u2081:", 1, update_graphs)
f = EntryBox(entry_frame, "\u0394\u03C6 (*\u03C0/6):", 3, update_graphs)

t = np.arange(0, 100, 0.01)
x = a_x.value*np.sin(w_y.value*t)
y = a_y.value*np.sin(w_x.value*t + np.pi/6*f.value)

fig = Figure(figsize=(GRAPH_SIZE, GRAPH_SIZE), dpi=100)
subplot = fig.add_subplot(111)
line, = subplot.plot(x, y, 'g-')
point, = subplot.plot(0, 0, 'o')

fig.supxlabel("x [m]", fontsize=FONT_SIZE)
fig.supylabel("y [m]", fontsize=FONT_SIZE)
fig.suptitle(f'Wykres toru', fontsize=FONT_SIZE)

set_up_canvas(fig,top_frame,tk.LEFT)

potential_fig = Figure(figsize=(GRAPH_SIZE, GRAPH_SIZE), dpi=100)
#potential_subplot = potential_fig.add_subplot(111, projection='3d')
potential_subplot = potential_fig.add_subplot(111)

plot_potential()
potential_fig.suptitle(f'Wykres potencjału', fontsize=FONT_SIZE)
set_up_canvas(potential_fig, top_frame, tk.LEFT)

entry_frame.pack(side=tk.RIGHT)

place_holder = tk.Label(text="Miejsce na tabele z danymi", master=bot_frame, width=70)
place_holder.pack(side=tk.RIGHT)

main_frame.pack(fill=tk.BOTH, expand=True)
top_frame.pack(side=tk.TOP)
bot_frame.pack(side=tk.BOTTOM)
button = tk.Button(master=root, text="Zamknij", command=_quit)
button.pack(side=tk.BOTTOM)

anim = animation.FuncAnimation(fig, animate, interval=10)

anim_fig = Figure(figsize=(GRAPH_SIZE, GRAPH_SIZE), dpi=100)
anim_subplot = anim_fig.add_subplot(111)
anim_subplot.set_xlim([-1.2, 1.2])
anim_subplot.set_ylim([-1.2, 1.2])
anim_line, = anim_subplot.plot([], [], lw = 2)
xdata, ydata = [], []
point2, = anim_subplot.plot(0, 0, 'o')
set_up_canvas(anim_fig, bot_frame, tk.LEFT)
anim2 = animation.FuncAnimation(anim_fig, animate2, interval=10)
anim_fig.supxlabel("x [m]", fontsize=FONT_SIZE)
anim_fig.supylabel("y [m]", fontsize=FONT_SIZE)
anim_fig.suptitle(f'Animacja', fontsize=FONT_SIZE)

fig.supxlabel("x [m]", fontsize=FONT_SIZE)
fig.supylabel("y [m]", fontsize=FONT_SIZE)
fig.suptitle(f'Wykres toru', fontsize=FONT_SIZE)

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

