'''pessoas = {'Nome':'Gustavo', 'Sexo':'M', 'Idade': 22}
#del pessoas['Sexo']   # Comando del para apagar alguma key no dicionario
pessoas['Peso'] = 98.5
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())
for k,v in pessoas.items():
    print(f'{k} = {v}')

brasil = []
estado1 = {'uf':'Rio de Janeiro','sigla':'RJ'}
estado2 = {'uf':'São Paulo', 'sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])'''

estado = dict()
brasil = list()
for c in range (0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:   # Para cada estado em brasil
    for k,v in e.items():
        print(f'{k} = {v}.')
