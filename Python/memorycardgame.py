from random import shuffle, sample

class MemoryCard:
    def __init__(self, value):
        self.__value = value
        self.__is_matched = False
    
    def __str__(self):
        return str(self.__value) if self.__is_matched else '*'
    
    def __repr__(self):
        return str(self)
    
    def match(self):
        self.__is_matched = True
    
    def get_value(self):
        return self.__value
    
    def is_matched(self):
        return self.__is_matched

class MemoryGame:
    def __init__(self):
        self.cards = []
    
    def start(self, quantity):
        self.cards = []
        
        for number in range(quantity):
            self.cards.append(MemoryCard(number + 1))
            self.cards.append(MemoryCard(number + 1))
        shuffle(self.cards)
    
    def play(self, index1, index2):
        card1 = self.cards[index1]
        card2 = self.cards[index2]
        
        if card1.is_matched() or card2.is_matched():
            return False
        
        if card1.get_value() == card2.get_value():
            card1.match()
            card2.match()
            return True
        
        return None
    
    def random_pair(self):
        unmatched_indexes = [index for index, card in enumerate(self.cards) if not card.is_matched()]
        
        return tuple(sample(unmatched_indexes, 2))
    
    def is_game_over(self):
        for card in self.cards:
            if not card.is_matched():
                return False
        return True
    
    def show_cards(self):
        for cards in self.cards:
            print(f'{str(cards):^5}', end='')
        print()
        
def main():
    game = MemoryGame()
    
    game.start(5)
    game.show_cards()
    
    while not game.is_game_over():
        index1, index2 = game.random_pair()
        game.play(index1, index2)
        print(f'({index1},{index2})', end='\t')
        game.show_cards()


if __name__ == '__main__':
    main()        