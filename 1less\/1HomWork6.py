# 6. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

if a + b <= c or a + c <= b or b + c <= a:
    print('Треугольник не существует!')
elif a != b and a != c and b != c:
    print('Треугольник разностороний')
elif a == b == c:
    print('Треугольник равностороний')
else:
    print('Треугольник равнобедренный')
