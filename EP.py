# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 21:35:52 2018

@author: Samuel Porto
"""

estoque={}

continua=True

while continua:
    print('''
          Controle de estoque
          0-sair
          1-adicionar item
          2-remover item
          3-alterar item
          4-imprimir estoque
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
            quantidade=int(input('Quantidade inicial: '))
            if quantidade<0:
                print('A quantidade inicial não pode ser negativa!')
            else:
                estoque[nome]=quantidade
                
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
            quantidade=int(input('Quantidade: '))
            estoque[nome]+=quantidade
            print('Novo estoque de {0}: {1}' .format(nome,estoque[nome]))
    else:
        print(estoque)




















