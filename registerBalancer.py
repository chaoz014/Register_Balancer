class register():

    def __init__(self, pennies, nickles, dimes, quarters, pen_roll, nick_roll, dim_roll, quart_roll, singles, twos, fives, tens, twenties, fifties, hundreds, misc_change):
        self.pennies = pennies*.01
        self.nickles = nickles*.05
        self.dimes = dimes*.1
        self.quarters = quarters*.25
        self.pen_roll = pen_roll*.5
        self.nick_roll = nick_roll*2
        self.dim_roll = dim_roll*5
        self.quart_roll = quart_roll*10
        self.singles = singles
        self.twos = twos*2
        self.fives = fives*5
        self.tens = tens*10
        self.twenties = twenties*20
        self.fifties = fifties*50
        self.hundreds = hundreds*100
        self.misc_change = misc_change

    def totalBalance(self):
        return (self.pennies + self.nickles + self.dimes + self.quarters + self.pen_roll +
            self.nick_roll + self.dim_roll +  self.quart_roll + self.singles + self.twos + self.fives +
            self.tens + self.twenties + self.fifties + self.hundreds + self.misc_change)

    def bal_135(self):
        return (self.totalBalance() - 135)

    def hasBalance(self):
        return (self.bal_135() < 0)

newReg = register(25, 10, 50, 8, 2, 1, 1, 1, 24, 10, 4, 5, 2, 3, 2, 0)
# y = input('enter something')
print(newReg)
print(newReg.totalBalance())
print(newReg.pennies)
print(newReg.bal_135())
print(529.75)
print(newReg.hasBalance())
