#Задача
print('Приветствую тебя! Реши в уме уравнение x=(a+b)^a и проверь себя!');
a=input('Введите значение переменной a:');
print(a);
b=input('Введите значение переменной b:');
print(b);
print('Какой ответ получился у тебя?');
answer=int(input('Введи свой ответ:'));
decision=(int(a)+int(b))**int(a);
k=((print('Правильный ответ на уравнение x=(a+b)^a:',(int(a)+int(b))**int(a))));
if answer == decision:
    print('Ты Молодец!');
else:
    print('Учи алгебру!');
