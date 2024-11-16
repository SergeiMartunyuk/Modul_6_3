class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self.speed = speed
        _cords = [0, 0, 0]

    def move(self, dx, dy, dz):
        self.dx = dx * self.speed
        self.dy = dy * self.speed
        self.dz = dz * self.speed

    def get_cords(self):
        print(f'X: {self.dx}, Y: {self.dy}, Z: {self.dz}')

    def attack(self):
        self._DEGREE_OF_DANGER += self._DEGREE_OF_DANGER
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

class Bird(Animal):
    import random
    num = [0, 1, 2, 3, 4]
    beak = True
    num_ = random.choice(num)

    def lay_eggs(self):
        print(f"Here are(is) {self.num_} eggs for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self.dz += dz * self.speed // -2

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):

    def speak(self):
        self.sound = "Click-click-click"
        print(self.sound)


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()