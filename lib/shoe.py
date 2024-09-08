#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand='Adidas', size=9,):
       self.brand = brand
       self._size = size

    def get_size(self):
       return self._size

    def set_size(self, value):
       if isinstance(value, int):
         self._size = value
       else:
         print("size must be an integer")
         return
    size = property(get_size, set_size)
    

    def cobble(self):
       print("Your shoe is as good as new!")
       self.condition = "New"  