# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 21:35:52 2018

@author: Samuel Porto ft. Roger Pina
"""
import json

with open('arquivo.txt','r') as arquivo:
    conteudo=arquivo.read()
    estoque=json.loads(conteudo)

continuacao=True

while continuacao:
    print('''
          Controle de estoque
          0-sair
          1-adicionar item
          2-remover item
          3-alterar item
          4-imprimir estoque
          5-produtos faltando
          6-valor total do estoque
          ''' 
          )

    escolha=int(input('Faça sua escolha:'))

    if escolha==0:
        continuacao=False
        print('Até um outro dia')

    
    elif escolha>6 or escolha<0:
        print('Operação inválida!')        

    elif escolha==1:
        continua=True
        nome=input('Nome do produto: ')    
        if nome in estoque:
            print('Produto já cadastrado')
            continua=False
        while continua:
                valor=float(input('Valor unitário em reais: '))
                if valor<0:
                    print('O preço não pode ser negativo!')
                else:
                    break
        while continua:
            quantidade=int(input('Quantidade inicial: '))
            if quantidade<0:
                print('A quantidade inicial não pode ser negativa!')
            else:
                estoque[nome]=quantidade,valor
                print('{0} adicionado por {1} reais a unidade' .format(nome,estoque[nome][1]))
                break
            
                
    elif escolha==2:
        while True:
            nome=input('Nome do produto (0 para sair): ')
            if nome=='0':
                break
            elif nome not in estoque:
                print('Elemento não encontrado!')
            else:
                del estoque[nome]
            
    elif escolha==3:
        while True:
            nome=input('Nome do produto (0 para sair): ')
            if nome=='0':
                break
            elif nome not in estoque:
                print('Elemento não encontrado!')
            else:
                while True:
                    valor=float(input('Valor unitário em reais (0 para manter o preço): '))
                    if valor == 0:
                        break
                    elif valor<0:
                        print('O preço não pode ser negativo!')
                    else:
                        estoque[nome][1]=valor
                        print(estoque[nome][1])
                        break
                quantidade=int(input('Alteração na quantidade (0 para não alterar o estoque): '))
                variavel=estoque[nome][0]
                estoque[nome][0]=variavel+quantidade                
                print('Novo estoque de {0}: {1} unidades, {2} reais cada' .format(nome,estoque[nome][0],estoque[nome][1]))
                break
            
    elif escolha==4:
        print('Os produtos no estoque são:')
        for i in estoque:
            print('{0}: {1} itens, preço: {2} a unidade' .format(i,estoque[i][0],estoque[i][1]))
        
    elif escolha==5:
        lista=[]
        for i in estoque:
            if estoque[i][0]<0:
                lista.append(i)
        print('Os produtos em falta são:')
        for e in lista:
            print(e)
    
    else:
        total=0
        for i in estoque:
            valor_produtos=estoque[i][1]*estoque[i][0]
            total+=valor_produtos
        print('O valor monetário total do estoque em reais é: {0}' .format(total))  
        

        
with open ('arquivo.txt','w') as arquivo:
    estoque_js=json.dumps(estoque,sort_keys=True,indent=4)
    conteudo=arquivo.write(estoque_js)

















