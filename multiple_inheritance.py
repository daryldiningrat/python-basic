from loguru import logger


class User():
    def sign_in(self):
        logger.info(f"Logged in")

class Wizard(User):
    def __init__(self, name, power):

        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):

        self.name = name
        self.num_arrows = num_arrows
    
    def check_arrows(self):
        print(f'attacking with arrows: arrows left-{self.num_arrows}')

    def run(self):
        print('ran really fast')

class HybridBorg(Wizard, Archer):
    
    def __init__(self, name, power, num_arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, num_arrows)


wizard1 = Wizard('Merlin', 50) # instances
archer1 = Archer('Robin', 100) # instances
hb1 = HybridBorg('borgie', 90, 200)


# Multiple Inheritance
logger.info(f'---- Multiple Inhertiance ----')

print(hb1.run())
print(hb1.attack())
print(hb1.check_arrows())


