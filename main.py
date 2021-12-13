import tkinter

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure




def update_graph(event):
    #Do usuniecia potem, ale narazie sie przydaje
    if str(event.key) == 'q':
        _quit()
    #----------
    update_line(event.key)
    set_up_figure()
    mpl.backend_bases.key_press_handler(event, canvas)


def update_line(key):
    # TODO: zminic try na if? albo ulepszyc wyrazenie pod try:
    global w_y
    try:
        w_y = int(key)
        line.set_ydata(np.sin(w_y * t))
    except ValueError:
        w_y = 1
        line.set_ydata(np.sin(w_y * t))


def set_up_figure():
    fig.supxlabel("x [m]", fontsize=FONT_SIZE)
    fig.supylabel("y [m]", fontsize=FONT_SIZE)
    fig.suptitle(f'Wykres dla: \u03C9\u2081 = {w_x}, \u03C9\u2082 = {w_y}', fontsize=FONT_SIZE)
    fig.canvas.draw()


def set_up_canvas():
    global canvas
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    canvas.mpl_connect("key_press_event", update_graph)


def _quit():
    root.quit()
    root.destroy()


GRAPH_SIZE = 6
FONT_SIZE = 15
root = tkinter.Tk()
root.wm_title("Wykres drgan prostopadlych")

w_x = 2
w_y = 2
a_x = 1
a_y = 1
f = np.pi/2

t = np.arange(0, 10, 0.01)
x = a_x*np.sin(w_x*t)
y = a_y*np.sin(w_y*t + f)

fig = Figure(figsize=(GRAPH_SIZE, GRAPH_SIZE), dpi=100)
subplot = fig.add_subplot(111)
line, = subplot.plot(x, y, 'g-')
canvas = FigureCanvasTkAgg(fig, master=root)

set_up_figure()
set_up_canvas()

button = tkinter.Button(master=root, text="Zamknij", command=_quit)
button.pack(side=tkinter.BOTTOM)

tkinter.mainloop()



#Propozycja jak będziemy mieli za dużo czasu:
def Td():
    ax = plt.axes(projection = '3d')

    t= np.arange(0,10,0.01)
    x = np.sin(2*t)
    y = np.sin(4*t)
    z = np.sin(6*t)

    ax.plot3D(x,y,z,'g-')
    plt.show()

#Td()

