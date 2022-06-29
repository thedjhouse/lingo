from tkinter import *
from lingo import Lingo

lingo = Lingo()

invoervelden = {}

def validate(event):
    print("beurt: " + str(lingo.beurt))
    print("woord: " + lingo.woord)
    
    invoer = invoervelden[lingo.beurt-1].get()
    print("ingevoerd: " + invoer)
    
    uitvoer = lingo.validate_input(invoer)
    print("resultaat: " + uitvoer)

    invoervelden[lingo.beurt-2].insert(END, " > " + uitvoer)

    status_label.config(text = uitvoer)

    beurten_label.config(text = str(lingo.beurt) + "/5")


# Main
app = Tk()
app.title("Lingo!")
app.geometry("300x400")
app.resizable(False, False)

# Titel
titel_label = Label(app, text = "Welkom bij Lingo!", font=("Arial", 18, "bold"))
titel_label.pack()
# stopwatch
stopwatch_label = Label(app, text = "Stopwatch", font=("Arial", 12, "bold"))
stopwatch_label.pack()
# stopwatch logic
stopwatch_logic = Label(app, text = "", font=("Arial", 12, "bold"))
stopwatch_logic.pack()

# Uitleg
intro_label = Label(app, text = "Raad het woord van 5 letters in 5 beurten.")
intro_label.pack()

# Status
status_label = Label(app, text = "Succes!", font=("Arial", 14, "bold"), fg = 'red')
status_label.pack()

# Aantal beurten
beurten_label = Label(app, text = "1/5", font=("Arial", 20, "bold"))
beurten_label.pack()

# Invoervelden
for r in range(5):
    invoerveld = Entry(app, bg='#3366cc', justify=LEFT, font=('arial', 24, 'bold'), fg='white')
    invoerveld.pack()
    invoervelden[r] = invoerveld
    invoerveld.bind('<Return>', validate)

# Run
app.mainloop()

