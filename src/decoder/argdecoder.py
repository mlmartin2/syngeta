weekdays = {
    'mon':0,
    'tues':1,
    'wed':2,
    'thur':3,
    'fri':4,
    'sat':5,
    'sun':6
}

def arg_slicer(arg):
    argedit = arg.rpartition(':')
    subs = argedit[0]
    dates = (argedit[2]).split(',')
    return [subs, dates]

def arg_decoder(arg):
    args = arg_slicer(arg)
    subs = subscription_from_arg(args[0])
    weekdays = []
    for date in args[1]:
        weekdays.append(weekday_from_arg(date))
    return [subs, weekdays]

def subscription_from_arg(str):
    subs = 0
    if str == 'Rewards':
        subs = 1
    return subs

def weekday_from_arg(str):
    part = str.rpartition('(')
    wday = part[2].removesuffix(')')
    return weekdays[wday]