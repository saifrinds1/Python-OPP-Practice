class Fighter:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 10

    def attack(self, other_guy):
        print("{} attacks {}!".format(self.name,other_guy.name))
        print("{} loses {} health points".format(other_guy.name,self.damage))
        other_guy.health  -= self.damage

    def __str__(self):
        return "{}: {}".format(self.name, self.health)

ftr1 = Fighter("Gohan")
ftr2 = Fighter("Gooku")

print(ftr1)
print(ftr2)

ftr2.attack(ftr1)

print(ftr1)
print(ftr2)