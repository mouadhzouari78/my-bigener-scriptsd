class shape:
    def __init__(self , color , is_filled):
        self.is_filled = is_filled
        self.color = color

class triangle(shape):
    def __init__(self , name , hight ,widht , color , is_filled):
        super().__init__(color , is_filled)
        self.name = name
        self._hight = hight
        self._widht = widht
    def mise7a(self):
        print(f"el mise7a is {self._hight * self._widht}cm")




class square(shape):
    def __init__(self , name , color , length , is_filled):
        super().__init__(color , is_filled)
        self.name = name
        self._length = length
    @property
    def length(self):
        return f"{self._length}cm"
    def mise7a(self):
        print(f"el mise7a is {self._length * self._length}")
shape1 = triangle("triangle" , 5 , 5 ,  "red" , True )
shape2 = square("square" , "yellow" , 5 , True )
print(shape1.mise7a())
print(shape2.length)