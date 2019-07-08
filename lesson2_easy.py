#Task2
a={'Apple','Fish','Orange'}
b={'Pop','Apple','Orange'}
print(a-b)


#Task3
print('Задача 3.'
      'Дан массив [2,3,4,9,17,202,999]')
name=[2,3,4,9,17,202,999]
p=list(filter(lambda x: x%2 != 0, name))
print('Нечетные, умноженное на 2:',p)
for i in p:
   print(i,'* 2 =', i*2)

k=list(filter(lambda x: x%2 ==0, name))
print('Четные, деленные на 4:',k)
for i in k:
    print(i, '/ 4 =', i/4)

#Task1
my_string="1. {} 2. {} 3.  {} 4. {}"
k=print(my_string.format("Яблоко", "банан", "киви", "арбуз"))