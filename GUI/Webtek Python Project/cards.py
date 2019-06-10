#Deck
deck = []

def makeDeck():

    suits = ["Spades","Diamonds","Hearts","Clubs"]
    
    for suit in suits:
        for value in range(2,14):
            if value == 11:
                a = "Jacks"
                deck.append(a +" of "+suit)
            elif value == 12:
                a = "Queens"
                deck.append(a +" of "+suit)
            elif value == 13:
                a = "Kings"
                deck.append(a +" of "+suit)
            else:
                deck.append(str(value) +" of "+ suit )
    deck.append("Ace")
   
    




