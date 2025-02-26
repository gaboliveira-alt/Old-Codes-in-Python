import random

class Lamp:
    def __init__(self, initial_state = False):
        if initial_state:
            self.state = "on"
        else:
            self.state = "off"
    
    def turn_on(self):
        self.state = "on"
        
    def turn_off(self):
        self.state = "off"
        
    def show_state(self):
        print("Lamp is", self.state)
        
def main():
    lamp1 = Lamp(True)
    lamp2 = Lamp()
    lamp2.turn_on
        
    print("Lamp States: ")
    print("- Lamp #1", end='')
    lamp1.show_state()
        
    print("- Lamp #2", end='')
    lamp2.show_state()
        
    def lamp_test():
        lamps = []
        lamps_count = random.randint(5, 20)
            
        for _ in range(lamps_count):
            lamps.append(Lamp())
                
            for lamp in lamps:
                lamp.show_state()
                    
                    
if __name__ == "__main__":
    main()