
class Game():

    rolls = [0] * 21 # if perfect game get extra roll at end
    currentRoll = 0

    def roll(self, pins):
        self.rolls[self.currentRoll] = pins
        self.currentRoll += 1

    def score(self):

        myScore = 0
        currentRoll = 0

        for frame in range(0, 10):
            if (self.isSpare(currentRoll)):
                myScore += 10 + self.rolls[currentRoll + 2]
            else:
                myScore += self.rolls[currentRoll] +  self.rolls[currentRoll + 1]

            currentRoll += 2
        return myScore

    def isSpare(self, currentRoll):
        return self.rolls[currentRoll] + self.rolls[currentRoll + 1] == 10

