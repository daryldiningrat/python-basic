from re import A
from loguru import logger


class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        logger.info(f"Logged in")

class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows, email):
        super().__init__(email)
        self.name = name
        self.num_arrows = num_arrows
    
    def attack(self):
        print(f'attacking with arrows: arrows left-{self.num_arrows}')

    def run(self):
        print('ran really fast')


wizard1 = Wizard('Merlin', 50, 'merlin@mail.com') # instances
archer1 = Archer('Robin', 100, 'robin@mail.com') # instances

print(wizard1.sign_in())
print(archer1.sign_in())

# Inheritance
logger.info(f'---- Inhertiance ----')

wizard1.name
wizard1.attack()

archer1.name
archer1.attack()

# polymorphism
logger.info(f'---- Polymorphism ----')

wizard2 = Wizard('Daryl', 100, 'daryl@mail.com') # instances
archer2 = Archer('Buriza', 40, 'buriza@mail.com') # instances

for char in [wizard2, archer2]:
    char.attack()
    print(char.email)

# Introspection

print(dir(wizard2))

