#numero_inserido = input("Insira algum número: ")
numero_inserido = 5

if float(numero_inserido) % 1 == 0:
    numero_inserido = int(numero_inserido)
    if numero_inserido % 2 == 0:
        print("Par")
    else:
        print("Ímpar")

else:
    print("Erro")


print("\nExercício 2\n")

#data_inserida = input("Informe as horas: ")
data_inserida = '00:00'

if data_inserida[2] != ':':
    print("Erro! - Data em formato errado")
else:
    if int(data_inserida[0] + data_inserida[1]) >= 18:
        print("Boa noite")
    elif int(data_inserida[0] + data_inserida[1]) >= 12:
        print("Boa Tarde")
    else:
        print("Bom dia")
        
print("\nExercício 3\n")

#nome_inserido = input("Qual seu nome?  ")
nome_inserido = 'Médio'

if len(nome_inserido) >= 8:
    print("Nome Grande")
elif len(nome_inserido) >=5:
    print("Nome Médio")
else: 
    print("Nome Pequeno") 