from statistics import mode
print('Введите список из чисел по возрастанию')
spisok = list(map(int,input().split()))
c=(mode(spisok))
print(f'Встречается чаще всего число: {c}')