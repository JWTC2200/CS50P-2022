# DUNGEON CRAWLER

#### Video Demo: https://youtu.be/qRkBDWUOsWI

### Introduction

My project is a short dungeon crawler game for the CS50P course.

The game is has the player go through different rooms battling monsters to reach the end of the dungeon. I want the game to be easily changeable so users can craft their own adventures.

Game files are stored in several .csv files and the game itself is played through the terminal window.

### Files

The game requires the following files to run:

- project.py
- room.csv 
- room_text.csv
- mons.csv
- mage.csv
- warrior.csv

**_room.csv_**: contains the information on each dungeon room. None of the data needs to be numerical as long as the data is kept consistent across the files so it can cross reference. For multiple monsters in a room the *mons* should have each additional monster seperated by a *"/"*.

**_room_text.csv_**: in order to reduce the size of *ro0m.csv* I sepearated each dungeon rooms flavour text into a seperate file. This also allows rooms to reuse flavour text as long as the *text* in *room.csv* is the same *id* in *room_text.csv*.

**_mons.csv_**: monster information. *id* should be the same as in *room.csv*. *hp*, *dmg* and *exp* should be integers.

**_mage.csv_** & **_warrior.csv_**: contain the stats for each hero class the player can choose from. *level* 1 stats are all applied upon initially selecting a class but are handled differently when the character levels up. *hp*, *mp* and *attk* are all **added** onto the character stats as they level up, as the hero may have taken damage or and lost hp or used mp on spells. *hpx, *mpx* and *xp* replace previous values as they represent maximum amounts.


### Playing the game

Upon starting the game you must decide between playing a Mage or a Warrior. The Mage has less HP and basic attack but much more MP to cast powerful spells (currently only Zap implemented). The Warrior much more HP and Attack but has very low MP and will likley only cast one or two spells during the adventure.

During the adventure you may be given the option to flee or not fight the monsters in the room in which case the adventure will end and the program will stop.

When battling the monsters in the room will be displayed and you have a number of options to choose from:
1. Attack
   - Deal damage equal to your *attk* value to the target monster.
2. Spell
   - Cast either *Heal* (recover 10HP for 3MP) or *Zap* (deal 20DMG to a target monster for 2MP)
3. Flee
   - Ends the adventure
4. Stats
   - Display your current stats, such as HP and MP

After each battle the exp you get from will be applied and your character may level up and grow stronger.

You will then be given a choice to recover half your HP or MP before continuing on to the next room.


### Closing thoughts

I originally had a lot more features for this game such as loot completeting a room, weapons or branching paths after each room. These features felt rather samey to code as I was going through so I dropped them.

If I was to add to this project I would try and have this implemented in a browser for a nicer UI.

Although the adventure is currently very basic it can be easily changed through the csv files for a longer more challenging game achiving my goal of making it easily customisable.

