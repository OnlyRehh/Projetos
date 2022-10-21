votoX = 0
votoY = 0
votoZ = 0
votoBranco=0
votoNulo=0

print('='*55)

print('ELEIÇAO')
print('Vote em um dos candidatos abaixo digitando seu numero\ncorrespondente\nOu tecle 0 para votar em branco')

print('='*55)

while True:

    print('\nCandidato X - 889\nCandidato Y - 847\nCandidato Z - 515\n')
    
    try:
    
        voto= int(input('vote:')) 
        
        if (voto == 889):
            votoX += 1  
        elif(voto == 847):
            votoY += 1    
        elif(voto == 515 ):
            votoZ += 1    
        elif(voto == 0):
            votoBranco += 1    
        else:
            votoNulo += 1
            
        
        print('Deseja finalizar a votacao?S/N')
        res= str(input())
        if (res == 'S') or (res == 's'):
            break
            
    except ValueError as error:
        print("Não é possivel votar por texto!\nEscolha um dos numeros entre os candidatos ou tecle 0 para votar em branco.")

if (votoX > votoY) and (votoX > votoZ):
    vencedor = 'o Candidato X '
elif(votoY > votoX) and (votoY > votoZ):
    vencedor = 'o Candidato Y'
elif(votoZ > votoX) and (votoZ > votoY):
    vencedor = 'o Candidato Z'
else:
    vencedor = 'Ninguém :/'
        
print('='*40)
print('VOTACAO ENCERRADA')
print('='*40)

print(f'O vencedor da eleição foi {vencedor}')
        
print(f'Candidato X - votos: {votoX}\nCandidato Y - votos: {votoY}\nCandidato Z - votos: {votoZ}' )
print(f'Votos Brancos:{votoBranco}\nVotos Nulos:{votoNulo}')



    







