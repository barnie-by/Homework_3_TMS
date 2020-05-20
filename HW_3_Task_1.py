print('Введите список из чисел по возрастанию')
spisok = list(map(int,input().split()))
print(spisok)
n=int(input('Введите число из списка: '))
x=spisok.index(n)
print(f'Идекс введенного числа в списке:  {x}')


