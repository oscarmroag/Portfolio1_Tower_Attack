# Imports:
import getpass
import textwrap
import sys

# Hiding user input for aesthetic purpose:
def hide_input(text):
  return getpass.getpass(text)
  
# Class Definition:
class Archer:
  def __init__(self):
    self.damage = 35
    self.cost = 25
  def __repr__(self):
    return "Archer with damage {damage} and cost {cost}".format(damage = self.damage, cost = self.cost)

class Soldier:
  def __init__(self):
    self.damage = 90
    self.cost = 60
  def __repr__(self):
    return "Soldier with damage {damage} and cost {cost}".format(damage = self.damage, cost = self.cost)

class Catapult:
  def __init__(self):
    self.damage = 270
    self.cost = 160
  def __repr__(self):
    return "Catapult with damage {damage} and cost {cost}".format(damage = self.damage, cost = self.cost)

class Tower:
  def __init__(self):
    self.health = 1000
    self.alive = True
  def __repr__(self):
    return "Tower HP = {tower_health}".format(tower_health = self.health)
  def lose_health(self, amount):
    # Deducts health from Tower
    self.health -= amount

class Player_Budget:
  def __init__(self):
    self.budget = 615
  def __repr__(self):
    return "Budget = ${budget}".format(budget = self.budget)

# Initialize Instances:
archer = Archer()
soldier = Soldier()
catapult = Catapult()
tower = Tower()
player_budget = Player_Budget()
first_turn = True 

# Initialize Game:

def initialize_game():
  Title_Screen = True
  while Title_Screen:
    choice = hide_input(textwrap.dedent("""\
        TOWER ATTACK:

        Your objective is to destroy the enemy tower using your budget to purchase attackers! 

        (Note: Your input will not be visible for aesthetic purposes)

        Press 1 to get started!
        Press 9 to exit at any time!
        """)
    )
    
    if choice == "1":
      player_turn()
      Title_Screen = False
    elif choice == "9": 
      sys.exit("Good Bye!")
    else: print("Press 1 to get started!")

def player_turn():
  if player_budget.budget < 25 : sys.exit(textwrap.dedent("""\
            Remaining Tower Health: {t_health}
            Budget too low! 
            GAME OVER
            ----------------------------------------------------------------------
            """).format(t_health = tower.health))
  while player_budget.budget > 0:
    global first_turn
    if first_turn:
        turn = hide_input(textwrap.dedent("""\
            ----------------------------------------------------------------------
            Tower Health = {tower_health}
            Budget = ${player_budget}

            Press 1 to use an Archer (${Archer_Cost}, DMG: {a_damage}), 2 to use a Soldier (${Soldier_Cost}, DMG: {s_damage}), or 3 to use a Catapult (${Catapult_Cost}, DMG: {c_damage})!
            ----------------------------------------------------------------------
            """).format(
                Archer_Cost=archer.cost,
                Soldier_Cost=soldier.cost,
                Catapult_Cost=catapult.cost,
                tower_health=tower.health,
                player_budget=player_budget.budget,
                a_damage = archer.damage,
                s_damage = soldier.damage,
                c_damage = catapult.damage
            ))
        first_turn = False
    else:
        turn = hide_input(textwrap.dedent("""\
            Tower Health = {tower_health}
            Budget = ${player_budget}

            1 = Archer (${Archer_Cost}, DMG: {a_damage}), 2 = Soldier (${Soldier_Cost}, DMG: {s_damage}), 3 = Catapult (${Catapult_Cost}, DMG: {c_damage})
            ----------------------------------------------------------------------
            """).format(
                Archer_Cost=archer.cost,
                Soldier_Cost=soldier.cost,
                Catapult_Cost=catapult.cost,
                tower_health=tower.health,
                player_budget=player_budget.budget,
                a_damage = archer.damage,
                s_damage = soldier.damage,
                c_damage = catapult.damage
            ))
    if turn == "9":
      sys.exit("Good Bye!")
    if turn == "1":
        if player_budget.budget >= archer.cost:
            tower.lose_health(archer.damage)
            player_budget.budget -= archer.cost
            if tower.health > 0:
                player_turn()
            else:
                tower.alive = False
                sys.exit(textwrap.dedent("""\
                "Congratulations! Tower Destroyed!"
                ----------------------------------------------------------------------
                """))
        else:
            print(textwrap.dedent("""\
            Not Enough Money!
            -------------------------------------------------------------------
            """))
            player_turn()
    elif turn == "2":
        if player_budget.budget >= soldier.cost:
            tower.lose_health(soldier.damage)
            player_budget.budget -= soldier.cost
            if tower.health > 0:
                player_turn()
            else:
                tower.alive = False
                sys.exit(textwrap.dedent("""\
                "Congratulations! Tower Destroyed!"
                ----------------------------------------------------------------------
                """))
        else:
            print(textwrap.dedent("""\
            Not Enough Money!
            -------------------------------------------------------------------
            """))
            player_turn()
    elif turn == "3":
        if player_budget.budget >= catapult.cost:
            tower.lose_health(catapult.damage)
            player_budget.budget -= catapult.cost
            if tower.health > 0:
                player_turn()
            else:
                tower.alive = False
                sys.exit(textwrap.dedent("""\
                "Congratulations! Tower Destroyed!"
                ----------------------------------------------------------------------
                """))
        else:
            print(textwrap.dedent("""\
            Not Enough Money!
            -------------------------------------------------------------------
            """))
            player_turn()
    else: player_turn()

# Starting the game:

initialize = initialize_game()
