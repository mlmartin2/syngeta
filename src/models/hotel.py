# Classe modelo para hotel, com campos fornecidos para o projeto
# nome, classificação, taxas diárias

class Hotel():
    name = ''
    classification = -1
    day_rates = {}

    def __init__(self, name, classification, defaultRate_weekDay, rewardsRate_weekDay, defaultRate_weekEnd, rewardsRate_weekEnd ):
        self.name = name
        self.classification = classification
        self.day_rates = {
            0: { # default
                0: defaultRate_weekDay,
                1: defaultRate_weekEnd 
            },
            1: { # reward
                0: rewardsRate_weekDay,
                1: rewardsRate_weekEnd
            }
        }

    def __str__(self):
        return('name:' + self.name + 
        ',classification:' + str(self.classification) + 
        ',rates:' + self.day_rates)

    # getter do preço relativo aos dias fornecidos
    # recebe assinatura associada ao usuário + dias da semana marcados
    # retorna preço total
    def get_price(self, user_subscription = 0, weekdays = []):
        price = 0
        for day in weekdays:
            rate = self.get_dayRate(day)
            price += self.day_rates[user_subscription][rate]
        return price
    
    # getter da taxa do dia da semana fornecido
    # recebe dia da semana ( valor numérico )
    # retorna taxa ( 0: dia de semana, 1: fim de semana)
    def get_dayRate(self, day):
        rate = 0
        if(day == 5 or day == 6):
            rate = 1
        return rate