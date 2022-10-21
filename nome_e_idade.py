print("Digite seu nome completo: ")
nome = input()

print("Digite seu ano de nascimento(entre 1922 e 2022): ")

try :

    ano = int(input())
    if (ano < 1922) or (ano > 2022 ) :
        
        while True:
            print("ano fora do intervalo solicitado, digite novamente.")
            print('Digite o ano do nascimento :')
            ano = int(input())
            
            if (ano > 1922) and (ano < 2022) :
                break 
             
except ValueError as error:
    print("voce não digitou um numero valido, digite novamente.")
    
    while True:
        try:
            print('Digite o ano de nascimento :')
            ano=int(input())
            break
        
        except:
            print('Numero invalido')
finally:

    idade = 2022 - ano
    print("{} completou ou completará {} anos esse ano.".format(nome,idade))