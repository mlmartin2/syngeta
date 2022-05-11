from src.models.hotel import Hotel
from datetime import date
from src.decoder.argdecoder import arg_decoder

_arg = "Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)"

lake = Hotel('Lakewood', 3, 110, 80, 90, 80)
bridge = Hotel('Bridgewood', 4, 160, 110, 60, 50)
ridge = Hotel('Ridgewood', 5, 220, 100, 150, 40)

hotels = [lake, bridge, ridge]

def get_weekday(day, month, year):
    d = date(day=day, month=month, year=year)
    return d.weekday() 

def get_cost(hotel, arg):
    args = arg_decoder(arg=arg)
    return hotel.get_price(args[0], args[1])

def get_cheapest_hotel(arg):   #DO NOT change the function's name
    cheapest_hotel = ''
    price = 0
    for hotel in hotels:
        cost = get_cost(hotel, arg)
        if(price == 0): 
            price = cost
            cheapest_hotel = hotel
        elif price > cost:
            price = cost
            cheapest_hotel = hotel
        elif cost == price:
            if cheapest_hotel.classification < hotel.classification:
                cheapest_hotel = hotel
    return cheapest_hotel.name

print(get_cheapest_hotel(_arg))

#print(lake.get_rate(1, get_weekday(8, 5, 2022)))
