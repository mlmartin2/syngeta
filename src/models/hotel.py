
hrates = {
    0: { # default
        0: 0, #weekday
        1: 0  #weekend
    },
    1: { # reward
        0: 0,
        1: 0
    }
}

class Hotel():
    name = ''
    classification = -1
    rates = {}

    def __init__(self, name, classification, defday, premday, defend, premend ):
        self.name = name
        self.classification = classification
        self.rates = {
        0: { # default
            0: defday, #weekday
            1: defend  #weekend
        },
        1: { # reward
            0: premday,
            1: premend
        }
}

    def __str__(self):
        return('name:' + self.name + 
        ',classification:' + str(self.classification) + 
        ',rates: weekday:' +  
        str(self.rates[0][0]) + ',' 
        + str(self.rates[1][0])  
        + ',weekend:' + str(self.rates[0][1])  
        + ',' + str(self.rates[1][1]))

    def get_price(self, user_classification = 0, weekdays = []):
        price = 0
        for day in weekdays:
            price += self.get_rate(user_classification, day)
        return price

    def get_rate(self, user_classification = 0, weekday = 0):
        day = 0
        if(weekday == 5 or weekday == 6):
            day = 1
        return self.rates[user_classification][day]

def teste():
    h = Hotel('Ridgewood', 5, 220, 100, 150, 40)
    print(h)

teste()