# Decodificador para o argumento padrão usado no projeto
# >> Formato: <Subscription>:<Date1>,<Date2>,<Date3>,...,<DateN>
# - Funções para extrair dados úteis do argumento fornecido.
# - Apenas utilizar decode_defaultArgument() externamente,
#   demais funções/dicionários tem apenas finalidades internas 

# Dicionário p/ dias da semana
weekdays = {
    'mon':0,
    'tues':1,
    'wed':2,
    'thur':3,
    'fri':4,
    'sat':5,
    'sun':6
}

# Dicionário p/ tipos de assinatura
subscriptions = {
    'Regular': 0,
    'Rewards': 1,
}

# Separadora do argumento padrão
# Recebe argumento padrão
# Retorna array de formato:
# [0] = string : Default/Rewards
# [1] = string[date1, date2, ..., dateN] : Dias da semana marcados
def slice_defaultArgument(default_argument):
    argedit = default_argument.rpartition(':')
    subscription = argedit[0]
    dates = (argedit[2]).split(',')
    return [subscription, dates]

# Getter do valor numérico do dia da semana por string
# Recebe string de formato 'DDMonthYYYY(weekday)' | ex: '16Mar2009(mon)' 
# Retorna valor númerico do dia da semana ( 0: segunda-feira -> 6: domingo)
def get_weekdayValue_fromString(str):
    weekday_part = str.rpartition('(')
    weekday = weekday_part[2].removesuffix(')')
    return weekdays[weekday]

# Decodificador do argumento padrão fornecido no desafio
# Recebe argumento padrão <Subscription>:<Date1>,<Date2>,<Date3> (ex: Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed))
# Retorna valores númericos dos dados ([assinatura, [weekday1, weekday2, ..., weekdayN]])
def decode_defaultArgument(default_argument):
    sliced_argument = slice_defaultArgument(default_argument)
    subscription = subscriptions[sliced_argument[0]]
    weekdays = []
    for date in sliced_argument[1]:
        weekdays.append(get_weekdayValue_fromString(date))
    return [subscription, weekdays]
