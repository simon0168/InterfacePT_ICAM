import matplotlib.pyplot as plt


x0 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36]
y0 = [0.3, 0.1, 0, 0.5, 0.6, 1, 1.8, 2, 2.2, 2.6, 2.7, 2.5, 2.1, 2, 1.6, 1.4, 1, 0.3, 0.5, -0.3, 0, -0.2, 0.9, 1.1,
         0.5, -0.8, -2.1, -2.3, -2.5, -2.3, -1.8, -1.5, 0, 0.3, 0.6, -0.3, 0]
y1 = [0.3, 0.1, 0, 0.5, 0.6, 1, 1.8, 2, 2.2, 2.6, 2.7, 2.5, 2.1, 2, 1.6, 1.4, 1, 0.3, 0.5, 0, 0, 0.2, 0.2, 0,
         0.1, 0.1, 0.1, 0.3, 0.5, 0.3, 0.8, 0.5, 0, 0.3, 0.6, 0.3, 0]

def proportionsValInterval(y, max, min):
    S = 0
    for elmts in y:
        if elmts >= min and elmts <= max :
            S += 1
    return S/len(y)


def Moy(y, delta, alpha): #delta c'est Max-min, alpha c'est le nombre de points qu'on cherche
    Max = max(y)
    Min = min(y)

    proportion = proportionsValInterval(y, Min + delta / 2, Min - delta / 2)

    moy = Min
    while moy < Max :
        moy += alpha

        if proportionsValInterval(y, moy+delta/2, moy-delta/2) > proportion :
            proportion = proportionsValInterval(y, moy+delta/2, moy-delta/2)
            Moy = moy

    return Moy


delta = 0.5
alpha = 0.01

Moy = Moy(y1,delta, alpha)

Max = Moy+delta/2
Min = Moy-delta/2


fig, ax = plt.subplots(figsize=(8, 3), dpi=100)
ax.axhline(Max, color='lightcoral')
ax.axhline(Min, color='lightcoral')
ax.axhline(Moy, color='red')
ax.plot(x0, y1)


plt.show()