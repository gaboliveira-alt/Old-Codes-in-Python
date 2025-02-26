from random import shuffle


class MemoryCard:
    def __init__(self, value,):
        self.value = value
        self.__is_matched = False
    
    def __str__(self):
        if self.__is_matched:
            return f'{self.value}'
        return "*"
    
    def __repr__(self):
       return str(self)
           
    def match(self):
        self.__is_matched = True
    
    def matched_card(self):
        return self.__is_matched

class MemoryGame:
    def __init__(self):
        self.cards = []
        
    def start(self, quantity):
        if quantity < 1:
            raise ValueError(f'Invalid Number: {quantity}')
        
        self.cards = [MemoryCard(cards) for cards in range(1, quantity + 1) for _ in range(2)]
        shuffle(self.cards)

    def play(self, index1, index2):
        if not(0 <= index1 < len(self.cards)) or not(0 <= index2 < len(self.cards)):
            raise IndexError("Index out of range")
        
        card1 = self.cards[index1]
        card2 = self.cards[index2]
        
        if card1.value == card2.value:
            card1.match()
            card2.match()
            print("Cards combinam")
            return True
        print("Cards não combinam")
        return False
    
    def is_game_over(self):
        return all(cards.matched_card for cards in self.cards)
    
    def show_cards(self):
        return " ".join([str(cards) for cards in self.cards])

def main():
    memory_game = MemoryGame()

    quantity_cards = int(input("\n Com quantas cartas voce deseja começar?\n"))
    memory_game.start(quantity_cards)
    print(memory_game.show_cards())
    
if __name__ == '__main__':
    main()
    
    
    





