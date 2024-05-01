import random
import os

class Ship:
    def __init__(self, name, cannons, crew, bank, maxhealth, invetory_items, chance):
        self.name = name
        self.cannons = cannons
        self.crew = crew
        self.bank = bank
        self.health = 100
        self.maxhealth = 100
        self.items = invetory_items
        invetory_items = 0
        chance = random.randint(1,5)
        
        
    def attack(self, target,):
        chance = random.randint(1,10)
        if chance >= 2:
            print("You hit")
            damage = random.randint(10, 20) + self.cannons
            print(f"{self.name} attacks {target.name} and deals {damage} damage!")
            print(f"{target.name} health: {target.health}")
        elif chance < 2:
            print("You missed")
            print(f"{target.name} health: {target.health}")
            damage = 0
        target.health -= damage
        target.health = max(target.health, 0)

    def boardchance(self):
        chance = random.randint(1,5)
        self.chance = chance


    def assault(self, target,):
        damage = random.randint(10,20) + self.cannons
        target.health -= damage
        target.health = max(target.health, 0)
        print(f"Enemy ship attacks player ship and deals {damage} damage!")
        print(f"You now have {target.health} health")

    def repair(self):
        self.maxhealth = self.maxhealth
        repair_amount = random.randint(10, 20)
        self.health += repair_amount
        if self.health > self.maxhealth:
            self.health = self.maxhealth
        print(f"{self.name} repairs {repair_amount} health.")
        print(f"{self.name} health: {self.health}")
    
    def treasure(self,):
        treasure_amount = random.randint(5, 20)
        self.bank += treasure_amount
        print(f"{treasure_amount} gold have been found")
        print(f"You now have {self.bank} gold")

    def stolen(self,):
        stolen_amount = random.randint(0,250)
        self.bank += stolen_amount
        print(f"You stole {stolen_amount} gold")
        print(f"You now have {self.bank} gold")

    def invetory(self,):
        invetory_items = 0
        self.items = invetory_items

class PirateGame:
    def __init__(self,):
        self.player_ship = Ship("Player Ship", cannons=5, crew=50, bank=0, maxhealth=100, invetory_items=0,chance=random.randint(1,5),)
        self.enemy_ship = Ship("Enemy Ship", random.randint(1, 5), crew=random.randint(10, 50), bank=0,maxhealth=random.randint(75, 150), invetory_items=0,chance=random.randint(1,5),)
        self

    def start(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
        while True:
            print("Options:")
            print("1. Attack enemy ship")
            print("2. Repair your ship")
            print("3. Search for treasure")
            print("4. Shop")
            print("5. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                os.system('cls' if os.name == 'nt' else 'clear')
                self.player_ship.health = self.player_ship.maxhealth
                self.enemy_ship.health = random.randint(75,150)   
                print(f"Enemy ship health: {self.enemy_ship.health}")
                print(f"Your current health: {self.player_ship.health}")
                print("Do you want to fight this ship?"), print("1. Fight ship"), print("2. No")
                choice = input("Enter your choice: ")
                
                if choice == "1":
                    while True:
                     if self.enemy_ship.health < 30:  
                        print("Options:") 
                        print("1. Shoot cannons")
                        print("2. Repair your ship")
                        print("3. Leave fight")
                        print("4. Board ship")

                     else:
                        print("Options:")
                        print("1. Shoot cannons")
                        print("2. Repair your ship")
                        print("3. Leave fight")

                     choice = input("Enter your choice: ")

                     if choice == "1":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        self.player_ship.attack(self.enemy_ship)

                        if self.enemy_ship.health >= 1:  
                         self.enemy_ship.assault(self.player_ship)
                        
                        if self.enemy_ship.health <= 0:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("You defeated the enemy ship!")
                            self.player_ship.stolen()
                            self.player_ship.health = self.player_ship.maxhealth - 25
                            print(f"You now have {self.player_ship.health} health")
                            break
                        
                        if self.player_ship.health <= 0:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Your ship was destroyed. Game over!")
                            quit()

                     elif choice == "2":
                         os.system('cls' if os.name == 'nt' else 'clear')
                         self.player_ship.repair()
                         
                     elif choice == "3":
                      os.system('cls' if os.name == 'nt' else 'clear')
                      print("You have left the fight")
                      break
                     
                     elif choice == "4":
                         if self.enemy_ship.health < 31:
                            if self.player_ship.crew > self.enemy_ship.crew:
                                self.player_ship.boardchance()
                                if self.player_ship.chance >= 2:
                                    self.player_ship.items += 1
                                    self.player_ship.crew -= 5
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print("You won the board")
                                    print(f"You now have {self.player_ship.items} captured ships ")
                                    print(f"You now have {self.player_ship.crew} crew members")
                                    break
                            if self.player_ship.chance < 2:
                                self.player_ship.crew = 25
                                print("You lost the board (crew now at 25)")
                                break

                         if self.player_ship.crew < self.enemy_ship.crew: 
                            self.player_ship.crew = 25
                            print("You lost the board (crew now at 25)")
                            break  
                            
                         else:
                             os.system('cls' if os.name == 'nt' else 'clear')
                             print("Invalid choice. Try again")
                     
                     else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Invalid choice. Try again.")

                elif choice == "2":
                      os.system('cls' if os.name == 'nt' else 'clear')
                      print("You didn't take the fight")
                    
            elif choice == "2":
                os.system('cls' if os.name == 'nt' else 'clear')
                self.player_ship.repair()
                
            elif choice == "3":
                os.system('cls' if os.name == 'nt' else 'clear')
                self.player_ship.treasure()

            elif choice == "4":
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f" Hull stability: {self.player_ship.maxhealth}%, Cannons amount: {self.player_ship.cannons}, Crew members: {self.player_ship.crew}, Gold coins: {self.player_ship.bank}, Captured ships: {self.player_ship.items}")
                    print("")
                    print("     Welcome to the Shop    ")
                    print("")
                    print("Options")
                    print("1. Buy cannons (1000 coins)")
                    print("2. Buy crew members (100 coins)")
                    print("3. Upgrade ship (5000 coins)")
                    print("4. Sell caputued ship (1000 coins)")
                    print("5. Leave shop")

                    choice = input("Enter your choice:")

                    if choice == "1":
                        if self.player_ship.bank < 1000:
                            self.player_ship.cannons - 1 
                            print("You don't have enough coins")
                        elif self.player_ship.bank >= 1000:
                             self.player_ship.bank -= 1000
                             self.player_ship.cannons += 1
                             print(f"You now have {self.player_ship.cannons} cannons")

                    elif choice == "2":
                        if self.player_ship.bank < 100:
                            self.player_ship.crew - 10
                            print("You don't have enough coins")
                        elif self.player_ship.bank >= 100:
                             self.player_ship.bank -= 100
                             self.player_ship.crew += 10
                             print(f"You now have {self.player_ship.cannons} cannons")

                    elif choice == "3":
                        if self.player_ship.bank < 5000:
                            self.player_ship.maxhealth - 50 
                            print("You don't have enough coins")
                        elif self.player_ship.bank >= 5000:
                             self.player_ship.bank -= 5000
                             self.player_ship.maxhealth += 50
                             print(f"Upgraded hull stability to {self.player_ship.maxhealth}%")

                    elif choice == "4":
                        if self.player_ship.items < 1:
                            self.player_ship.bank - 10000
                            print("You don't have any captured ships")
                        elif self.player_ship.items >= 1:
                            self.player_ship.items -= 1
                            self.player_ship.bank += 1000
                            print("You have sold a captured ship")

                    elif choice == "5":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break

                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Invalid choice. Try again.")

            elif choice == "5":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Thanks for playing!")
                quit()
            
            elif choice == "clear":
                os.system('cls' if os.name == 'nt' else 'clear')

            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Invalid choice. Try again.")
            
            if self.player_ship.health < 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Your ship was destroyed. Game over!") 
                quit()

if __name__ == "__main__":
    game = PirateGame()
    game.start()