# first we create the class/template
class Human:
    
    # class attributes
    legs = 2
    hands = 4
    head = 1
    ears = 2

    # create a constructor method
    def __init__(self, first_name, last_name, nationality, language, country) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.nationality = nationality
        self.language = language
        self.country = country

    # create an object method
    def bio(self):
        print(f'Hi, my name is {self.first_name} and I am from {self.country}')

# create objects
Jane = Human('Jane', 'Robertson', 'American', 'English', 'USA')
Anna = Human('Anna', 'Lubova', 'Mongolian', 'Russian', 'Russia')

Jane.bio()
Anna.bio()



# print(f'{Jane.first_name} is from {Jane.country} and speaks {Jane.language}')
# print(f'{Anna.first_name} is from {Anna.country} and speaks {Anna.language}')
# print(f'{Anna.first_name} has {Anna.hands} hands')