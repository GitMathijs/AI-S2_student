class Card:
    def __init__(self, suit="Spades", value="Ace"):
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return f"{self.value} of {self.suit}"
    
    def __eq__(self, other):
        return self.value == other.value
    
    def __gt__(self, other):
        order = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
        return order.index(self.value) > order.index(other.value)
    
    def __ge__(self, other):
        order = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
        return order.index(self.value) >= order.index(other.value)


class Drawpile:
    def __init__(self, cards=[]): # unpacker?
        self.cards = cards
    
    def __repr__(self):
        string = ""
        for card in self.cards:
            string += card.__repr__() + ", "
        string = string[:-2]
        return string


    def __len__(self):
        return len(self.cards)
    
    def __getitem__(self, index):
        return self.cards[index]
    
    def add(self, card):
        self.cards.append(card)

    def draw(self):
        return self.cards.pop(0)


card = Card("Hearts", 4)
card2 = Card("Clubs", 4)
card3 = Card("Diamonds", "Jack")
card4 = Card(value="King")

pile = Drawpile([card, card2, card3])
print(len(pile))
pile.add(card4)
print(len(pile))
print(pile.draw())
print(pile)