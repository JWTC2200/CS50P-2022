import csv
import sys
from tabulate import tabulate
from time import sleep

# class for current story progress
class Story:
    def __init__(self):
        self.progress = None

    def story_progress(self, room):
        self.progress = room

# class to keep track of and load room data
class Rooms:
    def __init__(self):
        self.room_name = ""
        self.room_text = ""
        self.room_mons = ""
        self.room_branch = ""
        self.room_current = ""
        self.mon_stats = []

    def __str__(self):
        if self.room_mons == "":
            self.room_mons = "\nNo monsters in this room"
        return f'{self.room_name}: {self.room_text}\nMonsters:{self.room_mons}'

    # loads room related variables
    def open_room(self, location):
        self.room_mons = ""
        with open("room.csv") as room:
            room_list = csv.DictReader(room)
            for row in room_list:
                if row["id"] == location:
                    # room name and current location
                    self.room_name = row["name"]
                    self.room_current = row["id"]
                    # room flavour text
                    room_text_no = row["text"]
                    with open("room_text.csv") as text_file:
                        text_list = csv.DictReader(text_file)
                        for line in text_list:
                            if line["id"] == room_text_no:
                                self.room_text = line["text"]
                    # add monsters
                    self.room_monsters(row["mons"])
                    # add next room branch
                    self.room_branch = row["branch"]

    # returns current room
    def room_location(self):
        return self.room_current

    # load monsters into dict
    def room_monsters(self, mons_list_raw):
        if self.mon_stats == []:
            mons_list_split = mons_list_raw.split("/")
            mon_num = 0
            for split in mons_list_split:
                with open("mons.csv") as mons:
                    mons_list = csv.DictReader(mons)
                    for row in mons_list:
                        if row["id"] == split:
                            mon_num += 1
                            self.room_mons += f'\n• {row["name"]}'
                            stats = {"no": mon_num, "name":row["name"], "hp":int(row["hp"]), "attk":row["attk"], "dmg":int(row["dmg"]), "exp":int(row["exp"])}
                            self.mon_stats.append(stats)

    # display monster dict
    def monster_table(self):
        if self.mon_stats == []:
            print("All monsters defeated!")
        else:
            print(tabulate(self.mon_stats, headers="keys", tablefmt="grid"))

    # handles monster damage. target must be an int
    def monster_damage(self, target, damage):
        r = -1
        for row in self.mon_stats:
            r += 1
            if row["no"] == target:
                row["hp"] -= damage
                if row["hp"] <= 0:
                    print(f'You have defeated {row["name"]}')
                    # deletes row index from dict
                    del self.mon_stats[r]


# contains all character class information and functions
class Hero:
    def __init__(self):
        self.job = None
        self.level = 1
        self.exp = 0
        self.expbar = 0
        self.health = 0
        self.health_max = 0
        self.mana = 0
        self.mana_max = 0
        self.attk = 0

    # hero stats as string format
    def __str__(self):
        return (f'⬥ {self.job}\n⬥ LV:{self.level}\n⬥ HP:{self.health}/{self.health_max}\n⬥ MP:{self.mana}/{self.mana_max}\n⬥ ATK:{self.attk}\n⬥ XP:{self.exp}/{self.expbar}')

    # hero stats into a list
    def hero_stats(self):
        stat = [{
            "job": self.job,
            "level": self.level,
            "exp": f'{self.exp}/{self.expbar}',
            "health": f'{self.health}/{self.health_max}',
            "mana": f'{self.mana}/{self.mana_max}',
            "attk": self.attk
            }]
        return stat

    # hero stats displayed using tabulate
    def hero_table(self):
        print(tabulate(self.hero_stats(), headers="keys", tablefmt="grid"))

    # stats used for battles only
    def hero_battle_stat(self):
        stat = [{
            "health": self.health,
            "health_max": self.health_max,
            "mana": self.mana,
            "mana_max": self.mana_max,
            "attk": self.attk
        }]
        return stat

    # only run on initial class selection
    def choose_job(self, job):
        valid_jobs = ("mage", "warrior")
        job_ck = job.lower().strip()
        if job_ck in valid_jobs:
            if job_ck == "mage":
                self.job = "Mage"
            if job_ck == "warrior":
                self.job = "Warrior"
            self.level_up(1)
        else:
            print("Invalid job")

    # function to add xp from fights. Triggers the level_up function
    def exp_gain(self, xp):
        self.exp += xp
        if self.exp >= self.expbar:
            self.level += 1
            print("YOU HAVE LEVELED UP!")
            self.exp = 0
            self.level_up(self.level)

    # Level character up from CSV. Also used to assign level 1 stats on class selection
    def level_up(self, level):
        if self.job == "Warrior":
            file = "warrior.csv"
        if self.job == "Mage":
            file = "mage.csv"
        with open(file) as c:
            character = csv.DictReader(c)
            for row in character:
                if int(row["level"]) == level:
                    self.expbar = int(row["xp"])
                    self.health += int(row["hp"])
                    self.health_max = int(row["hpx"])
                    self.mana += int(row["mp"])
                    self.mana_max = int(row["mpx"])
                    self.attk += int(row["attk"])
                    print(self)

    # damage calc
    def hero_damage(self, dmg):
        self.health -= dmg
        if self.health <= 0:
            print("You have died!")
            sys.exit("GAME OVER!")
        print(f'{self.health}/{self.health_max}HP')

    # healing calc and notices
    def hero_healing(self, heal):
        self.health += heal
        if self.health >= self.health_max:
            self.health == self.health_max
            print(f'{self.health}/{self.health_max}HP, fully healed')
        else:
            print(f'{self.health}/{self.health_max}HP')

    def hero_attack(self):
        return self.attk


def main():
    story = Story()
    room = Rooms()
    hero = Hero()

    # select initial class
    while hero.job == None:
        print("Welcome to the dungeon!")
        print("Are you a Mage or Warrior?")
        choose = input("class: ")
        ## sleep(1)
        hero.choose_job(choose)

    #  load first room
    while story.progress == None:
        sleep(1)
        print("Your adventure starts here!")
        story.progress = "1"

    # loop until story reaches end point branch 0
    while story.progress != "0":
        room.open_room(story.progress)
        sleep(1)
        if room.mon_stats != []:
            print(room)
            if battle_request(room.mon_stats):
                room.mon_stats, herostats, battle_exp = battling(hero.hero_battle_stat(), room.mon_stats)
                # update hero values
                hero.health = herostats[0]["health"]
                hero.mana = herostats[0]["mana"]
                # check if character has leveled up
                sleep(1)
                print(f'You earned {battle_exp}XP!')
                hero.exp_gain(battle_exp)
                sleep(1)
            print("You have defeated all the monsters")
            sleep(1)
            hero.health, hero.mana = recovery(hero.health, hero.health_max, hero.mana, hero.mana_max)
            sleep(1)
        print("Moving to next room")
        story.progress = room.room_branch

    if story.progress == "0":
        print("You have completed the adventure!")

# seperates the battle or flee request
def battle_request(encounter):
    if encounter != []:
        while True:
            sleep(1)
            reply = input("Do you want to fight the monsters Y/N?: ").lower().strip()
            if reply == "y":
                print("Lets battle!")
                sleep(1)
                return True
            if reply == "n":
                sys.exit("You have fled the dungeon\nYour adventure is over")


# function handling battles. Pass in character attack and monster table.
def battling(hero, monster):
    battle_exp = 0
    while monster != []:
        hero_turn = True
        while hero_turn == True:
            sleep(1)
            print(tabulate(monster, headers="keys", tablefmt="grid"))
            sleep(0.5)
            attack_stat = hero[0]["attk"]
            choice = input("What would you like to do?\n1.Attack\n2.Spell\n3.Flee\n4.Stats\n").strip()
            # sum exp from defeated monsters
            if choice == "1":
                monster, exp_sum = make_attack(monster, attack_stat)
                battle_exp += exp_sum
                hero_turn = False
            if choice == "2":
                monster, hero, exp_sum = cast_spell(monster, hero)
                battle_exp += exp_sum
                hero_turn = False
            if choice == "3":
                sys.exit("You flee the dungeon!\nGame over!")
            if choice == "4":
                print(tabulate(hero, headers="keys", tablefmt="grid"))
            if choice not in ["1", "2", "3", "4"]:
                print("Invalid choice")
        if monster != []:
            hero = monster_attack(monster, hero)
    # tuple with adjusted values
    return monster, hero, battle_exp


# validation for battle targeting
def make_attack(monster, damage):
    while True:
        target = input("Which monster do you want to attack? ")
        battle_exp = 0
        valid_targets = []
        for row in monster:
            valid_targets.append(row["no"])
        if target.isdigit():
            if int(target) in valid_targets:
                for row in monster:
                    if row["no"] == int(target):
                        row["hp"] -= damage
                        print(f'You deal {damage} damage to {row["name"]}!')
                        # check if monster defeated, delete row and add exp
                        if row["hp"] <= 0:
                            print(f'You have defeated {row["name"]}!')
                            battle_exp += row["exp"]
                            monster.remove(row)
                return monster, battle_exp
            else:
                print("Invalid target (type number)")
        else:
            print("Wrong input")

def cast_spell(monster, hero):
    while True:
        choice = input("Cast a spell:\n1.Heal 10HP 3MP \n2.Zap 20Dmg 2MP\n")
        options = ["1", "2"]
        battle_exp = 0
        if choice not in options:
            print("Invalid choice")
        # heal spell
        if choice == "1":
            # check mana (min 3)
            sleep(0.5)
            if hero[0]["mana"] < 3:
                print("Not enough mana. Your spell fails!")
                return monster, hero
            hero[0]["mana"] -= 3
            print("You cast Heal!")
            hero[0]["health"] += 10
            # stop health going above max
            if hero[0]["health"] > hero[0]["health_max"]:
                hero[0]["health"] = hero[0]["health_max"]
            print(tabulate(hero, headers="keys", tablefmt="grid"))
            return monster, hero, battle_exp
        if choice == "2":
            sleep(0.5)
            # check mana (min 2)
            if hero[0]["mana"] < 2:
                print("Not enough mana. Your spell fails!")
                return monster, hero, 0
            hero[0]["mana"] -= 2
            # treat as attack with set damage
            target = input("Which monster do you want to attack? ")
            valid_targets = []
            for row in monster:
                valid_targets.append(row["no"])
            if target.isdigit():
                if int(target) in valid_targets:
                    for row in monster:
                        if row["no"] == int(target):
                            row["hp"] -= 25
                            print(f'You deal 20 damage to {row["name"]}!')
                            # check if monster defeated, delete row and add exp
                            if row["hp"] <= 0:
                                print(f'You have defeated {row["name"]}!')
                                battle_exp += row["exp"]
                                monster.remove(row)
                    return monster, hero, battle_exp
                else:
                    print("Invalid target")
            else:
                print("Invalid target")

def monster_attack(monster, hero):
    sleep(1)
    for row in monster:
        sleep(0.5)
        print(f'• {row["name"]} attacks you with {row["attk"]} for {row["dmg"]} damage!')
        hero[0]["health"] -= int(row["dmg"])
        print(f'⬦ You have {hero[0]["health"]}/{hero[0]["health_max"]}HP')
        if hero[0]["health"] < 1:
            sys.exit("Your hero has died. Game over!")
    return hero

def recovery(hp, hpx, mp, mpx):
    hp_rec = int(hpx/2)
    mp_rec = int(mpx/2)
    while True:
        choice = input(f'Do you want to recover {hp_rec}HP or {mp_rec}MP?').lower().strip()
        if choice == "hp":
            hp += hp_rec
            if hp > hpx:
                hp = hpx
            return hp, mp
        if choice == "mp":
            mp += mp_rec
            if mp > mpx:
                mp = mpx
            return hp, mp
        else:
            print("Invalid choice, HP or MP")


if __name__ == "__main__":
    main()