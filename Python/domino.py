from random import shuffle, randint

class DominoTile:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
    
    def __str__(self):
        return f'({self.number1},{self.number2})'
    
    def __repr__(self):
        return str(self)
    
    def is_flipped(self):
        self.number1, self.number2 = self.number2, self.number1
    
    def is_double(self):
        return self.number1 == self.number2

class DominoSet:
    def __init__(self, tiles = []):
        if tiles:
            if not all(isinstance(tile, DominoTile) for tile in self.tiles):
                raise TypeError(f'Arguments tiles must be a list of DominoTile')
            self.tiles = tiles
        else:
            self.tiles = []
    
    def clear(self):
        self.tiles.clear()
    
    def generate_tiles(self):
        self.tiles = []
        
        self.tiles = [DominoTile(n1, n2) for n1 in range(0, 7) for n2 in range(n1, 7)]
    
    def shuffle_tiles(self):
        shuffle(self.tiles)
    
    def show_tiles(self):
        for tile in self.tiles:
            print(tile,end=' ')
        print()
    
    def picked_tiles(self, n):
        picked_tiles = DominoSet()
        picked_tiles.clear()
        
        for _ in range(n):
            index = randint(0, len(self.tiles) - 1)
            tile = self.tiles.pop(index)
            picked_tiles.tiles.append(tile)
        return picked_tiles
        
        
def main():
    domino = DominoSet()
    domino.generate_tiles()        
    domino.shuffle_tiles()
    
    print('PEÇAS RETIRADAS')
    domino.picked_tiles(5)
    domino.show_tiles()
    
    print('PEÇAS RESTANTES')
    domino.show_tiles()
    
if __name__ == '__main__':
    main()