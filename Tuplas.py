lanche = ('Hambúrguer' , 'Suco' , 'Pizza' , 'Pudim' , 'Batata Frita')
#TUPLAS SÃO IMUTÁVEIS!!!
for comida in lanche:  # O Python inicializa uma variável "comida" para a tupla "lanche"
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print('Comi pra caramba!')
for pos, comida in enumerate(lanche):  #Alem do dado me da a posiçao, 2 variaveis separadas por virgulas
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')
#Ambos levam ao mesmo resultado


print(sorted(lanche))  #Imprime a tupla em ordem alfabética

'''a = (2, 5, 4)
b = (5, 8, 1, 2)
c = (b + a)
print(c)
print(len(c))  #tamanho da tupla
print(c.count(5))  #quantas vezes o elemento 5 aparece na tupla c 
print(c.index(8))  #em que posição esta o elemento 8 na tupla c (primeira ocorrencia)
print(c.index(5, 1))  #em que posição esta o elemento 5 na tupla c depois da posição 1
del(lanche)  #apagando a variavel "lanche"
'''