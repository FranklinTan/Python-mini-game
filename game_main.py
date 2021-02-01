class Adventurer:
    def __init__(self, name, level, strength, speed, power):
        self.name = name
        self.level = int(level)
        self.strength = int(strength)
        self.speed = int(speed)
        self.power = int(power)
        self.HP = self.level * 6
        self.hidden = False

    def __repr__(self):
        return (self.name + " - HP: " + str(self.HP))
        
    def attack(self, target):
        if target.hidden == True:
            return  self.name + " can't see " + target.name
        else:
            damage = self.strength + 4
            target.HP -= damage
            return self.name + " attacks " + target.name + " for " + str(damage) + " damage"

class Fighter(Adventurer):
    def __init__(self, name, level, strength, speed, power):
        Adventurer.__init__(self, name, level, strength, speed, power)
        self.HP = self.level * 12

    def __repr__(self):
        return (self.name + " - HP: " + str(self.HP))

    def attack(self, target):
        if target.hidden == True:
            return  self.name + " can't see " + target.name
        else:
            damage = self.strength * 2 + 6
            target.HP -= damage
            return self.name + " attacks " + target.name + " for " + str(damage) + " damage"
    
class Thief(Adventurer):
    def __init__(self, name, level, strength, speed, power):
        Adventurer.__init__(self, name, level, strength, speed, power)
        self.HP = self.level * 8
        self.hidden = True

    def __repr__(self):
        return (self.name + " - HP: " + str(self.HP))
        
    def attack(self, target):
        if self.hidden == True:
            if self.speed < target.speed and target.hidden == True:
                return  self.name + " can't see " + target.name
            else:
                damage = (self.speed + self.level) * 5
                target.HP -= damage
                self.hidden = False
                return self.name + " sneak attacks " + target.name + " for " + str(damage) + " damage"
        else:
            return Adventurer.attack(self, target)

class Wizard(Adventurer):
    def __init__(self, name, level, strength, speed, power):
        Adventurer.__init__(self, name, level, strength, speed, power)
        self.HP = self.level * 6
        self.fireballs_left = self.power

    def __repr__(self):
        return (self.name + " - HP: " + str(self.HP))

    def attack(self, target):
        if self.fireballs_left > 0:
            self.power -= 1
            self.fireballs_left -= 1
            target.hidden = False
            damage = self.level * 3
            target.HP -= damage
            return self.name + " casts fireball on " + target.name + " for " + str(damage) + " damage"
        else:
            return Adventurer.attack(self, target)


def duel(adv1, adv2):
    while adv1.HP > 0 and adv2.HP > 0:
        print(adv1)
        print(adv2)
        print(adv1.attack(adv2))
        if adv1.HP > 0 and adv2.HP > 0:
            print(adv2.attack(adv1))
        elif adv2.HP <= 0 and adv1.HP > 0:
            break
            print(adv1.name, " wins!")
            return True
    if adv1.HP <= 0 and adv2.HP > 0:
        winner = adv2.name
        print(winner, " wins!")
        return winner
        return True
    elif adv2.HP <= 0 and adv1.HP > 0:
        winner = adv1.name
        print(winner, " wins!")
        return winner
        return True
    else:
        print("Every one loses!")
        return False

def HP(challenger):
    return challenger.HP
    
def tournament(advList):
    if advList == []:
        winner = None
        return winner
    else:
        while len(advList) > 1:
            advList = sorted(advList, key = HP, reverse = True)
            winner = duel(advList[1], advList[0])
            if winner == advList[0].name:
                del advList[1]
            elif winner == advList[1].name:
                del advList[0]
        winner = advList[0]
        return winner
        
