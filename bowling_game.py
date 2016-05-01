
class Game():

    rolls = [0] * 21 # if perfect game get extra roll at end
    currentRoll = 0

    def roll(self, pins):
        self.rolls[self.currentRoll] = pins
        self.currentRoll += 1

    def score(self):
        myScore = 0
        for i, val in enumerate(self.rolls):
            myScore += val

        return myScore