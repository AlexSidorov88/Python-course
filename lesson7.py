n = int(input("Enter length: "))  # программа(создаем список, устанавливаем размер, наполняем, выводим)

user_list = []

i = 0 

while i < n:
   string = "Enter element #" + str(i + 1) + ":"
   user_list.append(input(string))
   i += 1

print(user_list)