from tkinter.messagebox import RETRY


class Lingo:
    def __init__(self):
        self.woord= str.lower("lingo")
        self.beurt = 1

    def validate_input(self, invoer):
        
        self.beurt += 1

        invoer = str.lower(invoer)

        #kijk of het woord goed is.
        if (invoer == self.woord):
            return "Gewonnen"

        #Test lengte van de letters
        if(len(invoer) != 5):
            return "Voer een woord in van 5 letters!"

        #Vergelijk elke letter van de invoer
        uitvoer = ""
        for i in range(5):
            if (invoer[i] == self.woord[i]):
                uitvoer += str.upper(invoer[i])
            elif (invoer [i] in self.woord):
                uitvoer += invoer[i]
            else:
                uitvoer += "_"
        return uitvoer



