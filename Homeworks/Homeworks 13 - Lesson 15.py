import random


class Unit:
    def __init__(self, name, clan):
        self.name = name
        self.clan = clan
        self.power = 1
        self.health = 100
        self.intelligence = 1
        self.agility = 1

    def skill_up(cls):
        if cls == Mage and Mage.intelligence <= 9:
            Mage.intelligence += 1
        elif cls == Archer and Archer.agility <= 9:
            Archer.agility += 1
        elif cls == Knight and Knight.power <= 9:
            Knight.power += 1

    def heal(self):
        if self.health > 90:
            self.health = 100
        else:
            self.health += 10

    def __str__(self):
        return f"Имя: {self.name} | Клан: {self.clan} | "

    def force(self):
        return f"                   «{self.name}»                   \n" \
               f"Здоровье:{self.health} | Сила:{self.power} | Ловкость:{self.agility} | Интеллект:{self.intelligence}"


class Knight(Unit):
    def __init__(self, name_unit='None', name_clan='None'):
        super().__init__(name_unit, name_clan)
        weapons = ['Меч', 'Молот', 'Пика', 'Шпага', 'Трезубец', 'Кинжал']
        self.type_weapon = random.choice(weapons)

    def __str__(self):
        return super().__str__() + f"Тип оружия: {self.type_weapon}"


class Archer(Unit):
    def __init__(self, name='None', clan='None'):
        super().__init__(name, clan)
        bows = ['Обычный лук', 'Огненный лук', 'Ледяной лук', 'Асимметричный лук', 'Лук с четырьмя изгибами']
        self.type_bow = random.choice(bows)

    def __str__(self):
        return super().__str__() + f"Тип лука: {self.type_bow}"


class Mage(Unit):
    def __init__(self, name_unit='None', name_clan='None'):
        super().__init__(name_unit, name_clan)
        magic = ['Воздух', 'Огонь', 'Вода', 'Земля']
        self.type_magic = random.choice(magic)

    def __str__(self):
        return super().__str__() + f"Тип магии: {self.type_magic}"


mage = Mage("Ахмед", "Курвус")
archer = Archer("Хуан", "Бродяги")
knight = Knight("Педро", "Голов - Говяжих")
"""
force() - Показывает характеристики.
"""
print(mage)
print(archer)
print(knight)
