import numpy as np
import matplotlib.pyplot as plt


def vida():
    def ponerCirc(y, x):
        c = [round(x, 1), round(y, 1)]
        cs.append(c)

    def show_shape():
        ax = plt.gca()
        for i in cs:
            tx = i[0]
            ty = i[1]
            c = plt.Circle(
                (tx, ty), radius=R, color='black', fill=False, linewidth=1.2)
            ax.add_patch(c)
        c = plt.Circle((0, 0), radius=3 * R, color='black', fill=False)
        ax.add_patch(c)
        plt.axis('scaled')
        plt.axis('off')
        plt.savefig("flor.png")

    def pintarlos(x, y, cont):
        cont += 1
        if (cont < 4):

            for i in range(6):
                x_ = round(x + R * np.cos(2.0 * np.pi * (1 + i) / 6.0), 1)
                y_ = round(y + R * np.sin(2.0 * np.pi * (1 + i) / 6.0), 1)
                if (not ([x_, y_] in cs)):
                    ponerCirc(x_, y_)
                    pintarlos(x_, y_, cont)

        elif ((cont >= 4) and (cont < 6)):

            for i in range(6):

                x_ = round(x + R * np.cos(2.0 * np.pi * (1 + i) / 6.0), 1)
                y_ = round(y + R * np.sin(2.0 * np.pi * (1 + i) / 6.0), 1)

                if (not ([x_, y_] in cs) and enOuter(x_, y_, 3.2)):
                    if (y_ > 0):
                        ponerCirc2(x_, y_, 0, 2 * np.pi)
                    else:
                        ponerCirc2(x_, y_, np.pi, -np.pi)

                elif (not ([x_, y_] in cs) and enOuter(x_, y_, 2.8)):
                    if (x_ > 0):
                        ponerCirc2(x_, y_, 0.5 * np.pi, 2.5 * np.pi)
                    else:
                        ponerCirc2(x_, y_, -np.pi / 2, 1.5 * np.pi)

                elif (not ([x_, y_] in cs) and enOuter(x_, y_, 2.2)):

                    if (y_ > 0):
                        ponerCirc2(x_, y_, 0, 2 * np.pi)
                    else:
                        ponerCirc2(x_, y_, np.pi, -np.pi)
                    pintarlos(x_, y_, cont)

    def ponerCirc2(y, x, mint, maxt):
        thetas = np.linspace(mint, maxt, 200)
        xs = R * np.cos(thetas) + x
        ys = R * np.sin(thetas) + y

        for i in cs:
            ind = np.where(enCirculo(xs, ys, i))[0]

            if (len(ind) > 0):

                plt.plot(xs[ind], ys[ind], color="black", linewidth=1.2)

    def enCirculo(x, y, c):
        return (x - c[0])**2 + (y - c[1])**2 <= R**2

    def enOuter(x, y, n):
        return (x)**2 + (y)**2 > (n * R)**2

    R = 100
    cs = []

    ponerCirc(0, 0)
    pintarlos(0, 0, 1)
    show_shape()
