string = str(input('Введите сообщение на английском'))
string.lower()
check = True
while check:
    for i in range(len(string)):
        if ord(string[i]) not in range(96, 123):
            print('Не корректная строка')
            string = str(input())
            check = True
            break
        else:
            check = False

check = True
word = str(input('Введите ключевое слово'))
word.lower()
while check:
    for i in range(len(string)):
        if ord(string[i]) not in range(96, 123):
            print('Не корректная строка')
            string = str(input())
            check = True
            break
        else:
            check = False

if len(string) > len(word):
    word *= len(string)//len(word)+1

for i in range(len(string)):
    if ord(string[i])+ord(word[i])-96 > 122:
        print(chr(ord(string[i]) + ord(word[i]) - 122), end=' ')
    else:
        print(chr(ord(string[i])+ord(word[i])-96), end=' ')
