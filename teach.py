class student:
    def __init__(self, name, age, is_terrorist):
        self.is_terrorist = is_terrorist
        self.name = name
        self.age = age
class productive(student):
    def __init__(self, name, age, is_terrorist,is_productive):
        super().__init__(name , age , is_terrorist )
        self.is_productive = is_productive
sadok = productive("sadok", 60, True, False)
print(sadok.name)
print(sadok.age)
print(sadok.is_productive)
print(sadok.is_terrorist)
khalil = productive("khalil", 60, True, False)
p