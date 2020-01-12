#Antes de você criar uma ficha, você deve criar um arquivo txt na mesma pasta que o programa em python ou em uma subpasta na mesma pasta em que está situado o programa em python

print('Bem-vindo ao Programa de Fichas Python')
opcao1 = int(input('Qual opção vc quer:\n 1 - Buscar Ficha\n 2 - Criar Ficha\n Opcão: '))
#Essa parte é a Busca pela Ficha. 
#1. Primeiro ele irá ver qual é o nome do txt que está na mesma pasta que o mesmo ou em uma subpasta
#2. Após isso, ele irá procurar na pasta em que está este programa ou numa subpasta e irá ler linha por linha e imprimir na tela.
if opcao1 == 1:
    p = str(input('Nome: \n'))
    print('Dados de {}:'.format(p))
    arquivo = open('Fichas\{}.txt'.format(p), 'r')
    for linha in arquivo:
        linha = linha.rstrip()
        print (linha)
    arquivo.close()

#Essa parte é a da Obtenção de Dados e faz parte da Criação da Ficha
#Ele irá perguntar seus dados para colocar na ficha. A pergunta "Nome" tem que ser o mesmo nome que está no arquivo txt
if opcao1 == 2:
    p = str(input('Nome: '))
    n = str(input('Nome Completo: '))
    se = str(input('Sexo: '))
    i = int(input('Idade: '))
    s = str(input('Status: '))
    c = int(input('Contato: '))
    d = input('Data de Nascimento: ')
    l = str(input('Local de nascimento: '))
    e = input('E-mail: ')
		
#Agora que ele já obteve os dados, ele irá abrir o arquivo txt que tenha como Nome, o mesmo armazenado na variavel p, ou seja, na pergunta "Nome" e irá escrever no txt, os dados que foram dados pelo usuário.
arquivo = open('Fichas\{}.txt'.format(p), 'w')
arquivo.write('Nome Completo: {}\n'.format(n))
arquivo.write('Sexo: {}\n'.format(se))
arquivo.write('Idade: {}\n'.format(i))
arquivo.write('Status: {}\n'.format(s))
arquivo.write('Contato: {}\n'.format(c))
arquivo.write('Data de Nascimento: {}\n'.format(d))
arquivo.write('Local de Nascimento: {}\n'.format(l))
arquivo.write('E-mail: {}\n'.format(e))
arquivo.close()

input("Até mais ver!")
