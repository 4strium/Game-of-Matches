# Auteur : Romain MELLAZA
# Date : 01/04/2022
# Description : Programme qui permet à l'utilisateur de jouer (via une interface graphique TKinter) au jeu des allumettes.
# Comme demandé, quatres modes sont disponibles : Joueur contre Joueur, Joueur contre Ordinateur (en aléatoire), Joueur contre Ordinateur (en algorithme) et ordinateur contre ordinateur (en aléatoire)
# Pour voir les règles du jeu cliquez sur le bouton correspondant dans l'accueil
# 

# J'importe les modules indispensables au bon fonctionnement de mon programme :
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from random import randint

# Je défini ma fenêtre parent que j'appellerai "root" (ce sera mon accueil) :
root = Tk()

# Je défini des paramètres à cette fenêtre :
root.title("Le Jeu des 21 allumettes par Romain MELLAZA")       # Un titre
root.geometry("1080x720")                                       # Un resolution d'affichage, ici HD
root.minsize(1080, 720)                                         # Je bloque cette resolution, pour éviter que l'utilisateur ne redimmensionne n'importe comment.
root.maxsize(1080, 720)
root.iconbitmap(default='icon\LOGO_v1.ico')                          # Je défini un logo pour la fenêtre


# Je défini des variables essentielles avec leurs valeurs par défaut :
nb_allumettes = 21                                              # Le nombre d'alumettes initialement sur la table
count_x = 0                                                     # Variable pour compter le rang des images d'alummettes en fonction du nombre à supprimer (voir fctn "suppr_allum")
allum_list=[]                                                   # Liste qui contiendra toutes les images d'allumettes
count_player = 2                                                # Compteur qui permet au programme de savoir à quel joueur (ou robot) c'est le tour de jouer !
count_window_open = 0                                           # Compteur qui permet au programme de savoir combien de fenêtre de jeu l'utilisateur à ouvert !
count_window_regles = 0                                         # Compteur qui permet au programme de savoir combien de fenêtre de règles l'utilisateur à ouvert !

# J'importe et affiche une image de fond pour mon accueil:
bg = PhotoImage(file = "img\Background_IMAGE.png")
canvas_accueil = Canvas( root, width = 1080, height = 720)
canvas_accueil.pack(fill = "both", expand = True)
canvas_accueil.create_image( 0, 0, image = bg, anchor = "nw")

# Ajouter un titre à mon accueil :
# Je crée un texte blanc à qui j'ajoute un surlignement bleu derrière
i=canvas_accueil.create_text(540.45, 137, text='Bienvenue dans le super jeu des allumettes !', font=("Helvetica", 40), fill="white")
r=canvas_accueil.create_rectangle(canvas_accueil.bbox(i),fill="#00bdfb")                                                              
canvas_accueil.tag_lower(r,i)

# Ajouter un sous-titre à mon accueil :
# Je crée un texte blanc à qui j'ajoute un surlignement bleu derrière
k=canvas_accueil.create_text(540.45, 310, text='Veuillez selectionner un mode de jeu :', font=("Helvetica", 30), fill="white")
l=canvas_accueil.create_rectangle(canvas_accueil.bbox(k),fill="#00bdfb")
canvas_accueil.tag_lower(l,k)






##############################################################################################################################################################################################################
#                                                                                     ACCUEIL                                                                                                                #
#                                                                                                                                                                                                            #

# Définition d'une fonction qui créer les boutons pour prendre des allumettes:
def crea_button(racine,canvas):
    '''
    Fonction qui reçoit la fenêtre ("racine") ainsi que la toile ("canvas") où elle doit implanter des boutons pour choisir le nombre d'allumette que l'utilisateur prends.

    Chaque pression sur un bouton appelle ensuite une fonction de supression d'allumettes en rapport.

    Elle renvoie les caractéristiques et l'emplacement des boutons sur la toile.
    '''
    v=canvas.create_text(540, 525, text="Combien d'allumette(s) prenez-vous ?",font=("Helvetica", 30), fill="white")
    w=canvas.create_rectangle(canvas.bbox(v),fill="#00bdfb")
    canvas.tag_lower(w,v)
    button1 = Button(racine, text="1 allumette", command=lambda *args: suppr_allum(1, canvas, racine), font=("Helvetica", 14), fg='white', bg="#00bdfb", height = 2, width = 18)
    button1_window = canvas.create_window(75, 560, anchor='nw', window=button1)
    button2 = Button(racine, text="2 allumettes", command=lambda *args: suppr_allum(2, canvas, racine), font=("Helvetica", 14), fg='white', bg="#00bdfb", height = 2, width = 18)
    button2_window = canvas.create_window(430, 560, anchor='nw', window=button2)
    button3 = Button(racine, text="3 allumettes", command=lambda *args: suppr_allum(3, canvas, racine), font=("Helvetica", 14), fg='white', bg="#00bdfb", height = 2, width = 18)
    button3_window = canvas.create_window(780, 560, anchor='nw', window=button3)
    return button1_window, button2_window, button3_window


# Définition d'une fonction qui ouvre la fenêtre des régles du jeu:
def open_regles():
    '''
    Procédure qui ouvre la fenêtre des règles seulement si celle-ci n'est pas déjà ouverte.

    Les règles sont importées et affichées directement sur une nouvelle toile dans une nouvelle fenêtre.

    En revanche si elle est déjà ouverte alors un message d'erreur est affiché sur l'écran de l'utilisateur.
    '''
    global count_window_regles
    if count_window_regles == 0 :
        root_regles = Toplevel(root)
        root_regles.title("Les règles du Jeu des allumettes")
        root_regles.geometry("1080x720")
        root_regles.minsize(1080, 720)
        root_regles.maxsize(1080, 720)
        count_window_regles+=1
        # Importer et afficher une image de fond :
        canvas_regles = Canvas(root_regles, width = 1080, height = 720)
        canvas_regles.pack(fill = "both", expand = True)
        bg2 = ImageTk.PhotoImage(file = "french_version\Background_IMAGE_REGLES.png")
        canvas_regles.create_image( 0, 0, image = bg2, anchor = "nw")
        root_regles.mainloop()
    else :
        messagebox.showinfo("Erreur","Tu as déjà ouvert les règles du jeu !")

# Définition d'une fontion qui ouvre la fenêtre du mode Joueur 1 contre Joueur 2 :
def open_mode_jcj():
    '''
    Procédure qui définie ce qui se passe si l'utilisateur appuie sur le bouton "Joueur contre Joueur".

    Une nouvelle fenêtre de jeu est créée seulement si celle-ci n'est pas déjà ouverte.

    La procédure appelle par la suite d'autres fonctions pour afficher tous les éléments indispensables au jeu !
    '''
    global nb_allumettes, count_x, count_window_open
    if count_window_open == 0 :
        root_jcj = Toplevel(root)
        root_jcj.title("Partie entre deux joueurs")
        root_jcj.geometry("1080x720")
        root_jcj.minsize(1080, 720)
        root_jcj.maxsize(1080, 720)
        count_window_open+=1
        # Importer et afficher une image de fond :
        canvas_jcj = Canvas(root_jcj, width = 1080, height = 720)
        canvas_jcj.pack(fill = "both", expand = True)
        bg3 = ImageTk.PhotoImage(file = "img\Background_IMAGE.png")
        canvas_jcj.create_image( 0, 0, image = bg3, anchor = "nw")
        crea_button(root_jcj,canvas_jcj)
        spawn_allumettes(canvas_jcj)
        appelle_joueur(canvas_jcj)
    else :
        messagebox.showinfo("Erreur","Tu as déjà ouvert une fenêtre de jeu !\n\nFerme celle qui est ouverte d'abord...") 


def select_difficult():
    '''
    Procédure qui créée la fenêtre de choix qui apparaît à l'écran si l'utilisateur appuie sur "Joueur Contre Robot".

    On lui applique une image de fond, etc... 
    Puis on apelle la fonction qui implémante tous les éléments indispensables au choix (boutons, titres, ...)
    '''
    global count_window_open
    if count_window_open == 0 :
        root_selection = Toplevel(root)
        root_selection.title("Veuillez selectionner votre niveau de difficulté...")
        root_selection.geometry("1080x720")
        root_selection.minsize(1080, 720)
        root_selection.maxsize(1080, 720)
        count_window_open+=1
        # Importer et afficher une image de fond :
        canvas_selection = Canvas(root_selection, width = 1080, height = 720)
        canvas_selection.pack(fill = "both", expand = True)
        bg6 = ImageTk.PhotoImage(file = "img\Background_IMAGE.png")
        canvas_selection.create_image( 0, 0, image = bg6, anchor = "nw")
        selection_button(root_selection, canvas_selection)
        mainloop()
    else :
        messagebox.showinfo("Erreur","Tu as déjà ouvert une fenêtre de jeu !\n\nFerme celle qui est ouverte d'abord...")

def selection_button(root_menu, canvas):
    '''
    Fonction qui définie les éléments de la fenêtre de choix qui apparaît à l'écran si l'utilisateur appuie sur "Joueur Contre Robot"
    '''
    q=canvas.create_text(540.45, 200, text='Veuillez selectionner le niveau de difficulté du robot :', font=("Helvetica", 34), fill="white")
    s=canvas.create_rectangle(canvas.bbox(q),fill="#00bdfb")
    canvas.tag_lower(s,q)
    button_simple = Button(root_menu, text="Facile", command=lambda *args:open_mode_jco_simple(root_menu), font=("Helvetica", 50), fg='white', bg="#00bdfb", height = 2, width = 10)
    canvas.create_window(100, 320, anchor='nw', window=button_simple)
    button_difficile = Button(root_menu, text="Difficile", command=lambda *args:open_mode_jco_difficile(root_menu), font=("Helvetica", 50), fg='white', bg="#00bdfb", height = 2, width = 10)
    canvas.create_window(600, 320, anchor='nw', window=button_difficile)


# Définition d'une fontion qui ouvre la fenêtre du mode Ordinateur contre Ordinateur :
def open_mode_oco():
    '''
    Procédure qui définie ce qui se passe si l'utilisateur appuie sur le bouton "Ordinateur contre Ordinateur".

    Une nouvelle fenêtre de jeu est créée seulement si celle-ci n'est pas déjà ouverte.

    La procédure appelle par la suite d'autres fonctions pour afficher tous les éléments indispensables au jeu !
    '''
    global count_window_open
    if count_window_open == 0 :
        root_oco = Toplevel(root)
        root_oco.title("Partie entre deux ordinateurs")
        root_oco.geometry("1080x720")
        root_oco.minsize(1080, 720)
        root_oco.maxsize(1080, 720)
        count_window_open+=1
        # Importer et afficher une image de fond :
        canvas_oco = Canvas(root_oco, width = 1080, height = 720)
        canvas_oco.pack(fill = "both", expand = True)
        bg5 = ImageTk.PhotoImage(file = "img\Background_IMAGE.png")
        canvas_oco.create_image( 0, 0, image = bg5, anchor = "nw")
        appelle_robot_oco(canvas_oco, root_oco)
        spawn_allumettes_oco(canvas_oco)
    else :
        messagebox.showinfo("Erreur","Tu as déjà ouvert une fenêtre de jeu !\n\nFerme celle qui est ouverte d'abord...")

def msg_remerciment() :
    '''
    Procédure qui affiche un message de remerciment à l'utilisateur si celui-ci fini sa partie ou quitte le jeu en fermant la fenêtre.
    '''
    messagebox.showinfo("MERCI !","Merci beaucoup d'avoir joué à mon jeu !\n\n Dessins: Maéva LE GROS\n Développement: Romain MELLAZA")
    root.destroy()


# Ajouter un bouton pour ouvrir les règles du jeu :
button_rgl = Button(root, text="Les Règles du jeu", command=open_regles, font=("Helvetica", 14), fg='white', bg="#00bdfb", height = 2, width = 18)
button_rgl_window = canvas_accueil.create_window(855, 640, anchor='nw', window=button_rgl)

# Ajouter les différent boutons pour sélectionner les mode de jeu :

button_jcj = Button(root, text="Joueur 1 contre Joueur 2", command=open_mode_jcj, font=("Helvetica", 20), fg='white', bg="#00bdfb", height = 2, width = 22)
button_jcj_window = canvas_accueil.create_window(100, 400, anchor='nw', window=button_jcj)

button_jco = Button(root, text="Joueur contre Ordinateur", command=select_difficult, font=("Helvetica", 20), fg='white', bg="#00bdfb", height = 2, width = 22)
button_jco_window = canvas_accueil.create_window(640, 400, anchor='nw', window=button_jco)

button_oco = Button(root, text="Ordinateur contre Ordinateur", command=open_mode_oco, font=("Helvetica", 20), fg='white', bg="#00bdfb", height = 2, width = 22)
button_oco_window = canvas_accueil.create_window(375, 520, anchor='nw', window=button_oco)











##############################################################################################################################################################################################################
#                                                                                     MODE JOUEUR CONTRE JOUEUR                                                                                              #
#                                                                                                                                                                                                            #

# Définition d'une fonction qui créer les boutons pour prendre des allumettes:
def crea_button(racine,canvas):
    '''
    Fonction qui reçoit la fenêtre ("racine") ainsi que la toile ("canvas") où elle doit implemanter des boutons pour choisir le nombre d'allumette que l'utilisateur prends.

    Chaque pression sur un bouton appelle ensuite une fonction de supression d'allumettes en rapport.

    Elle renvoie les caractéristiques et l'emplacement des boutons sur la toile.
    '''
    global button1, button2, button3
    v=canvas.create_text(540, 525, text="Combien d'allumette(s) prenez-vous ?",font=("Helvetica", 30), fill="white")
    w=canvas.create_rectangle(canvas.bbox(v),fill="#00bdfb")
    canvas.tag_lower(w,v)
    button1 = Button(racine, text="1 allumette", command=lambda *args: suppr_allum(1, canvas, racine), font=("Helvetica", 14), fg='white', bg="#00bdfb", height = 2, width = 18)
    button1_window = canvas.create_window(75, 560, anchor='nw', window=button1)
    button2 = Button(racine, text="2 allumettes", command=lambda *args: suppr_allum(2, canvas, racine), font=("Helvetica", 14), fg='white', bg="#00bdfb", height = 2, width = 18)
    button2_window = canvas.create_window(430, 560, anchor='nw', window=button2)
    button3 = Button(racine, text="3 allumettes", command=lambda *args: suppr_allum(3, canvas, racine), font=("Helvetica", 14), fg='white', bg="#00bdfb", height = 2, width = 18)
    button3_window = canvas.create_window(780, 560, anchor='nw', window=button3)
    return button1_window, button2_window, button3_window


def spawn_allumettes(canvas):
    '''
    Fonction qui reçoit en paramètre la toile où elle doit afficher les images d'allumettes.

    A noter que j'utilise aussi cette fonction pour tous les modes sauf ordi contre ordi !

    Elle importe l'image et l'affiche à plusieurs positions dans la fenêtre, elle met toutes les données sur les images d'allumettes dans une liste "allum_list".
    '''
    global allum_list
    e=canvas.create_text(540, 450, text="Joueur 1",font=("Helvetica", 40), fill="blue")
    r=canvas.create_rectangle(canvas.bbox(e),fill="white")
    canvas.tag_lower(r, e)
    allum_img = ImageTk.PhotoImage(file = "img/allum_v1.png")
    allum1 = canvas.create_image(-30, 100, image = allum_img, anchor = 'nw')
    allum2 = canvas.create_image(20, 100, image = allum_img, anchor = 'nw')
    allum3 = canvas.create_image(70, 100, image = allum_img, anchor = 'nw')
    allum4 = canvas.create_image(120, 100, image = allum_img, anchor = 'nw')
    allum5 = canvas.create_image(170, 100, image = allum_img, anchor = 'nw')
    allum6 = canvas.create_image(220, 100, image = allum_img, anchor = 'nw')
    allum7 = canvas.create_image(270, 100, image = allum_img, anchor = 'nw')
    allum8 = canvas.create_image(320, 100, image = allum_img, anchor = 'nw')
    allum9 = canvas.create_image(370, 100, image = allum_img, anchor = 'nw')
    allum10 = canvas.create_image(420, 100, image = allum_img, anchor = 'nw')
    allum11 = canvas.create_image(470, 100, image = allum_img, anchor = 'nw')
    allum12 = canvas.create_image(520, 100, image = allum_img, anchor = 'nw')
    allum13 = canvas.create_image(570, 100, image = allum_img, anchor = 'nw')
    allum14 = canvas.create_image(620, 100, image = allum_img, anchor = 'nw')
    allum15 = canvas.create_image(670, 100, image = allum_img, anchor = 'nw')
    allum16 = canvas.create_image(720, 100, image = allum_img, anchor = 'nw')
    allum17 = canvas.create_image(770, 100, image = allum_img, anchor = 'nw')
    allum18 = canvas.create_image(820, 100, image = allum_img, anchor = 'nw')
    allum19 = canvas.create_image(870, 100, image = allum_img, anchor = 'nw')
    allum20 = canvas.create_image(920, 100, image = allum_img, anchor = 'nw')
    allum21 = canvas.create_image(970, 100, image = allum_img, anchor = 'nw')
    allum_list = [allum1, allum2, allum3, allum4, allum5, allum6, allum7, allum8, allum9, allum10, allum11, allum12, allum13, allum14,
    allum15, allum16, allum17, allum18, allum19, allum20, allum21]
    mainloop()


def suppr_allum(number, canvas_allum, root_correspondant):
    '''
    Fonction assez complexe qui admet en paramètre le nombre d'allumettes à supprimer "number" en fonction du bouton pressé (1 ou 2 ou 3) 
    ainsi que la toile du mode de jeu actuel "canvas_allum" (où sont donc les images d'allumettes à supprimer) et enfin la fenêtre correspondante "root_correspondant"
    
    La fonction soustrait le nombre d'allumettes prises au nombre d'allumettes restantes sur la table.
    Elle appelle ensuite le joueur qui doit jouer à ce tour grâce à la fonction "appelle_joueur()"

    En fonction du nombre d'allumettes restantes, les boutons pour prendre plus que possible se désactivent automatiquement !

    En fonction du nombre d'allumettes prises, le programme supprime le bon nombre d'images correspondant.

    Si il ne reste plus aucune allumette sur la table, le programme infomre le joueur actuel de sa défaite, ferme la fenêtre de jeu, réinitialise toutes las valeurs,
    les joueurs peuvent donc rejouer sans fermer complétement le jeu !

    Si l'utilisateur ferme manuellement le jeu, le message de remerciment est affiché !
    '''
    global nb_allumettes, count_x, count_player, count_window_open
    nb_allumettes = nb_allumettes - number
    appelle_joueur(canvas_allum)
    if nb_allumettes == 2 :
        button3['state'] = DISABLED
    elif nb_allumettes == 1: 
        button3['state'] = DISABLED
        button2['state'] = DISABLED
    if number == 3:
        canvas_allum.delete(allum_list[count_x])
        count_x+=1
        canvas_allum.delete(allum_list[count_x])
        count_x+=1
        canvas_allum.delete(allum_list[count_x])
        count_x+=1
        count_player+=1
    elif number == 2:
        canvas_allum.delete(allum_list[count_x])
        count_x+=1
        canvas_allum.delete(allum_list[count_x])
        count_x+=1
        count_player+=1
    elif number == 1:
        canvas_allum.delete(allum_list[count_x])
        count_x+=1
        count_player+=1
    if nb_allumettes == 0 :
        messagebox.showinfo("Perdu ! :(","Tu as pris la dernière allumette, dommage...")
        root_correspondant.destroy()
        nb_allumettes = 21
        count_x = 0
        count_player = 2
        count_window_open = 0
    try:
        root_correspondant.protocol('WM_DELETE_WINDOW', msg_remerciment)
    except:
        pass


def appelle_joueur(canvas):
    '''
    Fonction qui admet la toile du mode de jeu actuel "canvas" pour y afficher le joueur a qui c'est le tour de jouer
    en fonction de compteur de tour "count_player" (si il est pair ou impair).
    '''
    global count_player
    print('Count_PLAYER :', count_player)
    if count_player % 2 == 1 :
        e=canvas.create_text(540, 450, text="Joueur 1",font=("Helvetica", 40), fill="blue")
        r=canvas.create_rectangle(canvas.bbox(e),fill="white")
        canvas.tag_lower(r, e)
    if count_player % 2 == 0 :
        d=canvas.create_text(540, 450, text="Joueur 2",font=("Helvetica", 40), fill="red")
        f=canvas.create_rectangle(canvas.bbox(d),fill="white")
        canvas.tag_lower(f, d)




##############################################################################################################################################################################################################
#                                                                                MODE JOUEUR CONTRE ORDINATEUR (DIFFICULTÉ = SIMPLE)                                                                         #
#                                                                                                                                                                                                            #


# Définition d'une fonction qui créer les boutons pour prendre des allumettes:
def crea_button_robot_simple(racine,canvas):
    '''
    Fonction qui reçoit la fenêtre ("racine") ainsi que la toile ("canvas") où elle doit implemanter des boutons pour choisir le nombre d'allumette que l'utilisateur prends.

    Chaque pression sur un bouton appelle ensuite une fonction de supression d'allumettes en rapport.

    Elle renvoie les caractéristiques et l'emplacement des boutons sur la toile.

    La seule différence avec la fonction classique est que le robot peut ne pas l'appeler systématiquement car lui il passe directemnt par le suppression, et n'appuie évidemment sur aucun boutton !
    '''
    global button1, button2, button3
    v=canvas.create_text(540, 525, text="Combien d'allumette(s) prenez-vous ?",font=("Helvetica", 30), fill="white")
    w=canvas.create_rectangle(canvas.bbox(v),fill="#00bdfb")
    canvas.tag_lower(w,v)
    button1 = Button(racine, text="1 allumette", command=lambda *args: suppr_allum_robot_simple(1, canvas, racine), font=("Helvetica", 14), fg='white', bg="#00bdfb", height = 2, width = 18)
    button1_window = canvas.create_window(75, 560, anchor='nw', window=button1)
    button2 = Button(racine, text="2 allumettes", command=lambda *args: suppr_allum_robot_simple(2, canvas, racine), font=("Helvetica", 14), fg='white', bg="#00bdfb", height = 2, width = 18)
    button2_window = canvas.create_window(430, 560, anchor='nw', window=button2)
    button3 = Button(racine, text="3 allumettes", command=lambda *args: suppr_allum_robot_simple(3, canvas, racine), font=("Helvetica", 14), fg='white', bg="#00bdfb", height = 2, width = 18)
    button3_window = canvas.create_window(780, 560, anchor='nw', window=button3)
    return button1_window, button2_window, button3_window


# J'utilise aussi la fontion "spawn_allumettes" vue précedemment.


def suppr_allum_robot_simple(number, canvas_allum, root_correspondant):
    '''
    Fonction assez complexe qui admet en paramètre le nombre d'allumettes à supprimer "number" en fonction du bouton pressé (1 ou 2 ou 3) 
    ainsi que la toile du mode de jeu actuel "canvas_allum" (où sont donc les images d'allumettes à supprimer) et enfin la fenêtre correspondante "root_correspondant"
    
    La fonction soustrait le nombre d'allumettes prises au nombre d'allumettes restantes sur la table.
    Elle appelle ensuite le joueur ou le robot qui doit jouer à ce tour grâce à la fonction "appelle_robot()"

    En fonction du nombre d'allumettes restantes, les boutons pour prendre plus que possible se désactivent automatiquement !

    En fonction du nombre d'allumettes prises, le programme supprime le bon nombre d'images correspondant.

    Si il ne reste plus aucune allumette sur la table, le programme infomre le joueur actuel de sa défaite, ferme la fenêtre de jeu, réinitialise toutes las valeurs,
    les joueurs peuvent donc rejouer sans fermer complétement le jeu !

    Si l'utilisateur ferme manuellement le jeu, le message de remerciment est affiché !

    La seule différence avec la fonction classique, est que la fonction appelle le robot une fois sur deux et non pas deux joueurs !
    '''
    global nb_allumettes, count_x, count_player, count_window_open
    nb_allumettes = nb_allumettes - number
    appelle_robot(canvas_allum, root_correspondant)
    if nb_allumettes == 2 :
        button3['state'] = DISABLED
    elif nb_allumettes == 1: 
        button3['state'] = DISABLED
        button2['state'] = DISABLED
        button1['state'] = DISABLED
    if number == 3:
        canvas_allum.delete(allum_list[count_x])
        count_x+=1
        canvas_allum.delete(allum_list[count_x])
        count_x+=1
        canvas_allum.delete(allum_list[count_x])
        count_x+=1
        count_player+=1
        if nb_allumettes == 1 :
            messagebox.showinfo("Perdu ! :(","Tu es obligé de prendre la dernière allumette, dommage...")
            msg_remerciment()
    elif number == 2:
        canvas_allum.delete(allum_list[count_x])
        count_x+=1
        canvas_allum.delete(allum_list[count_x])
        count_x+=1
        count_player+=1
        if nb_allumettes == 1 :
            messagebox.showinfo("Perdu ! :(","Tu es obligé de prendre la dernière allumette, dommage...")
            msg_remerciment()
    elif number == 1:
        canvas_allum.delete(allum_list[count_x])
        count_x+=1
        count_player+=1
        if nb_allumettes == 1 :
            messagebox.showinfo("Perdu ! :(","Tu es obligé de prendre la dernière allumette, dommage...")
            msg_remerciment()
    try:
        root_correspondant.protocol('WM_DELETE_WINDOW', msg_remerciment)
    except:
        pass


def appelle_robot(canvas, root_correspondant):
    '''
    Fonction qui admet la toile du mode de jeu actuel "canvas" pour y afficher le joueur ou le robot a qui c'est le tour de jouer
    en fonction de compteur de tour "count_player" (si il est pair ou impair).

    Lorsque c'est au robot de jouer elle désactive tous les bouttons pour que le joueur ne joue pas à ça place ! (et inversement)

    Le robot prends des allumettes de manière aléatoire jusqu'à qu'il n'en reste que 3 ou moins, pour éviter qu'il joue "débilement"

    (Voir directement les commentaires dans le code pour comprendre la logique)
    '''
    global count_player, nb_robot, count_x, count_window_open
    if count_player % 2 == 1 :
        button1['state'] = NORMAL               # commande TRES utile qui permet de changer l'état des bouttons
        button2['state'] = NORMAL
        button3['state'] = NORMAL
        e=canvas.create_text(540, 450, text="Joueur 1",font=("Helvetica", 40), fill="blue")
        r=canvas.create_rectangle(canvas.bbox(e),fill="white")
        canvas.tag_lower(r, e)
    if count_player % 2 == 0 :
        d=canvas.create_text(540, 450, text=" ROBOT ",font=("Helvetica", 40), fill="red")
        f=canvas.create_rectangle(canvas.bbox(d),fill="white")
        canvas.tag_lower(f, d)
        button1['state'] = DISABLED
        button2['state'] = DISABLED
        button3['state'] = DISABLED
        nb_robot=randint(1,3)               # Je détermine de manière complétement alétoire le nombre d'allumettes prises par le robot
        while nb_robot > nb_allumettes :    # MAIS ATTENTION si le robot veut prendre plus d'allumettes qu'il n'y en a sur la table alors il redétermine une valeur aléatoirement jusqu'à que la condition soit fausse et que le programme sorte de la boucle
            nb_robot=randint(1,3)
        if nb_allumettes == 3 :             # Si il reste 3 allumettes sur la table, alors le robot en prends 2 pour piéger le joueur
            nb_robot = 2
        elif nb_allumettes == 2 :           # Si il reste 2 allumettes sur la table, alors le robot en prends 1 pour piéger le joueur
            nb_robot = 1
        elif nb_allumettes == 1 :           # Si il ne reste plus qu'une seule allumette alors le robot est obligé de la prendre et de concéder la défaite... Je ferme le jeu par la suite.
            messagebox.showinfo("Gagné ! :)","Le robot est obligé de prendre la dernière allumette, bien joué !")
            msg_remerciment()
        canvas.after(3000, suppr_allum_robot_simple, nb_robot, canvas, root_correspondant)      # Cette fonction permet d'éxécuter la fonction "suppr_allum_robot_simple()" vue juste au-dessus après 3000ms et avec mon nombre qui vient d'être déterminé, en argument.


# Définition d'une fontion qui ouvre la fenêtre du mode Joueur 1 contre un Ordinateur (difficulté : simple) :
def open_mode_jco_simple(root_precedent):
    '''
    Fonction qui admet en paramètre la fenêtre de sélection de difficulté pour pouvoir la supprimmer juste après qu'elle est donnée naissance à celle-ci !

    Une nouvelle fenêtre de jeu est créée seulement si celle-ci n'est pas déjà ouverte.

    Les paramètres de bases sont appliqués.

    La fonction appelle par la suite d'autres fonctions pour afficher tous les éléments indispensables au jeu !
    '''
    root_precedent.destroy()
    root_jco_simple = Toplevel(root)
    root_jco_simple.title("Partie entre un joueur et un ordinateur (difficulté = simple)")
    root_jco_simple.geometry("1080x720")
    root_jco_simple.minsize(1080, 720)
    root_jco_simple.maxsize(1080, 720)
    # Importer et afficher une image de fond :
    canvas_jco_simple = Canvas(root_jco_simple, width = 1080, height = 720)
    canvas_jco_simple.pack(fill = "both", expand = True)
    bg4 = ImageTk.PhotoImage(file = "img\Background_IMAGE.png")
    canvas_jco_simple.create_image( 0, 0, image = bg4, anchor = "nw")
    crea_button_robot_simple(root_jco_simple, canvas_jco_simple)
    spawn_allumettes(canvas_jco_simple)



##############################################################################################################################################################################################################
#                                                                              MODE JOUEUR CONTRE ORDINATEUR (DIFFICULTÉ = DIFFICILE)                                                                        #
#                                                                                                                                                                                                            #



def crea_button_robot_difficile(racine,canvas):
    '''
    Fonction qui reçoit la fenêtre ("racine") ainsi que la toile ("canvas") où elle doit implemanter des boutons pour choisir le nombre d'allumette que l'utilisateur prends.

    Chaque pression sur un bouton appelle ensuite une fonction de supression d'allumettes en rapport.

    Elle renvoie les caractéristiques et l'emplacement des boutons sur la toile.

    La seule différence avec la fonction classique est que le robot peut ne pas l'appeler systématiquement car lui il passe directemnt par le suppression, et n'appuie évidemment sur aucun boutton !
    '''
    global button1, button2, button3
    v=canvas.create_text(540, 525, text="Combien d'allumette(s) prenez-vous ?",font=("Helvetica", 30), fill="white")
    w=canvas.create_rectangle(canvas.bbox(v),fill="#00bdfb")
    canvas.tag_lower(w,v)
    button1 = Button(racine, text="1 allumette", command=lambda *args: suppr_allum_robot_difficile(1, canvas, racine), font=("Helvetica", 14), fg='white', bg="#00bdfb", height = 2, width = 18)
    button1_window = canvas.create_window(75, 560, anchor='nw', window=button1)
    button2 = Button(racine, text="2 allumettes", command=lambda *args: suppr_allum_robot_difficile(2, canvas, racine), font=("Helvetica", 14), fg='white', bg="#00bdfb", height = 2, width = 18)
    button2_window = canvas.create_window(430, 560, anchor='nw', window=button2)
    button3 = Button(racine, text="3 allumettes", command=lambda *args: suppr_allum_robot_difficile(3, canvas, racine), font=("Helvetica", 14), fg='white', bg="#00bdfb", height = 2, width = 18)
    button3_window = canvas.create_window(780, 560, anchor='nw', window=button3)
    return button1_window, button2_window, button3_window


def suppr_allum_robot_difficile(number, canvas_allum, root_correspondant):
    '''
    Fonction assez complexe qui admet en paramètre le nombre d'allumettes à supprimer "number" en fonction du bouton pressé (1 ou 2 ou 3) 
    ainsi que la toile du mode de jeu actuel "canvas_allum" (où sont donc les images d'allumettes à supprimer) et enfin la fenêtre correspondante "root_correspondant"
    
    La fonction soustrait le nombre d'allumettes prises au nombre d'allumettes restantes sur la table.
    Elle appelle ensuite le joueur ou le robot qui doit jouer à ce tour grâce à la fonction "appelle_robot()"

    En fonction du nombre d'allumettes restantes, les boutons pour prendre plus que possible se désactivent automatiquement !

    En fonction du nombre d'allumettes prises, le programme supprime le bon nombre d'images correspondant.

    Si il ne reste plus aucune allumette sur la table, le programme infomre le joueur actuel de sa défaite, ferme la fenêtre de jeu, réinitialise toutes las valeurs,
    les joueurs peuvent donc rejouer sans fermer complétement le jeu !

    Si l'utilisateur ferme manuellement le jeu, le message de remerciment est affiché !

    La seule différence avec la fonction classique, est que la fonction appelle le robot une fois sur deux et non pas deux joueurs !
    '''
    global nb_allumettes, count_x, count_player, count_window_open
    nb_allumettes = nb_allumettes - number
    appelle_robot_difficile(canvas_allum, root_correspondant)
    if nb_allumettes == 2 :
        button3['state'] = DISABLED
    elif nb_allumettes == 1: 
        button3['state'] = DISABLED
        button2['state'] = DISABLED
        button1['state'] = DISABLED
    if number == 3:
        canvas_allum.delete(allum_list[count_x])
        count_x+=1
        canvas_allum.delete(allum_list[count_x])
        count_x+=1
        canvas_allum.delete(allum_list[count_x])
        count_x+=1
        count_player+=1
        if nb_allumettes == 1 :
            messagebox.showinfo("Perdu ! :(","Tu es obligé de prendre la dernière allumette, dommage...")
            msg_remerciment()
    elif number == 2:
        canvas_allum.delete(allum_list[count_x])
        count_x+=1
        canvas_allum.delete(allum_list[count_x])
        count_x+=1
        count_player+=1
        if nb_allumettes == 1 :
            messagebox.showinfo("Perdu ! :(","Tu es obligé de prendre la dernière allumette, dommage...")
            msg_remerciment()
    elif number == 1:
        canvas_allum.delete(allum_list[count_x])
        count_x+=1
        count_player+=1
        if nb_allumettes == 1 :
            messagebox.showinfo("Perdu ! :(","Tu es obligé de prendre la dernière allumette, dommage...")
            msg_remerciment()
    try:
        root_correspondant.protocol('WM_DELETE_WINDOW', msg_remerciment)
    except:
        pass


def appelle_robot_difficile(canvas, root_correspondant):
    '''
    Fonction qui admet la toile du mode de jeu actuel "canvas" pour y afficher le joueur ou le robot a qui c'est le tour de jouer
    en fonction de compteur de tour "count_player" (si il est pair ou impair).

    Lorsque c'est au robot de jouer elle désactive tous les bouttons pour que le joueur ne joue pas à ça place ! (et inversement)

    Le robot prends ici des allumettes de manière algorithmique, et logique

    (Voir directement les commentaires dans le code pour comprendre la logique)
    '''
    global count_player, nb_robot, count_x, count_window_open
    if count_player % 2 == 1 :
        button1['state'] = NORMAL
        button2['state'] = NORMAL
        button3['state'] = NORMAL
        e=canvas.create_text(540, 450, text="Joueur 1",font=("Helvetica", 40), fill="blue")
        r=canvas.create_rectangle(canvas.bbox(e),fill="white")
        canvas.tag_lower(r, e)
    if count_player % 2 == 0 :
        d=canvas.create_text(540, 450, text=" ROBOT ",font=("Helvetica", 40), fill="red")
        f=canvas.create_rectangle(canvas.bbox(d),fill="white")
        canvas.tag_lower(f, d)
        button1['state'] = DISABLED
        button2['state'] = DISABLED
        button3['state'] = DISABLED
        if nb_allumettes % 4 == 3:                  # Ici contrairement à la difficulté simple, je détermine de manière algorithmique le nombre d'allumettes que le robot doit prendre pour être sûr de gagner !
            nb_robot = 2
        elif nb_allumettes % 4 == 2:
            nb_robot = 1
        elif nb_allumettes % 4 == 0:
            nb_robot = 3
        else:
            nb_robot = 1
        if nb_allumettes == 1 :
            messagebox.showinfo("Gagné ! :)","Le robot est obligé de prendre la dernière allumette, bien joué !")
            msg_remerciment()
        canvas.after(3000, suppr_allum_robot_difficile, nb_robot, canvas, root_correspondant)             # Cette fonction permet d'éxécuter la fonction "suppr_allum_robot_simple()" vue juste au-dessus après 3000ms et avec mon nombre qui vient d'être déterminé, en argument.


# Définition d'une fontion qui ouvre la fenêtre du mode Joueur 1 contre un Ordinateur :
def open_mode_jco_difficile(root_precedent):
    '''
    Fonction qui admet en paramètre la fenêtre de sélection de difficulté pour pouvoir la supprimmer juste après qu'elle est donnée naissance à celle-ci !

    Une nouvelle fenêtre de jeu est créée seulement si celle-ci n'est pas déjà ouverte.

    Les paramètres de bases sont appliqués.

    La fonction appelle par la suite d'autres fonctions pour afficher tous les éléments indispensables au jeu !
    '''
    root_precedent.destroy()
    root_jco_difficile = Toplevel(root)
    root_jco_difficile.title("Partie entre un joueur et un ordinateur (difficulté = difficile)")
    root_jco_difficile.geometry("1080x720")
    root_jco_difficile.minsize(1080, 720)
    root_jco_difficile.maxsize(1080, 720)
    # Importer et afficher une image de fond :
    canvas_jco_difficile = Canvas(root_jco_difficile, width = 1080, height = 720)
    canvas_jco_difficile.pack(fill = "both", expand = True)
    bg4 = ImageTk.PhotoImage(file = "img\Background_IMAGE.png")
    canvas_jco_difficile.create_image( 0, 0, image = bg4, anchor = "nw")
    crea_button_robot_difficile(root_jco_difficile,canvas_jco_difficile)
    spawn_allumettes(canvas_jco_difficile)




##############################################################################################################################################################################################################
#                                                                              MODE ORDINATEUR CONTRE ORDINATEUR                                                                                             #
#                                                                                                                                                                                                            #





def spawn_allumettes_oco(canvas):
    '''
    Fonction qui reçoit en paramètre la toile où elle doit afficher les images d'allumettes.

    A noter que j'utilise aussi cette fonction pour tous les modes sauf ordi contre ordi !

    Elle importe l'image et l'affiche à plusieurs positions dans la fenêtre, elle met toutes les données sur les images d'allumettes dans une liste "allum_list".

    Cette fonction est strictement la même que la classique, seulement le 1er joueur est remplacé par Marcus le robot. :)
    '''
    global allum_list
    e=canvas.create_text(540, 450, text="Marcus",font=("Helvetica", 40), fill="blue")
    r=canvas.create_rectangle(canvas.bbox(e),fill="white")
    canvas.tag_lower(r, e)
    allum_img = ImageTk.PhotoImage(file = "img/allum_v1.png")
    allum1 = canvas.create_image(-30, 100, image = allum_img, anchor = 'nw')
    allum2 = canvas.create_image(20, 100, image = allum_img, anchor = 'nw')
    allum3 = canvas.create_image(70, 100, image = allum_img, anchor = 'nw')
    allum4 = canvas.create_image(120, 100, image = allum_img, anchor = 'nw')
    allum5 = canvas.create_image(170, 100, image = allum_img, anchor = 'nw')
    allum6 = canvas.create_image(220, 100, image = allum_img, anchor = 'nw')
    allum7 = canvas.create_image(270, 100, image = allum_img, anchor = 'nw')
    allum8 = canvas.create_image(320, 100, image = allum_img, anchor = 'nw')
    allum9 = canvas.create_image(370, 100, image = allum_img, anchor = 'nw')
    allum10 = canvas.create_image(420, 100, image = allum_img, anchor = 'nw')
    allum11 = canvas.create_image(470, 100, image = allum_img, anchor = 'nw')
    allum12 = canvas.create_image(520, 100, image = allum_img, anchor = 'nw')
    allum13 = canvas.create_image(570, 100, image = allum_img, anchor = 'nw')
    allum14 = canvas.create_image(620, 100, image = allum_img, anchor = 'nw')
    allum15 = canvas.create_image(670, 100, image = allum_img, anchor = 'nw')
    allum16 = canvas.create_image(720, 100, image = allum_img, anchor = 'nw')
    allum17 = canvas.create_image(770, 100, image = allum_img, anchor = 'nw')
    allum18 = canvas.create_image(820, 100, image = allum_img, anchor = 'nw')
    allum19 = canvas.create_image(870, 100, image = allum_img, anchor = 'nw')
    allum20 = canvas.create_image(920, 100, image = allum_img, anchor = 'nw')
    allum21 = canvas.create_image(970, 100, image = allum_img, anchor = 'nw')
    allum_list = [allum1, allum2, allum3, allum4, allum5, allum6, allum7, allum8, allum9, allum10, allum11, allum12, allum13, allum14,
    allum15, allum16, allum17, allum18, allum19, allum20, allum21]
    mainloop()   




def suppr_allum_robot_simple_oco(number, canvas_allum, root_correspondant):
    '''
    Fonction assez complexe qui admet en paramètre le nombre d'allumettes à supprimer "number" en fonction du bouton pressé (1 ou 2 ou 3) 
    ainsi que la toile du mode de jeu actuel "canvas_allum" (où sont donc les images d'allumettes à supprimer) et enfin la fenêtre correspondante "root_correspondant"
    
    La fonction soustrait le nombre d'allumettes prises au nombre d'allumettes restantes sur la table.
    Elle appelle ensuite le joueur ou le robot qui doit jouer à ce tour grâce à la fonction "appelle_robot()"

    En fonction du nombre d'allumettes restantes, les boutons pour prendre plus que possible se désactivent automatiquement !

    En fonction du nombre d'allumettes prises, le programme supprime le bon nombre d'images correspondant.

    Si il ne reste plus aucune allumette sur la table, le programme infomre le joueur actuel de sa défaite, ferme la fenêtre de jeu, réinitialise toutes las valeurs,
    les joueurs peuvent donc rejouer sans fermer complétement le jeu !

    Si l'utilisateur ferme manuellement le jeu, le message de remerciment est affiché !

    La seule différence avec la fonction classique, est que la fonction appelle deux robots et non pas deux joueurs (qui devrait par conséquent cliquer) !
    '''
    global nb_allumettes, count_x, count_player, count_window_open
    nb_allumettes = nb_allumettes - number    
    if number == 3:
        canvas_allum.delete(allum_list[count_x])
        count_x+=1
        canvas_allum.delete(allum_list[count_x])
        count_x+=1
        canvas_allum.delete(allum_list[count_x])
        count_x+=1
        appelle_robot_oco(canvas_allum, root_correspondant)
        count_player+=1
    elif number == 2:
        canvas_allum.delete(allum_list[count_x])
        count_x+=1
        canvas_allum.delete(allum_list[count_x])
        count_x+=1
        appelle_robot_oco(canvas_allum, root_correspondant)
        count_player+=1
    elif number == 1:
        canvas_allum.delete(allum_list[count_x])
        count_x+=1
        appelle_robot_oco(canvas_allum, root_correspondant)
        count_player+=1
    try:
        root_correspondant.protocol('WM_DELETE_WINDOW', msg_remerciment)
    except:
        pass



def appelle_robot_oco(canvas, root_correspondant):
    '''
    Fonction qui admet la toile du mode de jeu actuel "canvas" pour y afficher le robot Donald ou le robot Marcus a qui c'est le tour de jouer
    en fonction de compteur de tour "count_player" (si il est pair ou impair).

    Lorsque c'est au robot de jouer elle désactive tous les bouttons pour que le joueur ne joue pas à ça place ! (et inversement)

    Les robots ont ici exactement la même logique que dans le mode difficulté simple du jco, c'est àdire aléatoire jusqu'à qu'il ne reste plus que 3 allumettes

    (Voir directement les commentaires dans le code pour comprendre la logique)
    '''
    global count_player, nb_robot
    if count_player % 2 == 1 :
        e=canvas.create_text(540, 450, text="Marcus",font=("Helvetica", 40), fill="blue")
        r=canvas.create_rectangle(canvas.bbox(e),fill="white")
        canvas.tag_lower(r, e)
        nb_robot=randint(1,3)
        while nb_robot > nb_allumettes :
            nb_robot=randint(1,3)
        if nb_allumettes == 3 :
            nb_robot = 2
        elif nb_allumettes == 2 :
            nb_robot = 1
        elif nb_allumettes == 1 :
            messagebox.showinfo("FINI !","AH MINCE J'AI PERDU, bien joué Donald !")                 # Je peux donc savoir quel robot a gagné et par conséquent quel robot a perdu !
            msg_remerciment()
        canvas.after(1500, suppr_allum_robot_simple_oco, nb_robot, canvas, root_correspondant)      # Cette fonction permet d'éxécuter la fonction "suppr_allum_robot_simple_oco()" vue juste au-dessus après 1500ms et avec mon nombre qui vient d'être déterminé, en argument.
    if count_player % 2 == 0 :
        d=canvas.create_text(540, 450, text="Donald",font=("Helvetica", 40), fill="red")
        f=canvas.create_rectangle(canvas.bbox(d),fill="white")
        canvas.tag_lower(f, d)
        nb_robot=randint(1,3)
        while nb_robot > nb_allumettes :
            nb_robot=randint(1,3)
        if nb_allumettes == 3 :
            nb_robot = 2
        elif nb_allumettes == 2 :
            nb_robot = 1
        elif nb_allumettes == 1 :
            messagebox.showinfo("FINI !","AH MINCE J'AI PERDU, bien joué Marcus !")                 # Je peux donc savoir quel robot a gagné et par conséquent quel robot a perdu !
            msg_remerciment()
        canvas.after(1500, suppr_allum_robot_simple_oco, nb_robot, canvas, root_correspondant)      # Cette fonction permet d'éxécuter la fonction "suppr_allum_robot_simple_oco()" vue juste au-dessus après 1500ms et avec mon nombre qui vient d'être déterminé, en argument.



    


# Si l'utilisateur ferme l'accueil cela affiche le message de remerciment :
root.protocol('WM_DELETE_WINDOW', msg_remerciment)


# Je rafraîchis continuellement mon application via cette commade :
root.mainloop()