from unittest import TestCase
from src.my_module import get_cheapest_hotel
from src.decoder.argdecoder import *

class MyTest(TestCase):
    def test1(self):
        result = "Lakewood"
        self.assertEqual(result, get_cheapest_hotel("Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"))

    def test2(self):
        result = "Bridgewood"
        self.assertEqual(result, get_cheapest_hotel("Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)"))

    def test3(self):
        result = "Ridgewood"
        self.assertEqual(result, get_cheapest_hotel("Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)"))
    
    def test6(self):
        result = [1, [0,1,2]]
        self.assertEqual(result, decode_defaultArgument("Rewards: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"))

    def test7(self):
        result = [1, [2,3,4]]
        self.assertEqual(result, decode_defaultArgument("Rewards: 16Mar2009(wed), 17Mar2009(thur), 18Mar2009(fri)"))

    def test8(self):
        result = 0
        self.assertEqual(result, get_weekdayValue_fromString('(mon)'))

    def test9(self):
        result = 6
        self.assertEqual(result, get_weekdayValue_fromString('(sun)'))