"""
homework from week 3 and 4 labs for devops class
python review, Cisco lab Python Classes Review 3.4.6
~~ here is a change to prove I can push a change ~~
"""


def my_city(city):
    # function name revised to pep 8 instead of myCity
    print(f'I live in {city}.')
    # used f strings instead of the clunky code from assignment: print("I live in " + city + ".")


class Location:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def my_location(self):
        print(f'Hi my name is {self.name}. I live in {self.country}')


# create an instance of Location, kwargs specified instead of using positional arguments as
# in the instructions because it makes the code easier to understand and is better practice
loc = Location(name='Fred', country='Cisco Land')

print(loc.name, loc.country)
print(type(loc))

loc.my_location()
# call the method from the above instance of the Location class

# First instantiation of the class Location - copy pasta from assignment
loc1 = Location("Tomas", "Portugal")
loc1.my_location()
# another instance
your_loc = Location("Your_Name", "Your_Country")

# more examples, more of the same ... not copy pasta
loc2 = Location(name='Wilbur', country='USA')
loc3 = Location(name='Velma', country='France')
# creating instances

loc2.my_location()
loc3.my_location()
your_loc.my_location()
# calling methods
