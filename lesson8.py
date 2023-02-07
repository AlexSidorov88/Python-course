text = 'lorem ipsum dolor sit amet, consectetur adipiscing elit'
#print(word.count('s'))
#print(word.capitalize())
#print(word.find('lo'))
word = (text.split(' '))   # перебираем текст на слова и делаем всем словам заглавные буквы

for x in range(len(word)):
   word[x] = word[x].capitalize()

result = ", ".join(word)  # из массива делаем строку
print(result)
