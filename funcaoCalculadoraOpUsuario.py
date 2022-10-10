def calculadora(n1=1,n2=1,op=1) :
    
    if(op == 1) :
        res = n1 + n2
    elif(op == 2) :
        res = n1 - n2
    elif(op == 3) :
        res = n1 * n2
    elif (op == 4)  :
        res = n1 / n2
    else:
        res = "erro"
    return res
    
a = 1        
while (a != 0):
    
    print("Selecione a operação que quer fazer de acordo com o menu abaixo:")
    print("1.Soma\n2.Subtração\n3.Multiplicação\n4.Divisão\n0.Sair")
    n = int(input())
    
    if (n == 0):
        a = n
    
    else:
    
        resultado = calculadora(op = n)

        if (resultado == "erro" ):

            print("Essa opção não existe!\n")
            
        else:
            
            print("Digite o primeiro numero:")
            n1 = int(input())
            print("Digite o segundo numero:")
            n2 = int(input())

            resultado = calculadora(n1,n2,n) 
            print("O resultado da operação é:",resultado,"\n")
             