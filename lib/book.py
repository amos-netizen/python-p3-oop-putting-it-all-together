#!/usr/bin/env python3

class Book:
   def __init__(self, title="And Then There Were None", page_count=272):
    self.title = title
    self._page_count = page_count  

   def get_page_count(self):
     return self._page_count

   def set_page_count(self, value):
      if isinstance(value, int):
        self._page_count = value
      else:
        print("page_count must be an integer")
        return
   
   page_count = property(get_page_count, set_page_count)

   def turn_page(self):
    print("Flipping the page...wow, you read fast!")
 