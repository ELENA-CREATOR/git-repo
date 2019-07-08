#Task3

def max_words(*args):
    max_str = ''
    for arg in args:
        if len(arg) > len(max_str):
            max_str = arg
    return max_str


print(max_words(
    'You','are','your', 'only', 'limit'
    ))


#Task2
def max_number(*args):
    max_num = 0
    for arg in args:
        if arg > max_num:
            max_num = arg
    return max_num


print(max_number(8,10,10000,53999))


#Task1
def user_map(name, age, city):
    str_user = f'{name}, {age} год(а), проживает в городе {city}'
    return str_user


print(user_map('Василий', '21', 'Москва'))
