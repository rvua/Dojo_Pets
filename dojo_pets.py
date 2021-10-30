class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
      self.first_name = first_name
      self.last_name = last_name
      self.pet = pet
      self.treats = treats
      self.pet_food = pet_food

    def walk(self):
        print(f"Taking {self.first_name} for a walk.")

    def feed(self):
        print(f"Time to feed {self.first_name} her {self.pet_food}.") 

    def bathe(self):
        print(f"Time to bathe {self.first_name}.")

class Pet: 
    def __init__(self, name, type, tricks, health, energy):
        self.name = name 
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy 
        self.ninja = Ninja('sally', 'jones', 'dog', 'bone', 'kibble')
    
    def sleep(self):
        print(f"Put {self.name} to sleep.")

    def eat(self):
        self.ninja.feed()
        print(self.ninja.pet_food)

    def play(self):
        self.ninja.walk()
        print(f"Take {self.name} for a walk and give her a {self.ninja.treats}")

    def noise(self):
        self.ninja
        print(f"{self.name} is very {self.energy} right now. Please give her a {self.ninja.treats}")

sally = Pet('sally', 'dog', 'shakes', 'healthy', 'hyper') 
ninja = Ninja('sally', 'jones', 'dog', 'bone', 'kibble')
ninja.feed()
ninja.walk()
ninja.bathe()
sally.eat()
sally.play()
sally.noise()