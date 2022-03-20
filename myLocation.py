class Location:

    def __init__(self, name, country):
        self.name = name
        self.country = country

    def mylocation(self):
        print("Hi, my name is " + self.name + "and i lives in " + self.country + ".")

loc1= Location("Thomas ","Portugal")
loc2 = Location("Ying", "China")
loc3 = Location("Amare", "Kenya")
your_loc = Location("Emman ", "Philippines")

loc1.mylocation()
loc2.mylocation()
loc3.mylocation()
your_loc.mylocation()


       
#loc = Location("JOHN EMMANUEL AQUINO", "Philippines")
#print(loc.name)
#print(loc.country)
#print(type(loc))