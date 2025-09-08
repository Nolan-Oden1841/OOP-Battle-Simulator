import random     
from enemy import Enemy

class mega_knight(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.health = 1000
        if random.random() < 0.2:
            self.attack_power = random.randint(100,200)
        else:
            self.attack_power = random.randint(50,150)

    def attack(self):
        return random.randint(self.attack_power // 2, self.attack_power)

    def special_attack(self):
        base_damage = self.attack()
        return base_damage * 2




