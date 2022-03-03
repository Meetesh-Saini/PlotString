import matplotlib.pyplot as plt
import numpy as np
import warnings

xindex = 0
xaxis = 0
yaxis = 0
fontsize = 0
abc = {}
curves = []
initialized = False

# abc = {"A": [[1, 2, 3, 2.5, 1.5], [1, 2, 1, 1.5, 1.5]], "B": [[1, 1], [1, 2]], "D": [[1, 1], [1, 2]], "E": [[1, 1, 3, 1, 1, 3, 1, 1, 3], [1, 2, 2, 2, 1.5, 1.5, 1.5, 1, 1]], "F": [[1, 1, 3, 1, 1, 3, 1], [1, 2, 2, 2, 1.5, 1.5, 1.5]], "G": [[3, 3, 2], [1, 1.5, 1.5]], "H": [[1, 1, 1, 3, 3, 3], [1, 2, 1.5, 1.5, 2, 1]], "I": [[1, 3, 2, 2, 1, 3], [1, 1, 1, 2, 2, 2]], "J": [[1, 3, 2, 2], [2, 2, 2, 1.25]], "K": [[1, 1, 1, 3, 1, 3], [1, 2, 1.5, 2, 1.5, 1]],
#        "L": [[1, 1, 1, 3], [1, 2, 1, 1]], "M": [[1, 1, 2, 3, 3], [1, 2, 1.5, 2, 1]], "N": [[1, 1, 3, 3], [1, 2, 1, 2]], "P": [[1, 1], [1, 2]], "Q": [[2, 3], [1.25, 1]], "R": [[1, 1, 1, 3], [1, 2, 1.5, 1]], "T": [[2, 2, 1, 3], [1, 2, 2, 2]], "U": [[1, 1], [1.5, 2]], "V": [[1, 2, 3], [2, 1, 2]], "W": [[1, 1.5, 2, 2+0.5, 3], [2, 1, 1.5, 1, 2]], "X": [[1, 3, 2, 1, 3], [1, 2, 1.5, 2, 1]], "Y": [[2, 2, 1, 2, 3], [1, 1.5, 2, 1.5, 2]], "Z": [[1, 3, 1, 3], [2, 2, 1, 1]]}

def init(margin=(1,1)):
    global abc, curves, xaxis, yaxis, initialized
    xaxis, yaxis = margin
    abc = {"A": [[xaxis, xaxis+1, xaxis+2, xaxis+1.5, xaxis+0.5], [yaxis, yaxis+1, yaxis, yaxis+0.5, yaxis+0.5]], "B": [[xaxis, xaxis], [yaxis, yaxis+1]], "D": [[xaxis, xaxis], [yaxis, yaxis+1]], "E": [[xaxis, xaxis, xaxis+2, xaxis, xaxis, xaxis+2, xaxis, xaxis, xaxis+2], [yaxis, yaxis+1, yaxis+1, yaxis+1, yaxis+0.5, yaxis+0.5, yaxis+0.5, yaxis, yaxis]], "F": [[xaxis, xaxis, xaxis+2, xaxis, xaxis, xaxis+2, xaxis], [yaxis, yaxis+1, yaxis+1, yaxis+1, yaxis+0.5, yaxis+0.5, yaxis+0.5]], "G": [[xaxis+2, xaxis+2, xaxis+1], [yaxis, yaxis+0.5, yaxis+0.5]], "H": [[xaxis, xaxis, xaxis, xaxis+2, xaxis+2, xaxis+2], [yaxis, yaxis+1, yaxis+0.5, yaxis+0.5, yaxis+1, yaxis]], "I": [[xaxis, xaxis+2, xaxis+1, xaxis+1, xaxis, xaxis+2], [yaxis, yaxis, yaxis, yaxis+1, yaxis+1, yaxis+1]], "J": [[xaxis, xaxis+2, xaxis+1, xaxis+1], [yaxis+1, yaxis+1, yaxis+1, yaxis+0.25]], "K": [[xaxis, xaxis, xaxis, xaxis+2, xaxis, xaxis+2], [yaxis, yaxis+1, yaxis+0.5, yaxis+1, yaxis+0.5, yaxis]],
       "L": [[xaxis, xaxis, xaxis, xaxis+2], [yaxis, yaxis+1, yaxis, yaxis]], "M": [[xaxis, xaxis, xaxis+1, xaxis+2, xaxis+2], [yaxis, yaxis+1, yaxis+0.5, yaxis+1, yaxis]], "N": [[xaxis, xaxis, xaxis+2, xaxis+2], [yaxis, yaxis+1, yaxis, yaxis+1]], "P": [[xaxis, xaxis], [yaxis, yaxis+1]], "Q": [[xaxis+1, xaxis+2], [yaxis+0.25, yaxis]], "R": [[xaxis, xaxis, xaxis, xaxis+2], [yaxis, yaxis+1, yaxis+0.5, yaxis]], "T": [[xaxis+1, xaxis+1, xaxis, xaxis+2], [yaxis, yaxis+1, yaxis+1, yaxis+1]], "U": [[xaxis, xaxis], [yaxis+0.5, yaxis+1]], "V": [[xaxis, xaxis+1, xaxis+2], [yaxis+1, yaxis, yaxis+1]], "W": [[xaxis, xaxis+0.5, xaxis+1, xaxis+1+0.5, xaxis+2], [yaxis+1, yaxis, yaxis+0.5, yaxis, yaxis+1]], "X": [[xaxis, xaxis+2, xaxis+1, xaxis, xaxis+2], [yaxis, yaxis+1, yaxis+0.5, yaxis+1, yaxis]], "Y": [[xaxis+1, xaxis+1, xaxis, xaxis+1, xaxis+2], [yaxis, yaxis+0.5, yaxis+1, yaxis+0.5, yaxis+1]], "Z": [[xaxis, xaxis+2, xaxis, xaxis+2], [yaxis+1, yaxis+1, yaxis, yaxis]]}

    curves = ["B", "C", "D", "G", "J", "O", "P", "Q", "R", "S", "U", " "]
    initialized = True


def write(text):
    if initialized:
        global xindex
        for i in text.upper():
            if i not in curves:
                plt.plot(np.array(abc[i][0])+xindex, abc[i][1])
            else:
                if i == "B": # no   diff
                    extend_x = xindex+xaxis
                    extend_y_upper = yaxis+0.75
                    extend_y_lower = yaxis+0.25
                    base_plot = plt.plot(np.array(abc[i][0])+xindex, abc[i][1])
                    s = np.linspace(0, 2)
                    c = np.sqrt((0.25**2-(s/8)**2))
                    plt.plot(s+extend_x, c+extend_y_upper, color=base_plot[0].get_color())
                    plt.plot(s+extend_x, -c+extend_y_upper, color=base_plot[0].get_color())
                    plt.plot(s+extend_x, c+extend_y_lower, color=base_plot[0].get_color())
                    plt.plot(s+extend_x, -c+extend_y_lower, color=base_plot[0].get_color())

                elif i == "C": # yes
                    extend_x = xindex+xaxis+2
                    extend_y = yaxis+0.5
                    s = np.linspace(0, 2)
                    c = np.sqrt((0.5**2-(s/4)**2))
                    base_plot = plt.plot(-s+extend_x, c+extend_y)
                    plt.plot(-s+extend_x, -c+extend_y, color=base_plot[0].get_color())

                elif i == "D": # no
                    extend_x = xindex+xaxis
                    extend_y = yaxis+0.5
                    base_plot = plt.plot(np.array(abc[i][0])+xindex, abc[i][1])
                    s = np.linspace(0, 2)
                    c = np.sqrt((0.5**2-(s/4)**2))
                    plt.plot(s+extend_x, c+extend_y, color=base_plot[0].get_color())
                    plt.plot(s+extend_x, -c+extend_y, color=base_plot[0].get_color())

                elif i == "G": # no
                    extend_x = xindex+xaxis+2
                    extend_y = yaxis+0.5
                    base_plot = plt.plot(np.array(abc[i][0])+xindex, abc[i][1])
                    s = np.linspace(0, 2)
                    c = np.sqrt((0.5**2-(s/4)**2))
                    plt.plot(-s+extend_x, c+extend_y, color=base_plot[0].get_color())
                    plt.plot(-s+extend_x, -c+extend_y, color=base_plot[0].get_color())

                elif i == "J": # no
                    extend_x = xindex+xaxis+0.5
                    extend_y = yaxis+0.25
                    base_plot = plt.plot(np.array(abc[i][0])+xindex, abc[i][1])
                    s = np.linspace(0, 0.5)
                    c = np.sqrt((0.25**2-(s/2)**2))
                    plt.plot(s+extend_x, -c+extend_y, color=base_plot[0].get_color())
                    plt.plot(-s+extend_x, -c+extend_y,
                             color=base_plot[0].get_color())

                elif i == "O": # yes
                    extend_x = xindex+xaxis+1
                    extend_y = yaxis+0.5
                    s = np.linspace(0, 1)
                    c = np.sqrt((0.5**2-(s/2)**2))
                    base_plot = plt.plot(-s+extend_x, c+extend_y)
                    plt.plot(-s+extend_x, -c+extend_y, color=base_plot[0].get_color())
                    plt.plot(s+extend_x, c+extend_y, color=base_plot[0].get_color())
                    plt.plot(s+extend_x, -c+extend_y, color=base_plot[0].get_color())

                elif i == "P": # no
                    extend_x = xindex+xaxis
                    extend_y = yaxis+0.75
                    base_plot = plt.plot(np.array(abc[i][0])+xindex, abc[i][1])
                    s = np.linspace(0, 2)
                    c = np.sqrt((0.25**2-(s/8)**2))
                    plt.plot(s+extend_x, c+extend_y, color=base_plot[0].get_color())
                    plt.plot(s+extend_x, -c+extend_y, color=base_plot[0].get_color())

                elif i == "Q": # no
                    extend_x = xindex+xaxis+1
                    extend_y = yaxis+0.5
                    base_plot = plt.plot(np.array(abc[i][0])+xindex, abc[i][1])
                    s = np.linspace(0, 1)
                    c = np.sqrt((0.5**2-(s/2)**2))
                    plt.plot(-s+extend_x, c+extend_y, color=base_plot[0].get_color())
                    plt.plot(-s+extend_x, -c+extend_y, color=base_plot[0].get_color())
                    plt.plot(s+extend_x, c+extend_y, color=base_plot[0].get_color())
                    plt.plot(s+extend_x, -c+extend_y, color=base_plot[0].get_color())

                elif i == "R": # no
                    extend_x = xindex+xaxis
                    extend_y = yaxis+0.75
                    base_plot = plt.plot(np.array(abc[i][0])+xindex, abc[i][1])
                    s = np.linspace(0, 2)
                    c = np.sqrt((0.25**2-(s/8)**2))
                    plt.plot(s+extend_x, c+extend_y, color=base_plot[0].get_color())
                    plt.plot(s+extend_x, -c+extend_y, color=base_plot[0].get_color())

                elif i == "S": # yes   diff
                    extend_x_full = xindex+xaxis+2
                    extend_x_half = xindex+xaxis
                    extend_y_upper = yaxis+0.75
                    extend_y_lower = yaxis+0.25
                    s = np.linspace(0, 2)
                    c = np.sqrt((0.25**2-(s/8)**2))
                    base_plot = plt.plot(-s+extend_x_full, c+extend_y_upper)
                    s = np.linspace(1, 2)
                    plt.plot(-s+extend_x_full, -c+extend_y_upper,
                             color=base_plot[0].get_color())
                    plt.plot(s+extend_x_half, c+extend_y_lower,
                             color=base_plot[0].get_color())
                    s = np.linspace(0, 2)
                    plt.plot(s+extend_x_half, -c+extend_y_lower,
                             color=base_plot[0].get_color())

                elif i == "U": # no
                    extend_x = xindex+xaxis+1
                    extend_y = yaxis+0.5
                    base_plot = plt.plot(np.array(abc[i][0])+xindex, abc[i][1])
                    s = np.linspace(0, 1)
                    c = np.sqrt((0.5**2-(s/2)**2))
                    plt.plot(s+extend_x, -c+extend_y, color=base_plot[0].get_color())
                    plt.plot(-s+extend_x, -c+extend_y, color=base_plot[0].get_color())
                    plt.plot(np.array(abc[i][0])+xindex+2, abc[i]
                             [1], color=base_plot[0].get_color())
            if i in abc or curves:
                xindex += 3
    else:
        warnings.warn("It is recommended to initialize plotstring first to pass necessary parameters.",RuntimeWarning,1,None)
        init()
        write(text)


def show(setOrigin=False):
    xmin, xmax, ymin, ymax = plt.axis()
    if xmax/3 > 2:
        if setOrigin:
            plt.axis([0, xmax, 0, xmax/3])
        else:
            plt.axis([xmin, xmax, ymin, xmax/3])
            print(xmin,ymin)
    plt.show()

def help():
    help_data = {1:("init","\nParameters:\n\tmargin:Tuple (optional)\n\nSyntax: init(margin=(x,y))\nIt passes all required parameters for the plot to work correctly. It is recommended to use it first and then use other methods.\n\nmargin=(x,y)\nx = shift on X-axis\ny = shift on Y-axis\n"), 
                 2:("write","\nParameters:\n\ttext:string\n\nSyntax: write(text='passed text')\nIt will plot the whole text in uppercase.\n\ntext='passed text'\npassed text = The text you want to plot\n"),
                 3:("show","\nParameters:\n\tsetOrigin:bool (optional)\n\nSyntax: show(setOrigin=False)\nIt will show to plot plotted by 'write' function.\n\nsetOrigin=True will set the minimum limit of X-axis and Y-axis to 0. Its default value is False\n")}
    while True:
        options = '\n'.join([f"{i}. {help_data[i][0]}" for i in help_data])
        print(options)
        print(f"{max(help_data.keys())+1}. q")
        command = input("\n>")
        if command=="q":
            break
        else:
            if command in map(str,help_data.keys()):
                print(help_data[int(command)][1])
            else:
                print("\nInvalid command\n")