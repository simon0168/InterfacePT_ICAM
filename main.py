import tkinter as tk
import ttkbootstrap as ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.widgets import Slider
import numpy as np
import matplotlib.patheffects as path_effects
import webbrowser
import time

def Moy_sum_abs(y):
    S=0

    for elmts in y:
        S += abs(elmts)
    S = S/len(y)

    format_S = "{:.2f}".format(S)

    return format_S
def create_graph(liste_x,liste_y):

    x = liste_x[0]
    y = liste_y[0]
    x1 = liste_x[1]
    y1 = liste_y[1]
    x2 = liste_x[2]
    y2 = liste_y[2]


    plt.rcParams.update({
        "figure.facecolor": (0.0, 0.0, 0.0, 0.0),  # red   with alpha = 0%
        "axes.facecolor": (1.0, 1.0, 1.0, 0.0),  # green with alpha = 0%
        "savefig.facecolor": (0.0, 0.0, 0.0, 0.2),  # blue  with alpha = 0%
    })

    # Création de la figure Matplotlib
    fig, ax = plt.subplots(figsize=(8, 3), dpi=100)
    plt.subplots_adjust(bottom=0.25)
    plt.subplots_adjust(right=0.8)

    # Définir l'échelle des y entre -10 et 10
    ax.set_ylim(-6, 6)

    # Changer la couleur des axes x et y
    ax.spines['bottom'].set_color('gray')  # Axe x
    ax.spines['top'].set_color('gray')  # Axe x
    ax.spines['left'].set_color('gray')  # Axe y
    ax.spines['right'].set_color('gray')  # Axe y
    # Changer la couleur des valeurs des axes x et y en blanc
    ax.tick_params(axis='x', colors='gray')
    ax.tick_params(axis='y', colors='gray')

    # Afficher le cadrillage sur le graphique
    ax.grid(color='grey')

    # Ajouter une ligne rouge au niveau de y=0
    ax.axhline(0, color='lightcoral')

    # Tracer la courbe
    ax.plot(x, y, color='white')
    ax.plot(x1, y1, color='white', alpha=0.5, linewidth=1.5)
    ax.plot(x2, y2, color='white', alpha=0.2,linewidth=1)

    # Ajouter une légende à droite du graphique
    ax.legend([f'zero (0)',f'n ({Moy_sum_abs(y)})', f'n-1 ({Moy_sum_abs(y1)})', f'n-2 ({Moy_sum_abs(y2)})'], loc='upper center', bbox_to_anchor=(1.12, 0.85), frameon=False)

    initial_x = 0

    # Creation de l'axe verticale
    vline = ax.axvline(initial_x, color='lightcoral', linestyle='--')

    # Creation des textes
    text = ax.text(0, 0, '', ha='right', va='center', color='white')

    # Créer un effet de contour extérieur
    contour_exterieur = path_effects.Stroke(linewidth=3, foreground='#002b36')

    # Créer un effet de contour intérieur
    contour_interieur = path_effects.Stroke(linewidth=0, foreground='white')

    # Appliquer les effets de contour au texte
    text.set_path_effects([contour_exterieur, contour_interieur])
    ax.text(30, 6.5, f'MoySumAbs: {Moy_sum_abs(y)}', fontsize=12, ha='center', color='white')

    def update_x(val):
        vline.set_xdata([slider_x.val])
        x_vline = vline.get_xdata()[0]
        y_interp = np.interp(x_vline, x, y)
        text.set_position((x_vline - 1, y_interp))
        text.set_text(f'{y_interp:.2f}')
        fig.canvas.draw_idle()

    ax_slider_x = plt.axes([0.2, 0.1, 0.5, 0.03])
    slider_x = Slider(ax_slider_x, '', 0, 35, valinit=initial_x, initcolor='blue', track_color='grey')
    slider_x.valtext.set_color('white')
    slider_x.on_changed(update_x)

    def update_slider():
        update_x(slider_x.val)
        window.after(50000, update_slider)  # Appel récursif après 100 millisecondes

    # Appel initial de la fonction de mise à jour du slider
    update_slider()

    return fig

def button3():
    val = entry1.get()
    print(val)

# Fonction appelée lorsque la sélection du menu déroulant change


def testCom():
    selectedCom = dropdown.get()
    selectedBaude = int(dropdown1.get())


    # Mettre à jour le texte en fonction du résultat
    if selectedCom == 'COM3' and selectedBaude == 9600:
        text0.config(text='True', foreground='green')
    else:
        text0.config(text='False', foreground='red')



def ouvrir_pdf():
    # Chemin vers le fichier PDF
    chemin_pdf = "notice.pdf"

    # Ouvre le fichier PDF dans le navigateur par défaut
    webbrowser.open(chemin_pdf)

# Definition des valeurs
x2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36]
y2 = [0.3, 0.1, 0, 0.5, 0.6, 1.2, 2, 2.1, 2.9, 3, 3.6, 4, 3.2, 2.4, 2.2, 2, 1, 0.3, 0.5, -0.3, 0, -0.2, 0.9, 1.1,
         0.5, -1, -3, -3.2, -3.3, -4, -4.1, -3, 0, 0.3, 0.6, -0.3, 0]
x1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36]
y1 = [0.3, 0.1, 0, 0.5, 0.6, 1, 1.8, 2, 2.2, 2.6, 3, 3.5, 2.1, 2, 1.6, 1.4, 1, 0.3, 0.5, -0.3, 0, -0.2, 0.9, 1.1,
         0.5, -1, -3, -3.2, -3.3, -4, -4.1, -3, 0, 0.3, 0.6, -0.3, 0]
x0 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36]
y0 = [0.3, 0.1, 0, 0.5, 0.6, 1, 1.8, 2, 2.2, 2.6, 2.7, 2.5, 2.1, 2, 1.6, 1.4, 1, 0.3, 0.5, -0.3, 0, -0.2, 0.9, 1.1,
         0.5, -0.8, -2.1, -2.3, -2.5, -2.3, -1.8, -1.5, 0, 0.3, 0.6, -0.3, 0]


liste_x = [x0, x1, x2]
liste_y = [y0, y1, y2]

# Creation de la main window
window = ttk.Window(themename='solar')
window.title('Demo')
window.geometry('1000x700')

title_label = ttk.Label(master=window, text='Dévoilage de roue', font='Calibri 24 bold')
title_label.pack(pady=10)


# Creations des frames
topFrame = ttk.Frame(window)
mainFrame = ttk.Frame(window)
leftFrame = ttk.Frame(mainFrame, width=200, height=700,borderwidth=20)
rightFrame = ttk.Frame(mainFrame, width=800, height=700,borderwidth=20)
topFrame.pack(pady=10)
mainFrame.pack(pady=10)
leftFrame.pack(side='left', padx=10, pady=10, fill=tk.Y)
rightFrame.pack(side='left', padx=10, pady=10, expand=True, fill=tk.BOTH)

# Créer le widget de menu déroulant
button0 = ttk.Button(topFrame, text='Tester la connexion', command=testCom)
button0.pack(pady=10,padx=10, side='left')
text0 = ttk.Label(master=topFrame, text='False', foreground='grey')
text0.pack(pady=10, padx=10, side='left')
dropdown = ttk.Combobox(topFrame)
dropdown['values'] = ('COM1', 'COM2', 'COM3','COM4', 'COM5', 'COM6','COM7', 'COM8', 'COM9')  # Valeurs du menu déroulant
dropdown.set('COM')  # Option par défaut affichée
dropdown.bind('<<ComboboxSelected>>')  # Lier la fonction on_select à l'événement de sélection
dropdown.pack(pady=10,padx=10, side='left')

dropdown1 = ttk.Combobox(topFrame)
dropdown1['values'] = (9600, 10000)  # Valeurs du menu déroulant
dropdown1.set('Baude')  # Option par défaut affichée
dropdown1.bind('<<ComboboxSelected>>')  # Lier la fonction on_select à l'événement de sélection
dropdown1.pack(pady=10,padx=10, side='left')


# Ajouter les boutons dans la colonne de droite
button1 = ttk.Button(leftFrame, text='Faire un tour')
button1.pack(pady=(100,10))
text1 = ttk.Label(master=leftFrame, text='Coordonnées angulaires', foreground='grey')
text1.pack(pady=(35,2))
entry1 = ttk.Entry(master=leftFrame)
entry1.pack(pady=(2,10))
button3 = ttk.Button(leftFrame, text='Aller à la position', command=button3)
button3.pack(pady=10)
button4 = ttk.Button(leftFrame, text='Voir la notice', command=ouvrir_pdf)
button4.pack(pady=(200,10))



# Création du canevas Tkinter pour afficher la figure
fig = create_graph(liste_x,liste_y)
canvas = FigureCanvasTkAgg(fig, master=rightFrame)
canvas.draw()
canvas.get_tk_widget().pack(padx=10, pady=10)

text2 = ttk.Label(master=rightFrame, text='Coordonnées angulaires: 32', foreground='grey')
text2.pack(pady=(2,2))
text3 = ttk.Label(master=rightFrame, text='Vitesse max: 140', foreground='grey')
text3.pack(pady=(2,2))
text4 = ttk.Label(master=rightFrame, text='Moteur: EU-32', foreground='grey')
text4.pack(pady=(2,2))




window.mainloop()