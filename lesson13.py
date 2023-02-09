x = 0 

while x == 0:
   try:
         x = int(input("Enter num: ")) 
         x += 5 
         print(x)
   except ValueError:
      print("It is not number!")