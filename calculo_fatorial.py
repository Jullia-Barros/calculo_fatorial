("######################")
("Olá, vamos calcular o fatorial de um número")
("######################")

# No programa você irá digitar um número e ele calculara-rá seus anteriores!

n= int (input ("Digite un número para calcular seu fatorial: "))
c= n
f =1
print ('Calculando {}! = '.format(n), end='')
while(c > 0):
    print ('{}'.format(c), end='')
    print ('x' if c > 1 else '=', end='')
    f *= c
    c -= 1
print ('{}'.format(f))

print("Obrigada por sua participação!!")
