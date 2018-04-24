# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 21:35:52 2018

@author: Samuel Porto
"""
import json

with open('arquivo.txt','r') as arquivo:
    conteudo=arquivo.read()
    estoque=json.loads(conteudo)

continua=True

while continua:
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

    escolha=int(input('Faça sua escolha: '))

    if escolha==0:
        print('Até um outro dia')
        continua=False

    elif escolha==1:
        nome=input('Nome do produto: ')    
        if nome in estoque:
            print('Produto já cadastrado')        
        else:
            valor=float(input('Valor unitário em reais: '))
            if valor<0:
                print('O preço não pode ser negativo!')
            else:
                quantidade=int(input('Quantidade inicial: '))
                if quantidade<0:
                    print('A quantidade inicial não pode ser negativa!')
                else:
                    estoque[nome]=quantidade,valor
                
    elif escolha==2:
        nome=input('Nome do produto: ')
        if nome not in estoque:
            print('Elemento não encontrado')
        else:
            del estoque[nome]
            
    elif escolha==3:
        nome=input('Nome do produto: ')
        if nome not in estoque:
            print('Elemento não encontrado')
        else:
            valor=float(input('Novo valor unitário em reais: '))
            if valor<0:
                print('O preço não pode ser negativo!')
            else:
                quantidade=int(input('Alteração na quantidade: '))
                variavel=estoque[nome][0]
                estoque[nome][0]=variavel+quantidade
                estoque[nome][1]=valor                
                print('Novo estoque de {0}: {1} unidades, {2} reais cada' .format(nome,estoque[nome][0],estoque[nome][1]))
    
    elif escolha==4:
        print(estoque)
        
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

















