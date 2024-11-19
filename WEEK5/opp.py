from abc import ABC, abstractmethod
import random


class GameCharacter(ABC):
    def __init__(self, name, level=1):
        self._name = name
        self._level = level
        self._health = 100
        self._experience = 0
        
    @property
    def name(self):
        return self._name
    
    @property
    def level(self):
        return self._level
    
    @property
    def health(self):
        return self._health
    
    def gain_experience(self, amount):
        self._experience += amount
        if self._experience >= 100:
            self.level_up()
    
    def level_up(self):
        self._level += 1
        self._experience = 0
        print(f"{self._name} has reached level {self._level}! 🎉")
    
    def take_damage(self, amount):
        self._health = max(0, self._health - amount)
        if self._health == 0:
            print(f"{self._name} has been defeated! ☠️")
    
    def heal(self, amount):
        self._health = min(100, self._health + amount)
        print(f"{self._name} healed for {amount} health! ❤️")
    
    @abstractmethod
    def special_ability(self):
        pass

# Warrior Class
class Warrior(GameCharacter):
    def __init__(self, name, weapon="Sword", level=1):
        super().__init__(name, level)
        self.weapon = weapon
        self._strength = 15
        
    def special_ability(self):
        damage = self._strength * self._level
        print(f"⚔️ {self._name} uses Mighty Strike with {self.weapon} for {damage} damage!")
        return damage
    
    def battle_cry(self):
        print(f"🗣️ {self._name}: For glory and honor!")

# Mage Class
class Mage(GameCharacter):
    def __init__(self, name, spell_school="Arcane", level=1):
        super().__init__(name, level)
        self.spell_school = spell_school
        self._mana = 100
        
    def special_ability(self):
        if self._mana >= 30:
            damage = 20 * self._level
            self._mana -= 30
            print(f"🔮 {self._name} casts a powerful {self.spell_school} spell for {damage} damage!")
            return damage
        else:
            print(f"⚠️ {self._name} is out of mana!")
            return 0
    
    def meditate(self):
        self._mana = min(100, self._mana + 30)
        print(f"✨ {self._name} meditates and recovers mana. Current mana: {self._mana}")


class Rogue(GameCharacter):
    def __init__(self, name, stealth_level=5, level=1):
        super().__init__(name, level)
        self.stealth_level = stealth_level
        self._energy = 100
        
    def special_ability(self):
        if self._energy >= 25:
            damage = 25 * self._level
            self._energy -= 25
            print(f"🗡️ {self._name} performs a stealth attack for {damage} damage!")
            return damage
        else:
            print(f"⚠️ {self._name} is out of energy!")
            return 0
    
    def hide(self):
        success_chance = min(90, self.stealth_level * 10)
        if random.randint(1, 100) <= success_chance:
            print(f"🥷 {self._name} successfully hides in the shadows!")
            return True
        print(f"👀 {self._name} failed to hide!")
        return False


def simulate_battle():
    
    warrior = Warrior("Aragorn", weapon="Andúril")
    mage = Mage("Gandalf", spell_school="Light")
    rogue = Rogue("Ezio", stealth_level=8)
    
    print("=== Welcome to the Battle Simulator! ===\n")
    
   
    characters = [warrior, mage, rogue]
    
    for round_num in range(1, 4):
        print(f"\nRound {round_num}:")
        print("-" * 30)
        
        for char in characters:
            
            char.special_ability()
            
            #
            if isinstance(char, Warrior):
                char.battle_cry()
            elif isinstance(char, Mage):
                char.meditate()
            elif isinstance(char, Rogue):
                char.hide()
            
           
            damage = random.randint(10, 30)
            char.take_damage(damage)
            if char.health < 50:
                char.heal(25)
            
           
            char.gain_experience(random.randint(20, 40))
            print(f"Health: {char.health}, Level: {char.level}\n")

if __name__ == "__main__":
    simulate_battle()