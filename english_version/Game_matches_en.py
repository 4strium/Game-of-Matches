# $$$$$$$\                                    $$\                 $$\      $$\     
# $$  __$$\                                   \__|                $$$\    $$$ |    
# $$ |  $$ | $$$$$$\  $$$$$$\$$$$\   $$$$$$\  $$\ $$$$$$$\        $$$$\  $$$$ |    
# $$$$$$$  |$$  __$$\ $$  _$$  _$$\  \____$$\ $$ |$$  __$$\       $$\$$\$$ $$ |    
# $$  __$$< $$ /  $$ |$$ / $$ / $$ | $$$$$$$ |$$ |$$ |  $$ |      $$ \$$$  $$ |    
# $$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$  __$$ |$$ |$$ |  $$ |      $$ |\$  /$$ |    
# $$ |  $$ |\$$$$$$  |$$ | $$ | $$ |\$$$$$$$ |$$ |$$ |  $$ |      $$ | \_/ $$ |$$\ 
# \__|  \__| \______/ \__| \__| \__| \_______|\__|\__|  \__|      \__|     \__|\__|

#
# Description: Program that allows the user to play (via a TKinter graphical interface) the game of matches.
# Four modes are available: Player vs. Player, Player vs. Computer (random), Player vs. Computer (algorithmic) and Computer vs. Computer (random).
# To see the rules of the game click on the corresponding button in the home page!
# 

# I import the modules essential to the proper functioning of my program:
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from random import randint

# I define my parent window that I will call "root" (this will be my homepage):
root = Tk()

# I define parameters to this window:
root.title("The Game of 21 matches by Romain MELLAZA")       # A title
root.geometry("1080x720")                                       # A display resolution, here HD
root.minsize(1080, 720)                                         # I block this resolution, to prevent the user from resizing anyhow.
root.maxsize(1080, 720)
root.iconbitmap(default='icon\LOGO_v1.ico')                     # I define a logo for the window.


# I define essential variables with their default values:
nb_allumettes = 21                                              # The number of matches initially on the table
count_x = 0                                                     # Variable to count the rank of match images according to the number to delete (see fctn "suppr_allum")
allum_list=[]                                                   # List that will contain all match images
count_player = 2                                                # Counter that allows the program to know which player (or robot) it's the turn to play!
count_window_open = 0                                           # Counter that allows the program to know how many game windows, the user has opened !
count_window_regles = 0                                         # Counter that allows the program to know how many rules windows, the user has opened !
name_defined = False
player1 = None
player2 = None

# I import and display a background image for my homepage:
bg = PhotoImage(file = "img\Background_IMAGE.png")
canvas_accueil = Canvas( root, width = 1080, height = 720)
canvas_accueil.pack(fill = "both", expand = True)
canvas_accueil.create_image( 0, 0, image = bg, anchor = "nw")

# Add a title to my homepage:
# I create a white text to which I add a blue highlight behind.
i=canvas_accueil.create_text(540.45, 137, text='Welcome to the super match game!', font=("Helvetica", 45), fill="white")
r=canvas_accueil.create_rectangle(canvas_accueil.bbox(i),fill="#00bdfb")                                                              
canvas_accueil.tag_lower(r,i)

# Add a subtitle to my homepage:
# I create a white text to which I add a blue highlight behind.
k=canvas_accueil.create_text(540.45, 310, text='Please select a game mode:', font=("Helvetica", 38), fill="white")
l=canvas_accueil.create_rectangle(canvas_accueil.bbox(k),fill="#00bdfb")
canvas_accueil.tag_lower(l,k)






##############################################################################################################################################################################################################
#                                                                                     HOMEPAGE                                                                                                               #
#                                                                                                                                                                                                            #

def reset_count_win_reg():
    '''
    Procedure that resets the open rules counter
    '''
    global count_window_regles, root_regles
    count_window_regles = 0
    root_regles.destroy()

def reset_count_win_game():
    '''
    Procedure that resets the open game window counter
    '''
    global count_window_open, root_name, root_jcj, root_selection, root_oco, nb_allumettes, count_x, count_player, allum_list, root_jco_difficile
    count_window_open = 0
    nb_allumettes = 21
    allum_list = []
    count_x = 0
    count_player = 0
    try :
        root_name.destroy()
    except :
        pass
    try :
        root_jcj.destroy()
    except :
        pass
    try :
        root_selection.destroy()
    except :
        pass
    try :
        root_oco.destroy()
    except :
        pass
    try :
        root_jco_simple.destroy()
    except :
        pass
    try :
        root_jco_difficile.destroy()
    except :
        pass


# Defining a function that opens the game rules window:
def open_regles():
    '''
    Procedure that opens the rules window only if it is not already open.

    The rulers are imported and displayed directly on a new canvas in a new window.

    On the other hand, if it is already open then an error message is displayed on the user's screen.
    '''
    global count_window_regles
    if count_window_regles == 0 :
        root_regles = Toplevel(root)
        root_regles.title("Match game rules")
        root_regles.geometry("1080x720")
        root_regles.minsize(1080, 720)
        root_regles.maxsize(1080, 720)
        count_window_regles+=1
        # Importer et afficher une image de fond :
        canvas_regles = Canvas(root_regles, width = 1080, height = 720)
        canvas_regles.pack(fill = "both", expand = True)
        bg2 = ImageTk.PhotoImage(file = "english_version\Background_IMAGE_REGLES.png")
        canvas_regles.create_image( 0, 0, image = bg2, anchor = "nw")
        root_regles.mainloop()
    else :
        messagebox.showinfo("Error","You have already opened the rules of the game!")


def switch_jcj():
    global name_defined
    if name_defined == False :
        choose_name()
    else :
        open_mode_jcj(player1, player2)

def validation_name_user(root_to_close):
    """
    
    """
    global count_window_open, name_defined, player1, player2
    count_window_open = 0
    name_defined = True

    player1 = entry1.get()
    player2 = entry2.get()

    if len(player1) > 0 :
        player1 = player1[:14]
    if len(player2) > 0 :
        player2 = player2[:14]

    if len(player1) == 0 :
        player1 = "Player 1"
    if len(player2) == 0 :
        player2 = "Player 2"

    player1 = " " + player1 + " "
    player2 = " " + player2 + " "

    root_to_close.destroy()

    open_mode_jcj(player1, player2)


def choose_name():
    global root_name, count_window_open, entry1, entry2
    if count_window_open == 0 :
        root_name = Toplevel(root)
        root_name.title("Choose your names...")
        root_name.geometry("1080x720")
        root_name.minsize(1080, 720)
        root_name.maxsize(1080, 720)
        count_window_open+=1
        # Import and display a background image:
        canvas_name = Canvas(root_name, width = 1080, height = 720)
        canvas_name.pack(fill = "both", expand = True)
        bg3 = ImageTk.PhotoImage(file = "img\Background_IMAGE.png")
        canvas_name.create_image( 0, 0, image = bg3, anchor = "nw")
        
        i=canvas_name.create_text(540.45, 137, text='Choose your nicknames for the game:', font=("Helvetica", 40), fill="white")
        r=canvas_name.create_rectangle(canvas_name.bbox(i),fill="#00bdfb")                                                              
        canvas_name.tag_lower(r,i)


        q=canvas_name.create_text(530, 265, text=' Player 1 : ', font=("Helvetica", 24), fill="blue")
        s=canvas_name.create_rectangle(canvas_name.bbox(q),fill="white")                                                              
        canvas_name.tag_lower(s,q)
        entry1 = Entry(root_name, font=("Helvetica", 24), width=14, bd=0)
        canvas_name.create_window(400, 290, anchor='nw', window=entry1)
        entry1.focus()

        x=canvas_name.create_text(530, 400, text=' Player 2 : ', font=("Helvetica", 24), fill="red")
        c=canvas_name.create_rectangle(canvas_name.bbox(x),fill="white")                                                              
        canvas_name.tag_lower(c,x)
        entry2 = Entry(root_name, font=("Helvetica", 24), width=14, bd=0)
        canvas_name.create_window(400, 425, anchor='nw', window=entry2)
        

        validation_btn = Button(root_name, text="Validate", font=("Helvetica", 25), fg='white', bg="#00bdfb", height = 1, width = 10, command=lambda *args:validation_name_user(root_name))
        canvas_name.create_window(425, 550, anchor='nw', window=validation_btn)

        root_name.protocol('WM_DELETE_WINDOW', reset_count_win_game)

        root_name.mainloop()
    else :
        messagebox.showinfo("Error","You already opened a game window!\n\nClose the open one first...")


# Defining a function that opens the Player 1 vs. Player 2 mode window:
def open_mode_jcj(name1, name2):
    '''
    Procedure that defines what happens if the user presses the "Player vs. Player" button.

    A new game window is created only if it is not already open.

    The procedure then calls other functions to display all the elements essential to the game!
    '''
    global nb_allumettes, count_x, count_window_open, root_jcj
    if count_window_open == 0 :
        root_jcj = Toplevel(root)
        root_jcj.title("Game between two players")
        root_jcj.geometry("1080x720")
        root_jcj.minsize(1080, 720)
        root_jcj.maxsize(1080, 720)
        count_window_open+=1
        # Import and display a background image:
        canvas_jcj = Canvas(root_jcj, width = 1080, height = 720)
        canvas_jcj.pack(fill = "both", expand = True)
        bg3 = ImageTk.PhotoImage(file = "img\Background_IMAGE.png")
        canvas_jcj.create_image( 0, 0, image = bg3, anchor = "nw")
        root_jcj.protocol('WM_DELETE_WINDOW', reset_count_win_game)
        crea_button(root_jcj,canvas_jcj, name1, name2)
        spawn_allumettes(canvas_jcj, name1)
        appelle_joueur(canvas_jcj, name1, name2)
    else :
        messagebox.showinfo("Error","You already opened a game window!\n\nClose the open one first...") 


def select_difficult():
    '''
    Procedure that creates the choice window that appears on the screen if the user presses "Player Against Robot".

    Apply a background image, etc.
    Then we call the function that implements all the essential elements for the choice (buttons, titles, etc.)
    '''
    global count_window_open, root_selection
    if count_window_open == 0 :
        root_selection = Toplevel(root)
        root_selection.title("Please select your level of difficulty...")
        root_selection.geometry("1080x720")
        root_selection.minsize(1080, 720)
        root_selection.maxsize(1080, 720)
        count_window_open+=1
        # Import and display a background image:
        canvas_selection = Canvas(root_selection, width = 1080, height = 720)
        canvas_selection.pack(fill = "both", expand = True)
        bg6 = ImageTk.PhotoImage(file = "img\Background_IMAGE.png")
        canvas_selection.create_image( 0, 0, image = bg6, anchor = "nw")
        selection_button(root_selection, canvas_selection)
        root_selection.protocol('WM_DELETE_WINDOW', reset_count_win_game)
        mainloop()
    else :
        messagebox.showinfo("Error","You already opened a game window!\n\nClose the open one first...")

def selection_button(root_menu, canvas):
    '''
    Function that defines the elements of the choice window that appears on the screen if the user presses "Player Vs Robot"
    '''
    q=canvas.create_text(540.45, 200, text='Please select the difficulty level of the robot:', font=("Helvetica", 34), fill="white")
    s=canvas.create_rectangle(canvas.bbox(q),fill="#00bdfb")
    canvas.tag_lower(s,q)
    button_simple = Button(root_menu, text="Easy", command=lambda *args:open_mode_jco_simple(root_menu), font=("Helvetica", 50), fg='white', bg="#00bdfb", height = 2, width = 10)
    canvas.create_window(100, 320, anchor='nw', window=button_simple)
    button_difficile = Button(root_menu, text="Difficult", command=lambda *args:open_mode_jco_difficile(root_menu), font=("Helvetica", 50), fg='white', bg="#00bdfb", height = 2, width = 10)
    canvas.create_window(600, 320, anchor='nw', window=button_difficile)


# Defining a function that opens the Computer vs. Computer mode window:
def open_mode_oco():
    '''
    Procedure that defines what happens if the user presses the "Computer vs. Computer" button.

    A new game window is created only if it is not already open.

    The procedure then calls other functions to display all the elements essential to the game!
    '''
    global count_window_open, root_oco
    if count_window_open == 0 :
        root_oco = Toplevel(root)
        root_oco.title("Game between two computers")
        root_oco.geometry("1080x720")
        root_oco.minsize(1080, 720)
        root_oco.maxsize(1080, 720)
        count_window_open+=1
        # Import and display a background image:
        canvas_oco = Canvas(root_oco, width = 1080, height = 720)
        canvas_oco.pack(fill = "both", expand = True)
        bg5 = ImageTk.PhotoImage(file = "img\Background_IMAGE.png")
        canvas_oco.create_image( 0, 0, image = bg5, anchor = "nw")
        root_oco.protocol('WM_DELETE_WINDOW', reset_count_win_game)
        appelle_robot_oco(canvas_oco, root_oco)

        if player1 == " Player 1 " or player1 == None:
            name_robot_1 = " Marcus "
        else :
            name_robot_1 = player1
        spawn_allumettes(canvas_oco, name_robot_1)
    else :
        messagebox.showinfo("Error","You already opened a game window!\n\nClose the open one first...")

def msg_remerciment() :
    '''
    Procedure that displays a thank you message to the user if he finishes his game or quits the game by closing the window.
    '''
    messagebox.showinfo("THANK YOU !","Thank you so much for playing my game!\n\n Drawings: Maéva LE GROS\n Development: Romain MELLAZA")
    root.destroy()


# Add a button to open the game rules:
button_rgl = Button(root, text="The game's rules", command=open_regles, font=("Helvetica", 14), fg='white', bg="#00bdfb", height = 2, width = 18)
button_rgl_window = canvas_accueil.create_window(855, 640, anchor='nw', window=button_rgl)

# Add the different buttons to select the game mode:

button_jcj = Button(root, text="Player 1 versus Player 2", command=switch_jcj, font=("Helvetica", 20), fg='white', bg="#00bdfb", height = 2, width = 22)
button_jcj_window = canvas_accueil.create_window(100, 400, anchor='nw', window=button_jcj)

button_jco = Button(root, text="Player versus Computer", command=select_difficult, font=("Helvetica", 20), fg='white', bg="#00bdfb", height = 2, width = 22)
button_jco_window = canvas_accueil.create_window(640, 400, anchor='nw', window=button_jco)

button_oco = Button(root, text="Computer versus Computer", command=open_mode_oco, font=("Helvetica", 20), fg='white', bg="#00bdfb", height = 2, width = 22)
button_oco_window = canvas_accueil.create_window(375, 520, anchor='nw', window=button_oco)











##############################################################################################################################################################################################################
#                                                                                     PLAYER VS PLAYER MODE                                                                                                  #
#                                                                                                                                                                                                            #

# Definition of a function that creates the buttons to take matches:
def crea_button(racine,canvas, name1, name2):
    '''
    Function that receives the window ("root") as well as the canvas ("canvas") where it must implement buttons to choose the number of matches that the user takes.

    Each button press then invokes a related match delete function.

    It returns the characteristics and the location of the buttons on the canvas.
    '''
    global button1, button2, button3
    v=canvas.create_text(540, 525, text="How many match(es) do you take?",font=("Helvetica", 35), fill="white")
    w=canvas.create_rectangle(canvas.bbox(v),fill="#00bdfb")
    canvas.tag_lower(w,v)
    button1 = Button(racine, text="1 match", command=lambda *args: suppr_allum(1, canvas, racine, name1, name2), font=("Helvetica", 14), fg='white', bg="#00bdfb", height = 2, width = 18)
    button1_window = canvas.create_window(75, 560, anchor='nw', window=button1)
    button2 = Button(racine, text="2 matches", command=lambda *args: suppr_allum(2, canvas, racine, name1, name2), font=("Helvetica", 14), fg='white', bg="#00bdfb", height = 2, width = 18)
    button2_window = canvas.create_window(430, 560, anchor='nw', window=button2)
    button3 = Button(racine, text="3 matches", command=lambda *args: suppr_allum(3, canvas, racine, name1, name2), font=("Helvetica", 14), fg='white', bg="#00bdfb", height = 2, width = 18)
    button3_window = canvas.create_window(780, 560, anchor='nw', window=button3)
    return button1_window, button2_window, button3_window


def spawn_allumettes(canvas, first_name=" You "):
    '''
    Function that receives as a parameter the canvas where it must display the images of matches.

    Note that I also use this function for all modes except computer against computer!

    It imports the image and displays it in several positions in the window, it puts all the data about the match images in an "allum_list".
    '''
    global allum_list, first_label, second_label
    first_label=canvas.create_text(540, 450, text=first_name,font=("Helvetica", 40), fill="blue")
    second_label=canvas.create_rectangle(canvas.bbox(first_label),fill="white")
    canvas.tag_lower(second_label, first_label)
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


def suppr_allum(number, canvas_allum, root_correspondant, name1, name2):
    '''
    Quite complex function which accepts as a parameter the number of matches to be deleted "number" according to the button pressed (1 or 2 or 3)
    as well as the canvas of the current game mode "canvas_allum" (where are therefore the images of matches to be deleted) and finally the corresponding window "root_correspondant"
    
    The function subtracts the number of matches taken from the number of matches remaining on the table.
    It then calls the player who must play this turn using the "appelle_joueur()" function

    Depending on the number of remaining matches, the buttons to take more than possible are automatically deactivated!

    Depending on the number of matches taken, the program deletes the correct number of corresponding images.

    If there are no matches left on the table, the program informs the current player of his defeat, closes the game window, resets all values, 
    so players can play again without closing the game completely!

    If the user manually closes the game, the thank you message is displayed!
    '''
    global nb_allumettes, count_x, count_player, count_window_open, allum_list
    nb_allumettes = nb_allumettes - number
    appelle_joueur(canvas_allum, name1, name2)
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
        messagebox.showinfo("Lost ! :(","You took the last match, too bad...")
        root_correspondant.destroy()
        nb_allumettes = 21
        count_x = 0
        count_player = 2
        count_window_open = 0
    root_correspondant.protocol('WM_DELETE_WINDOW', reset_count_win_game)



def appelle_joueur(canvas, name1, name2):
    '''
    Function that admits the canvas of the current game mode "canvas" to display the player whose turn 
    it's according to the turn counter "count_player" (if it's even or odd).
    '''
    global count_player, e, r, d, f
    if count_player % 2 == 1 :
        try:
            canvas.delete(d)
            canvas.delete(f)
        except:
            pass

        e=canvas.create_text(540, 450, text=name1, font=("Helvetica", 40), fill="blue")
        r=canvas.create_rectangle(canvas.bbox(e),fill="white")
        canvas.tag_lower(r, e)
    if count_player % 2 == 0 :
        try :
            canvas.delete(first_label)
            canvas.delete(second_label)
        except :
            pass

        try:
            canvas.delete(e)
            canvas.delete(r)
        except :
            pass

        d=canvas.create_text(540, 450, text=name2, font=("Helvetica", 40), fill="red")
        f=canvas.create_rectangle(canvas.bbox(d),fill="white")
        canvas.tag_lower(f, d)





##############################################################################################################################################################################################################
#                                                                                PLAYER VS COMPUTER MODE (DIFFICULTY = SIMPLE)                                                                               #
#                                                                                                                                                                                                            #


# Definition of a function that creates the buttons to take matches:
def crea_button_robot_simple(racine,canvas):
    '''
    Function that receives the window ("racine") as well as the canvas ("canvas") where it must implement buttons to choose the number of matches that the user takes.

    Each button press then invokes a related match delete function.

    It returns the characteristics and the location of the buttons on the canvas.

    The only difference with the classic function is that the robot may not systematically call it because it goes directly through the deletion, and obviously does not press any button!
    '''
    global button1, button2, button3
    v=canvas.create_text(540, 525, text="How many match(es) do you take?",font=("Helvetica", 35), fill="white")
    w=canvas.create_rectangle(canvas.bbox(v),fill="#00bdfb")
    canvas.tag_lower(w,v)
    button1 = Button(racine, text="1 match", command=lambda *args: suppr_allum_robot_simple(1, canvas, racine), font=("Helvetica", 14), fg='white', bg="#00bdfb", height = 2, width = 18)
    button1_window = canvas.create_window(75, 560, anchor='nw', window=button1)
    button2 = Button(racine, text="2 matches", command=lambda *args: suppr_allum_robot_simple(2, canvas, racine), font=("Helvetica", 14), fg='white', bg="#00bdfb", height = 2, width = 18)
    button2_window = canvas.create_window(430, 560, anchor='nw', window=button2)
    button3 = Button(racine, text="3 matches", command=lambda *args: suppr_allum_robot_simple(3, canvas, racine), font=("Helvetica", 14), fg='white', bg="#00bdfb", height = 2, width = 18)
    button3_window = canvas.create_window(780, 560, anchor='nw', window=button3)
    return button1_window, button2_window, button3_window


# I also use the "spawn_allumettes" function seen above.


def suppr_allum_robot_simple(number, canvas_allum, root_correspondant):
    '''
    Quite complex function which accepts as a parameter the number of matches to be deleted "number" according to the button pressed (1 or 2 or 3)
    as well as the canvas of the current game mode "canvas_allum" (where are therefore the images of matches to be deleted) and finally the corresponding window "root_correspondant"
    
    The function subtracts the number of matches taken from the number of matches remaining on the table.
    It then calls the player or the robot which must play this turn using the "appelle_robot()" function

    Depending on the number of remaining matches, the buttons to take more than possible are automatically deactivated!

    Depending on the number of matches taken, the program deletes the correct number of corresponding images.

    If there are no matches left on the table, the program informs the current player of his defeat, closes the game window, resets all values, 
    so players can play again without closing the game completely!

    If the user manually closes the game, the thank you message is displayed!

    The only difference with the classic function is that the function calls the robot every other time and not two players!
    '''
    global nb_allumettes, count_x, count_player, count_window_open
    nb_allumettes = nb_allumettes - number
    appelle_robot(canvas_allum, root_correspondant)
    if nb_allumettes == 3 :
        button3['state'] = DISABLED
    elif nb_allumettes == 2 :
        button3['state'] = DISABLED
        button2['state'] = DISABLED
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
            messagebox.showinfo("Lost ! :(","You have to take the last match, too bad...")
            reset_count_win_game()
    elif number == 2:
        canvas_allum.delete(allum_list[count_x])
        count_x+=1
        canvas_allum.delete(allum_list[count_x])
        count_x+=1
        count_player+=1
        if nb_allumettes == 1 :
            messagebox.showinfo("Lost ! :(","You have to take the last match, too bad...")
            reset_count_win_game()
    elif number == 1:
        canvas_allum.delete(allum_list[count_x])
        count_x+=1
        count_player+=1
        if nb_allumettes == 1 :
            messagebox.showinfo("Lost ! :(","You have to take the last match, too bad...")
            reset_count_win_game()
    root_correspondant.protocol('WM_DELETE_WINDOW', reset_count_win_game)



def appelle_robot(canvas, root_correspondant):
    '''
    Function that admits the canvas of the current game mode "canvas" to display there the player or the robot whose turn 
    it's to play according to the turn counter "count_player" (if it is even or odd).

    When it's up to the robot to play, it deactivates all the buttons so that the player doesn't play instead! (and vice versa)

    The robot takes matches randomly until there are only 3 or less left, to prevent it from playing "crazy"

    (See comments directly in the code to understand the logic)
    '''
    global count_player, nb_robot, count_x, count_window_open, d, f, e, r
    if count_player % 2 == 1 :
        try :
            canvas.delete(d)
            canvas.delete(f)
        except:
            pass

        button1['state'] = NORMAL               # VERY useful command that allows you to change the state of the buttons
        button2['state'] = NORMAL
        button3['state'] = NORMAL
        e=canvas.create_text(540, 450, text=" You ",font=("Helvetica", 40), fill="blue")
        r=canvas.create_rectangle(canvas.bbox(e),fill="white")
        canvas.tag_lower(r, e)
    if count_player % 2 == 0 :
        try :
            canvas.delete(first_label)
            canvas.delete(second_label)
        except :
            pass

        try :
            canvas.delete(e)
            canvas.delete(r)
        except :
            pass

        d=canvas.create_text(540, 450, text=" ROBOT ",font=("Helvetica", 40), fill="red")
        f=canvas.create_rectangle(canvas.bbox(d),fill="white")
        canvas.tag_lower(f, d)
        button1['state'] = DISABLED
        button2['state'] = DISABLED
        button3['state'] = DISABLED
        nb_robot=randint(1,3)               # I determine in a completely random way the number of matches taken by the robot
        while nb_robot > nb_allumettes :    # BUT BE CAREFUL if the robot wants to take more matches than there are on the table then it redetermines a random value until the condition is false and the program exits the loop
            nb_robot=randint(1,3)
        if nb_allumettes == 3 :             # If there are 3 matches left on the table, then the robot takes 2 to trap the player
            nb_robot = 2
        elif nb_allumettes == 2 :           # If there are 2 matches left on the table, then the robot takes 1 to trap the player
            nb_robot = 1
        elif nb_allumettes == 1 :           # If there is only one match left then the robot is obliged to take it and concede defeat... I close the game afterwards.
            messagebox.showinfo("Won ! :)","The robot is forced to take the last match, well done!")
            reset_count_win_game()
        canvas.after(3000, suppr_allum_robot_simple, nb_robot, canvas, root_correspondant)      # This function allows you to execute the "suppr_allum_robot_simple()" function seen just above after 3000ms and with my number which has just been determined, as an argument.


# Defining a function that opens the Player 1 mode window against a Computer (difficulty: simple):
def open_mode_jco_simple(root_precedent):
    '''
    Function that accepts the difficulty selection window as a parameter in order to be able to delete it just after it is given birth to this one!

    A new game window is created only if it is not already open.

    Basic settings are applied.

    The function then calls other functions to display all the elements essential to the game!
    '''
    global root_jco_simple
    root_precedent.destroy()
    root_jco_simple = Toplevel(root)
    root_jco_simple.title("Game between a player and a computer (difficulty = simple)")
    root_jco_simple.geometry("1080x720")
    root_jco_simple.minsize(1080, 720)
    root_jco_simple.maxsize(1080, 720)
    # Importer et afficher une image de fond :
    canvas_jco_simple = Canvas(root_jco_simple, width = 1080, height = 720)
    canvas_jco_simple.pack(fill = "both", expand = True)
    bg4 = ImageTk.PhotoImage(file = "img\Background_IMAGE.png")
    canvas_jco_simple.create_image( 0, 0, image = bg4, anchor = "nw")
    root_jco_simple.protocol('WM_DELETE_WINDOW', reset_count_win_game)
    crea_button_robot_simple(root_jco_simple, canvas_jco_simple)
    spawn_allumettes(canvas_jco_simple)



##############################################################################################################################################################################################################
#                                                                                      PLAYER VS COMPUTER MODE (DIFFICULTY = HARD)                                                                           #
#                                                                                                                                                                                                            #



def crea_button_robot_difficile(racine,canvas):
    '''
    Function that receives the window ("root") as well as the canvas ("canvas") where it must implement buttons to choose the number of matches that the user takes.

    Each button press then invokes a related match delete function.

    It returns the characteristics and the location of the buttons on the canvas.

    The only difference with the classic function is that the robot may not systematically call it because it goes directly through the deletion, and obviously does not press any button!
    '''
    global button1, button2, button3
    v=canvas.create_text(540, 525, text="How many match(es) do you take?",font=("Helvetica", 35), fill="white")
    w=canvas.create_rectangle(canvas.bbox(v),fill="#00bdfb")
    canvas.tag_lower(w,v)
    button1 = Button(racine, text="1 match", command=lambda *args: suppr_allum_robot_difficile(1, canvas, racine), font=("Helvetica", 14), fg='white', bg="#00bdfb", height = 2, width = 18)
    button1_window = canvas.create_window(75, 560, anchor='nw', window=button1)
    button2 = Button(racine, text="2 matches", command=lambda *args: suppr_allum_robot_difficile(2, canvas, racine), font=("Helvetica", 14), fg='white', bg="#00bdfb", height = 2, width = 18)
    button2_window = canvas.create_window(430, 560, anchor='nw', window=button2)
    button3 = Button(racine, text="3 matches", command=lambda *args: suppr_allum_robot_difficile(3, canvas, racine), font=("Helvetica", 14), fg='white', bg="#00bdfb", height = 2, width = 18)
    button3_window = canvas.create_window(780, 560, anchor='nw', window=button3)
    return button1_window, button2_window, button3_window


def suppr_allum_robot_difficile(number, canvas_allum, root_correspondant):
    '''
    Fairly complex function that accepts as a parameter the number of matches to be removed "number" depending on the button pressed (1 or 2 or 3) as well as the canvas of the current game mode "canvas_allum" (where are the images of matches to delete) 
    and finally the corresponding window "root_correspondant"
    
    The function subtracts the number of matches taken from the number of matches remaining on the table.
    It then calls the player or the robot which must play this turn using the "appelle_robot()" function

    Depending on the number of remaining matches, the buttons to take more than possible are automatically deactivated!

    Depending on the number of matches taken, the program deletes the correct number of corresponding images.

    If there are no matches left on the table, the program informs the current player of his defeat, closes the game window, resets all values, 
    so players can play again without closing the game completely!

    If the user manually closes the game, the thank you message is displayed!

    The only difference with the classic function is that the function calls the robot every other time and not two players!
    '''
    global nb_allumettes, count_x, count_player, count_window_open
    nb_allumettes = nb_allumettes - number
    appelle_robot_difficile(canvas_allum, root_correspondant)
    if nb_allumettes == 3 :
        button3['state'] = DISABLED
    elif nb_allumettes == 2 :
        button3['state'] = DISABLED
        button2['state'] = DISABLED
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
            messagebox.showinfo("Lost ! :(","You have to take the last match, too bad...")
            reset_count_win_game()
    elif number == 2:
        canvas_allum.delete(allum_list[count_x])
        count_x+=1
        canvas_allum.delete(allum_list[count_x])
        count_x+=1
        count_player+=1
        if nb_allumettes == 1 :
            messagebox.showinfo("Lost ! :(","You have to take the last match, too bad...")
            reset_count_win_game()
    elif number == 1:
        canvas_allum.delete(allum_list[count_x])
        count_x+=1
        count_player+=1
        if nb_allumettes == 1 :
            messagebox.showinfo("Lost ! :(","You have to take the last match, too bad...")
            reset_count_win_game()

    root_correspondant.protocol('WM_DELETE_WINDOW', reset_count_win_game)



def appelle_robot_difficile(canvas, root_correspondant):
    '''
    Function that admits the canvas of the current game mode "canvas" to display there the player or the robot whose turn 
    it's to play according to the turn counter "count_player" (if it is even or odd).

    When it's up to the robot to play, it deactivates all the buttons so that the player doesn't play instead! (and vice versa)

    The robot here picks matches algorithmically, and logically

    (See comments directly in the code to understand the logic)
    '''
    global count_player, nb_robot, count_x, count_window_open
    if count_player % 2 == 1 :
        try :
            canvas.delete(d)
            canvas.delete(f)
        except:
            pass
        
        button1['state'] = NORMAL
        button2['state'] = NORMAL
        button3['state'] = NORMAL
        e=canvas.create_text(540, 450, text=" You ",font=("Helvetica", 40), fill="blue")
        r=canvas.create_rectangle(canvas.bbox(e),fill="white")
        canvas.tag_lower(r, e)

    if count_player % 2 == 0 :
        try :
            canvas.delete(first_label)
            canvas.delete(second_label)
        except :
            pass

        try :
            canvas.delete(e)
            canvas.delete(r)
        except :
            pass

        d=canvas.create_text(540, 450, text=" ROBOT ",font=("Helvetica", 40), fill="red")
        f=canvas.create_rectangle(canvas.bbox(d),fill="white")
        canvas.tag_lower(f, d)
        button1['state'] = DISABLED
        button2['state'] = DISABLED
        button3['state'] = DISABLED
        if nb_allumettes % 4 == 3:                  # Here unlike the simple difficulty, I algorithmically determine the number of matches that the robot must take to be sure to win!
            nb_robot = 2
        elif nb_allumettes % 4 == 2:
            nb_robot = 1
        elif nb_allumettes % 4 == 0:
            nb_robot = 3
        else:
            nb_robot = 1
        if nb_allumettes == 1 :
            messagebox.showinfo("Won ! :)","The robot is forced to take the last match, well done!")
            reset_count_win_game()
        canvas.after(3000, suppr_allum_robot_difficile, nb_robot, canvas, root_correspondant)             # This function allows you to execute the "suppr_allum_robot_simple()" function seen just above after 3000ms and with my number which has just been determined, as an argument.


# Defining a function that opens the Player 1 mode window against a Computer:
def open_mode_jco_difficile(root_precedent):
    '''
    Function that accepts the difficulty selection window as a parameter in order to be able to delete it just after it is given birth to this one!

    A new game window is created only if it is not already open.

    Basic settings are applied.

    The function then calls other functions to display all the elements essential to the game!
    '''
    global root_jco_difficile
    root_precedent.destroy()
    root_jco_difficile = Toplevel(root)
    root_jco_difficile.title("Game between a player and a computer (difficulty = difficult)")
    root_jco_difficile.geometry("1080x720")
    root_jco_difficile.minsize(1080, 720)
    root_jco_difficile.maxsize(1080, 720)
    # Importer et afficher une image de fond :
    canvas_jco_difficile = Canvas(root_jco_difficile, width = 1080, height = 720)
    canvas_jco_difficile.pack(fill = "both", expand = True)
    bg4 = ImageTk.PhotoImage(file = "img\Background_IMAGE.png")
    canvas_jco_difficile.create_image( 0, 0, image = bg4, anchor = "nw")
    root_jco_difficile.protocol('WM_DELETE_WINDOW', reset_count_win_game)
    crea_button_robot_difficile(root_jco_difficile,canvas_jco_difficile)
    spawn_allumettes(canvas_jco_difficile)




##############################################################################################################################################################################################################
#                                                                                  COMPUTER VERSUS COMPUTER MODE                                                                                             #
#                                                                                                                                                                                                            #



def suppr_allum_robot_simple_oco(number, canvas_allum, root_correspondant):
    '''
    Fairly complex function that accepts as a parameter the number of matches to be removed "number" depending on the button pressed (1 or 2 or 3) as well as the canvas of the current game mode "canvas_allum" (where are the images of matches to delete) 
    and finally the corresponding window "root_correspondant"

    The function subtracts the number of matches taken from the number of matches remaining on the table.
    It then calls the robot which must play this turn using the "call_robot_oco()" function

    Depending on the number of remaining matches, the buttons to take more than possible are automatically deactivated!

    Depending on the number of matches taken, the program deletes the correct number of corresponding images.

    If there are no matches left on the table, the program informs the current player of his defeat, closes the game window, resets all values, 
    so players can play again without closing the game completely!

    If the user manually closes the game, the thank you message is displayed!

    The only difference with the classic function is that the function calls two robots and not two players (who should therefore click)!
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

    root_correspondant.protocol('WM_DELETE_WINDOW', reset_count_win_game)



def appelle_robot_oco(canvas, root_correspondant):
    '''
    Function that admits the canvas of the current game mode "canvas" to display the robot Donald or the robot Marcus whose turn it is to play 
    according to the turn counter "count_player" (if it is even or odd).

    When it's up to the robot to play, it deactivates all the buttons so that the player doesn't play instead! (and vice versa)

    The robots here have exactly the same logic as in the jco's simple difficulty mode, i.e. random until there are only 3 matches left

    (See comments directly in the code to understand the logic)
    '''
    global count_player, nb_robot, vava, wiwi, sexy, girl

    if player1 == " Player 1 " or player1 == None:
        name_robot_1 = " Marcus "
    else :
        name_robot_1 = player1
    
    if player2 == " Player 2 " or player2 == None:
        name_robot_2 = " Donald "
    else :
        name_robot_2 = player2

    if count_player % 2 == 1 :
        try :
            canvas.delete(sexy)
            canvas.delete(girl)
        except :
            pass

        vava=canvas.create_text(540, 450, text=name_robot_1,font=("Helvetica", 40), fill="blue")
        wiwi=canvas.create_rectangle(canvas.bbox(vava),fill="white")
        canvas.tag_lower(wiwi, vava)
        nb_robot=randint(1,3)
        while nb_robot > nb_allumettes :
            nb_robot=randint(1,3)
        if nb_allumettes == 3 :
            nb_robot = 2
        elif nb_allumettes == 2 :
            nb_robot = 1
        elif nb_allumettes == 1 :
            text_msg_1 = "I LOST, well done" + name_robot_2 + "!"
            messagebox.showinfo("FINISHED !",text_msg_1)                 # So I can know which robot won and therefore which robot lost!
            reset_count_win_game()
        canvas.after(1500, suppr_allum_robot_simple_oco, nb_robot, canvas, root_correspondant)      # This function allows you to execute the "suppr_allum_robot_simple_oco()" function seen just above after 1500ms and with my number which has just been determined, as an argument.
    if count_player % 2 == 0 :
        try :
            canvas.delete(first_label)
            canvas.delete(second_label)
        except :
            pass

        try :
            canvas.delete(vava)
            canvas.delete(wiwi)
        except :
            pass
        
        sexy=canvas.create_text(540, 450, text=name_robot_2,font=("Helvetica", 40), fill="red")
        girl=canvas.create_rectangle(canvas.bbox(sexy),fill="white")
        canvas.tag_lower(girl, sexy)
        nb_robot=randint(1,3)
        while nb_robot > nb_allumettes :
            nb_robot=randint(1,3)
        if nb_allumettes == 3 :
            nb_robot = 2
        elif nb_allumettes == 2 :
            nb_robot = 1
        elif nb_allumettes == 1 :
            text_msg_2 = "I LOST, well done" + name_robot_1 + "!"
            messagebox.showinfo("FINISHED !",text_msg_2)                 # So I can know which robot won and therefore which robot lost!
            reset_count_win_game()
        canvas.after(1500, suppr_allum_robot_simple_oco, nb_robot, canvas, root_correspondant)      # This function allows you to execute the "suppr_allum_robot_simple_oco()" function seen just above after 1500ms and with my number which has just been determined, as an argument.



    


# If the user closes the homepage, it displays the thank you message:
root.protocol('WM_DELETE_WINDOW', msg_remerciment)


# I continuously refresh my application via this command:
root.mainloop()