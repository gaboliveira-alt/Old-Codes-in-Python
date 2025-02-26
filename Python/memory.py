
from random import shuffle


class MemoryCard:
    def __init__(self, value):
        self.value = value
        self.is_matched = False

    def __str__(self):
        if self.is_matched:
           return f'{self.value}'
        return "*"

    def match(self):
        self.is_matched = True


class MemoryGame:
    def __init__(self):
        self.cards = []

    def Start(self, quantity):
        cards = list(range(1, quantity + 1)) * 2
        shuffle(cards)
        self.cards = [MemoryCard(value) for value in cards]

    def Play(self, index1, index2):
        card1 = self.cards[index1]
        card2 = self.cards[index2]

        if index2 == index1:
            print("A segunda carta tem que ser diferente da primeira")
            return

        if card1.value == card2.value:
            card1.match()
            card2.match()
            print(f"Par encontrado: {card1.value}")
        else:
            print("Cards Não combinam.")

    def is_game_over(self):
        return all(card.is_matched for card in self.cards)

    def show_cards(self):
        print(" ".join(str(card) for card in self.cards))


def main():

    game = MemoryGame()
    game.Start(10)
    while not game.is_game_over():
        game.show_cards()
        print("Escolha duas cartas de 0 a 19")
        index1 = int(input("Escolha a primeira carta: "))
        index2 = int(input("Escolha a segunda carta: "))
        game.Play(index1, index2)
    print("Parabéns! Você encontrou todos os pares!")

if __name__ == '__main__':
    main()
