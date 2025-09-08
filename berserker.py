from enemy import enemy

class berserker(enemy):

    def take_damage(self, damage):
       self.health -= damage
       print("UH IM A GINGER")

   