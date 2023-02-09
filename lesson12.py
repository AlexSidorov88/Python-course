user_text = input('Write your message: ')  #записываем текст с консоля в текстовый файл

file = open('text.txt', 'a' )

file.write(user_text + "\n")

file.close()
