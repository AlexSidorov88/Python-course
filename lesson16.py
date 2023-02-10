class Auto:
   name = None
   model = None
   price = None

   def set_data(self, name, model, price):     #method
      self.name = name
      self.model = model
      self.price = price
   def get_data(self):
      print(self.name, "model:", self.model, "price:", self.price)

auto1 = Auto()
auto1.set_data('Toyota', 'Rav4', 25000)
#auto1.name = 'Toyota'
#auto1.model = 'Rav4'
#auto1.price = 25000

auto2 = Auto()
auto2.set_data('BMW', 'X5', 40000)
#auto2.name = 'BMW'
#auto2.model = 'X5'
#auto2.price = 40000
auto1.get_data()
auto2.get_data()