class animal:
    def __init__(self, is_eating , is_plying , name):
        self.name = name
        self.is_eating = is_eating
        self.is_plying = is_plying
    def describe(self):
        print(f"{self.is_eating}and {'happy' if self.is_plying else 'sad'}")
class rabbit(animal):
    def __init__(self, color, is_happy , is_playing , is_eating , name):
        super().__init__(is_playing , is_eating , name)
        self.color = color
        self.is_happy = is_happy
class dog(animal):
    def __init__(self, color, is_happy , is_playing , is_eating , name):
        super().__init__(is_playing , is_eating , name)
        self.color = color
        self.is_happy = is_happy
class cat(animal):
    def __init__(self, color, is_happy , is_playing , is_eating , name):
        super().__init__(is_playing , is_eating , name)
        self.color = color
        self.is_happy = is_happy
catty = cat(name = "gool" ,color = "red", is_happy = True , is_playing = False , is_eating = True)
doggy = dog(name = "doggy",color="brown", is_happy = True , is_playing = True , is_eating = False)
rabitty  = rabbit(name= "slime" ,color="white", is_happy = False , is_playing = False , is_eating = False)
doggy.describe()
catty.describe()
rabitty.describe()
