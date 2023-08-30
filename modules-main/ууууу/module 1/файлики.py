my_file = open('ff.txt', 'w', encoding='utf-8')
my_file.write('Привет!')
my_file.close()

my_file = open('ff.txt', 'r+', encoding='utf-8')
print(my_file.read())
my_file.write("Как дела?")
my_file.close()

my_file = open('ff.txt', 'a', encoding='utf-8')
my_file.write('Хорошо')
my_file.close()

