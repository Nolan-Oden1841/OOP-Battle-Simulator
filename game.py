import random
from goblin import Goblin
from hero import Hero
from boss import mega_knight
def main():
    print("Welcome to the Battle Arena!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    # Create a hero
    hero = Hero("Aragorn")

    # Create goblins ༼ ºل͟º ༽ ༼ ºل͟º ༽ ༼ ºل͟º ༽
    goblin_colors = ['Green', 'Red', 'Blue', 'Yellow', 'Purple', 'Orange', 'Black', 'White', 'Gray', 'Brown']
    goblins = [Goblin(f"Goblin {i+1}", color, health=100) for i, color in enumerate(goblin_colors)]

    # Keep track of how many goblins were defeated
    defeated_goblins = 0

    # Battle Loop 
    while hero.is_alive() and any(goblin.is_alive() for goblin in goblins):
        print("\nNew Round!")
        
        # Hero's turn to attack
        target_goblin = random.choice([goblin for goblin in goblins if goblin.is_alive()])
        damage = hero.strike()
        print(f"Hero attacks {target_goblin.name} for {damage} damage!")
        target_goblin.take_damage(damage, target_goblin.health)

        # Check if the target goblin was defeated
        if not target_goblin.is_alive():
            defeated_goblins += 1
            print(f"{target_goblin.name} has been defeated!")

        # Goblins' turn to attack
        for goblin in goblins:
            if goblin.is_alive():
                damage = goblin.attack()
                print(f"{goblin.name} attacks hero for {damage} damage!")
                hero.receive_damage(damage, hero.health)

    # Determine outcome
    if hero.is_alive():
        print(f"\nThe hero has defeated all the goblins! ༼ ᕤ◕◡◕ ༽ᕤ")
    else:
        print(f"\nThe hero has been defeated. Game Over. (｡•́︿•̀｡)")

    # Final tally of goblins defeated
    print(f"\nTotal goblins defeated: {defeated_goblins} / {len(goblins)}")

    if hero.is_alive() and defeated_goblins == len(goblins):
        print("Mega Knight appears (ง'̀-'́)ง")
        mega_knight_boss = mega_knight("Mega Knight")
        
        while hero.is_alive() and mega_knight_boss.is_alive():
            # Hero's turn to attack
            damage = hero.strike()
            print(f"Hero attacks {mega_knight_boss.name} for {damage} damage!")
            mega_knight_boss.take_damage(damage, mega_knight_boss.health)

            if not mega_knight_boss.is_alive():
                print(f"{mega_knight_boss.name} has been defeated! The hero is victorious! ༼ ᕤ◕◡◕ ༽ᕤ")
                break

          
            if random.random() < 0.2:
                damage = mega_knight_boss.special_attack()
                print(f"{mega_knight_boss.name} uses a SPECIAL ATTACK for {damage} damage!")
            else:
                damage = mega_knight_boss.attack()
                print(f"{mega_knight_boss.name} attacks hero for {damage} damage!")
            hero.receive_damage(damage, hero.health)

        if not hero.is_alive():
            print(f"\nThe hero has been defeated by the Mega Knight. Game Over. (｡•́︿•̀｡)")

if __name__ == "__main__":
    main()
