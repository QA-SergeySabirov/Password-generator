from random import*
def generate_password(length, chars):
    password = ''
    for i in range(length):
        password += choice(chars)
    return password

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''


def digit_rule(g, text): #проверка чисел
    while g.isdigit() == False:
        print("\033[31m{}".format('Ошибка введите цифру'))
        print("\033[0m".format(''))
        g = input(text)
    return g

n = input('Количество паролей ')
text_n = 'Количество паролей '
n = int(digit_rule(n, text_n))


lenght = input('Длина одного пароля ')
text_lenght = 'Длина одного пароля '
lenght = int(digit_rule(lenght,text_lenght))

def answer_rule(answer, text):#проверка ответа да/нет
    while answer not in ['да', 'нет']:
        print("\033[31m{}".format('Введите "да" или "нет"'))
        print("\033[0m".format(''))
        answer = input(text)
    return answer

dig = input('Включать цифры? (да/нет) ').lower()
text_dig = 'Включать цифры? (да/нет) '
dig = answer_rule(dig, text_dig)

p = input('Включать прописные буквы? (да/нет) ').lower()
text_up_let = 'Включать прописные буквы? (да/нет) '
p = answer_rule(p, text_up_let)

str = input('Включать строчные буквы? (да/нет) ').lower()
text_down_let = 'Включать строчные буквы? (да/нет) '
str = answer_rule(str, text_down_let)

sym = input('Включать символы? (да/нет) ').lower()
text_sym = ('Включать символы? (да/нет) ')
sym = answer_rule(sym, text_sym)

exception = input('Исключать неоднозначные символы il1Lo0O? (да/нет) ').lower()
text_exception = 'Исключать неоднозначные символы il1Lo0O? (да/нет) '
exception = answer_rule(exception, text_exception)

if dig == 'да':
    chars += digits
if p == 'да':
    chars += uppercase_letters
if str == 'да':
    chars += lowercase_letters
if sym == 'да':
    chars += punctuation
if exception == 'да':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')
print('\nВарианты паролей')

for _ in range(n):
    print(generate_password(lenght, chars))




