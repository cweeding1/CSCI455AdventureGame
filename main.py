import random
import sys
import robot


class Player:
    def __init__(self):
        self.health = 300
        self.maxHealth = 300
        self.key = False
        self.attack = 25
        self.potion = 1
        self.recharged = False
        self.weapon = "Plastic Sword"
        

    def fight(self, enemy):

        if enemy.defeated == True:
            print("You already beat me")
            return

        else:
            print("There is a enemy here\nYou have " + str(self.health) + "/" + str(self.maxHealth) + " health")
            while True:
                choice = int(input("1. Fight\n2. Health Potion (Coward)\n3. Run (Even Bigger Coward)\n---> "))
                if choice == 1:
                    if self.health > 0 and enemy.health > 0:
                        print("You attack with your " + str(self.weapon))
                        #TODO make sure this works
                        robo.armMove()
                        dmg = random.randint(self.attack-15, self.attack)
                        print("Somehow you dealt " + str(dmg) + " damage to your opponent")
                        enemy.health -= dmg
                        if enemy.health <= 0:
                            print("\nThat was the killing blow\n"
                                  "How do you feel about killing an opponent with no arms?")
                            enemy.health = 0
                            enemy.defeated = True
                            break
                        else:
                            enemyDmg = random.randint(enemy.attack-5, enemy.attack)
                            #TODO make sure this works
                            robo.headTiltCommand()
                            print("\nLuckily your opponent sucks and only dealt " + str(enemyDmg) + " damage to you")
                            self.health -= enemyDmg
                            if self.health <= 0:
                                print("but that was the killing blow and you lost...")
                                print("ENEMY: " + str(enemy.taunt))
                                break
                                sys.exit(0)
                            else:
                                print("You have " + str(self.health) + "/" + str(self.maxHealth) + " health, your opponent has " + str(enemy.health) + "/" + str(enemy.maxHealth) + " health\n")
                elif choice == 3:
                    chance = random.randint(1, 4)
                    if chance == 1:
                        print("You tripped while running away and lost 10 health\nYou must fight for your life")
                        self.health -= 10
                    else:
                        print("Panzy Ass")
                        print("You ran away with " + str(self.health) + "/" + str(self.maxHealth) + " health")
                        break
                elif choice == 2:
                    if self.potion > 0:
                        self.potion -= 1
                        self.health += 25
                        if self.health > self.maxHealth:
                            self.health = self.maxHealth
                        print("You used a potion and restored your health to " + str(self.health) + "/" + str(self.maxHealth))
                    else:
                        print("You don't have any potions dummy")

    def recharge(self):
        if not self.recharged:
            robo.tts("recharging health")
            self.health = self.maxHealth
            robo.tts("you now have full health")
            self.recharged = True
        else:
            robo.tts("recharge station already used, tough luck")
            robo.tts("your health is at " + str(self.health) + "/" + str(self.maxHealth))


class Enemy:
    def __init__(self):
        self.health = 50
        self.maxHealth = 50
        self.attack = 10
        self.defeated = False
        self.taunt = "You Suck"


class HardEnemy:
    def __init__(self):
        self.health = 100
        self.maxHealth = 100
        self.attack = 20
        self.defeated = False
        self.taunt = "I AM HUNTER LLOYD, THE KILLER OF GODS"


class Maze:
    def __init__(self):
        self.positionX = 0
        self.positionY = 0
        self.moveCount = 0
        self.totalMoves = 40
        self.facingDirection = "East"

        self.items = [["CRUSTY SOCK", 40], ["DEEZ HANDS", 40], ["MAGIC WAND OF METH", 50], ["POOL NOODLE ENERGY SWORD", 50],
                      ["SUPER SOAKER 3000", 55], ["LOONEYS LEFT LEG", 55], ["HEROIN NEEDLE", 60]]

        self.maze = [[ 1,   0,  2,  0,   3],
                     ["x", "x", 0, "x",  0],
                     [ 6,   0,  7, "x",  8],
                     [ 0,  "x", 0, "x", "x"],
                     [11,  "x", 12, 0,   13]]

        #enemy positions
        self.enemy2 = Enemy()
        self.enemy3 = Enemy()
        self.enemy8 = Enemy()
        self.enemy7 = Enemy()

        self.hardEnemy11 = HardEnemy()
        self.hardEnemy13 = HardEnemy()


        self.visitedMaze = [[0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0]]

        self.updateVisited(self.positionX, self.positionY)

    def updateVisited(self, x, y):
        self.visitedMaze[x][y] = 1
        print(self.visitedMaze[0])
        print(self.visitedMaze[1])
        print(self.visitedMaze[2])
        print(self.visitedMaze[3])
        print(self.visitedMaze[4])

    def updateDirection(self, direction):
        if self.facingDirection == "North":
            if direction == "East":
                print("turning right 90")
                robo.turnRight()
                self.facingDirection = direction
            elif direction == "South":
                print("turning 180")
                robo.turnAround()
                self.facingDirection = direction
            elif direction == "West":
                print("turning left 90")
                robo.turnLeft()
                self.facingDirection = direction
        elif self.facingDirection == "East":
            if direction == "South":
                print("turning right 90")
                robo.turnRight()
                self.facingDirection = direction
            elif direction == "West":
                print("turning 180")
                robo.turnAround()
                self.facingDirection = direction
            elif direction == "North":
                print("turning left 90")
                robo.turnLeft()
                self.facingDirection = direction
        elif self.facingDirection == "South":
            if direction == "West":
                print("turning right 90")
                robo.turnRight()
                self.facingDirection = direction
            elif direction == "North":
                print("turning 180")
                robo.turnAround()
                self.facingDirection = direction
            elif direction == "East":
                print("turning left 90")
                robo.turnLeft()
                self.facingDirection = direction
        elif self.facingDirection == "West":
            if direction == "North":
                print("turning right 90")
                robo.turnRight()
                self.facingDirection = direction
            elif direction == "East":
                print("turning 180")
                robo.turnAround()
                self.facingDirection = direction
            elif direction == "South":
                print("turning left 90")
                robo.turnLeft()
                self.facingDirection = direction

        print("You are facing " + self.facingDirection)

    def getPaths(self):
        #print("X:" + str(self.positionX) + " Y:" + str(self.positionY))

        if self.positionY != 0 and self.maze[self.positionX][self.positionY-1] != "x":
            print("There is a path to the West")
            robo.tts("There is a path to the west")

        if self.positionY != (len(self.maze) - 1) and self.maze[self.positionX][self.positionY+1] != "x":
            print("There is a path to the East")
            robo.tts("There is a path to the east")

        if self.positionX != 0 and self.maze[self.positionX-1][self.positionY] != "x":
            print("There is a path to the North")
            robo.tts("There is a path to the north")
        
        if self.positionX != (len(self.maze) - 1) and self.maze[self.positionX+1][self.positionY] != "x":
            print("There is a path to the South")
            robo.tts("There is a path to the south")

    def checkEnemy(self, x, y):
        #print(self.maze[x][y])

        if self.maze[x][y] != 0:
            if self.maze[x][y] == 12:
                Chris.recharge()

            if self.maze[x][y] == 6:
                print("There is a exit sign here, do you have the key")
                if Chris.key:
                    print("You used the key to escape\nYOU WIN")
                    sys.exit(0)
                else:
                    print("Come back with the key loser")

            else:
                if self.maze[x][y] == 2:
                    Chris.fight(self.enemy2)
                elif self.maze[x][y] == 3:
                    Chris.fight(self.enemy3)
                    print("The enemy dropped a potion and you pick it up")
                    Chris.potion += 1
                    print("You have " + str(Chris.potion) + " potions, use them wisely")
                elif self.maze[x][y] == 8:
                    Chris.fight(self.enemy8)
                elif self.maze[x][y] == 7:
                    Chris.fight(self.enemy7)

                elif self.maze[x][y] == 11:
                    Chris.fight(self.hardEnemy11)
                    randWeapon = random.choice(self.items)
                    print(randWeapon)
                    print("There is a weapon on the floor and you pick it up")
                    Chris.weapon = randWeapon[0]
                    Chris.attack = randWeapon[1]
                    print("Your weapon is now " + str(randWeapon[0]) + " and it can deal up to " + str(randWeapon[1]) + " damage")
                elif self.maze[x][y] == 13:
                    self.hardEnemy13.health = 150
                    Chris.fight(self.hardEnemy13)
                    print("The enemy dropped a key and you picked it up")
                    Chris.key = True

        self.updateVisited(x, y)

    def goNorth(self):
        if self.moveCount < self.totalMoves:
            if self.positionX != 0 and self.maze[self.positionX-1][self.positionY] != "x":
                self.updateDirection("North")
                self.positionX -= 1
                self.moveCount += 1
                robo.moveForward()
                self.checkEnemy(self.positionX, self.positionY)
            else:
                print("no path to the north")
        else:
            print("Game Over, Out Of Moves")

    def goEast(self):
        if self.moveCount < self.totalMoves:
            if self.positionY != 4 and self.maze[self.positionX][self.positionY+1] != "x":
                self.updateDirection("East")
                self.positionY += 1
                self.moveCount += 1
                robo.moveForward()
                self.checkEnemy(self.positionX, self.positionY)
            else:
                print("no path to the east")
        else:
            print("Game Over, Out Of Moves")
            sys.exit(0)

    def goSouth(self):
        if self.moveCount < self.totalMoves:
            if self.positionX != 4 and self.maze[self.positionX+1][self.positionY] != "x":
                self.updateDirection("South")
                self.positionX += 1
                self.moveCount += 1
                robo.moveForward()
                self.checkEnemy(self.positionX, self.positionY)
            else:
                print("no path to the south")
        else:
            print("Game Over, Out Of Moves")
            sys.exit(0)

    def goWest(self):
        if self.moveCount < self.totalMoves:
            if self.positionY != 0 and self.maze[self.positionX][self.positionY-1] != "x":
                self.updateDirection("West")
                self.positionY -= 1
                self.moveCount += 1
                robo.moveForward()
                self.checkEnemy(self.positionX, self.positionY)
            else:
                print("no path to the west")
        else:
            print("Game Over, Out Of Moves")
            sys.exit(0)

Chris = Player()
newMaze = Maze()
robo = robot.KeyControl()

#TODO will have a robot object here too
#have functions listen and speak
#listen will start the listening and do stuff with if
    #if listen == North etc
#speak will replace almost all of the print statements
#TODO need animation functions as well
    #have function for fighting animation, recharge animation, key animation, and

while True:
    newMaze.getPaths()
    print(str(newMaze.moveCount) + "/" + str(newMaze.totalMoves))
    #robo.speechCommand()
    try:
        choice = robo.speechCommand()
        #choice = int(input("1: North / 2: East / 3: South / 4: West : "))
    except:
        print("Invalid Input")
        choice = 0

    if choice.lower() == "north":
        #newMaze.updateDirection("North")
        newMaze.goNorth()
    elif choice.lower() == "east":
        #newMaze.updateDirection("East")
        newMaze.goEast()
    elif choice.lower() == "south":
        #newMaze.updateDirection("South")
        newMaze.goSouth()
    elif choice.lower() == "west":
        #newMaze.updateDirection("West")
        newMaze.goWest()
    elif choice.lower() == "exit":
        sys.exit(0)
    elif choice == 0:
        pass
    else:
        print("Invalid Input")
