# my_file = open('file.txt')

# print(my_file.read())

# print(my_file.readline())

# my_file.close()

from translate import Translator
translator= Translator(to_lang="ja")
try:
    with open('./sad.txt', mode='r') as my_file:
     text = my_file.read()
     trans = translator.translate(text)
     with open('./sad-ja.txt', mode='w') as my_file2:
         my_file2.write(trans)
except FileNotFoundError as err:
    print("file not found")
    raise err

