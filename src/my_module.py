from src.models.initHotels import hotels
from datetime import date
from src.decoder.argdecoder import decode_defaultArgument

def get_cheapest_hotel(default_argument):
    cheapest_hotel = ''
    cheapest_price = 0
    decoded_argument = decode_defaultArgument(default_argument)
    for hotel in hotels:
        cost = hotel.get_price(decoded_argument[0], decoded_argument[1])
        if cheapest_price == 0 or cheapest_price > cost: 
            cheapest_price = cost
            cheapest_hotel = hotel
        elif cost == cheapest_price and cheapest_hotel.classification < hotel.classification:
            cheapest_hotel = hotel
    return cheapest_hotel.name

