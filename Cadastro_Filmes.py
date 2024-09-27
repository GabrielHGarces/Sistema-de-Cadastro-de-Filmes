from operator import itemgetter
import ast
import os

'''
Programa de cadastro de filmes

O objetivo do programa é permitir que o usuario insira  filmes e seus generos para busca e  manuseamento de dados.
O sistema usa um arquivo CSV para garantir a persistencia dos dados.


'''

#Permite cadastro dos filmes e os salva em um arquivo CSV
def Operação_de_cadastro():
  
  Manipular_CSV()
  nome_do_filme = input("Digite o nome do filme: ")
  genero_do_filme = input("DIgite o genero predominante do filme: ")
  

  id_do_filme = 0
  ordenar_obrigatória()
  

  
   
  for i in range(len(lista_dic)):
    
      if lista_dic[i]["id"] == id_do_filme or lista_dic[i]["id"]  < id_do_filme  :
        id_do_filme = id_do_filme+1 
  


  dicionario_a_cadastrar ={
    "nome":nome_do_filme,
    "genero":genero_do_filme,
    "id": id_do_filme
  }
  dicionario_convertido = str(dicionario_a_cadastrar)
  CSV_salvar = open("Lista_de_dicionarios.txt","a")
  CSV_salvar.write(dicionario_convertido +'\n')

  CSV_salvar.close()
  
  
  
  menu_de_operação()

#Mostra todos os itens cadastrados
def Operação_de_listagem():
  Manipular_CSV()

  for index in range(len(lista_dic)):
    
    print("Nome do Filme: "+lista_dic[index]["nome"])
    print("Gênero Predominante do Filme: "+lista_dic[index]["genero"])
    print("ID do Filme: "+str(lista_dic[index]["id"]))
    print()
  
  menu_de_operação()

#Permite fazer uma busca por cada categoria disponivel, seja  nome, genero ou iD
def Operação_de_busca():
  Manipular_CSV()
  escolha_usu = 200
  
  while escolha_usu < 0 or escolha_usu > 3:
    print()
    print("Para busca por nome digite 0 ")
    print("Para busca por genero predominante digite 1 ")
    print("Para busca por id digite 2 ")
    print("Para voltar ao menu anterior digite 3 ")
    print()

    try:

      escolha_usu = int(input("Insira o numero para escolher uma opção  "))
      print()
    except:
        print()
        print("ERRO")
        print("Digite somente um numero de 0 a 3")

    else:
      
      #Vai contar se algum valor for encontrado, para que o usuario tenha feedback do resultado da sua operação
      contador_valores = 0
      
      if escolha_usu == 0:
        print()
        
        a_buscar = input("Insira o nome do filme que você busca: ")

        for i in range(len(lista_dic)):
          if lista_dic[i]["nome"] == a_buscar :
            contador_valores = contador_valores + 1
            print(lista_dic[i])

        if contador_valores == 0:
            print("Resultado não encontrado")
        else:
            print("Resultado Encontrado")
         

        break
      if escolha_usu == 1:
        print()
        a_buscar = input("Insira o genero predominante que você busca busca: ")

        for i in range(len(lista_dic)):
          if lista_dic[i]["genero"] == a_buscar :
            contador_valores = contador_valores + 1
            print(lista_dic[i])

        if contador_valores == 0:
            print("Resultado não encontrado")
        else:
            print("Resultado Encontrado")
        

        break
      if escolha_usu == 2:
        print()
        try:
          a_buscar = int(input("Insira o id que você busca busca: "))
        except:
          print("ERRO")
          print("Digite Um numero inteiro")
          print()

        else:
          for i in range(len(lista_dic)):
            if lista_dic[i]["id"] == a_buscar :
              contador_valores = contador_valores + 1
              print(lista_dic[i])
          if contador_valores == 0:
            print("Resultado não encontrado")
          else:
            print("ID Encontrado")

          
        break  

    





  


  menu_de_operação()

# Permite remover um registro de filmes Via ID
def Operação_de_remoção():

  a_remover = None
  Manipular_CSV()
  try:

    a_remover = int(input("Insira o ID a ser deletado:  "))
    print()
  except:
    print()
    print("ERRO")
    print("Digite somente um numero inteiro")
  
  
  #Vai contar se algum valor for encontrado, para que o usuario tenha feedback do resultado da sua operação
  contador_valores = 0
  
  #Esse contador vai salvar o index do id que o usuario quer remover
  contador = None

  for i in range(len(lista_dic)):
    if lista_dic[i]["id"] == a_remover :
      contador = i
      contador_valores = contador_valores + 1
  if contador_valores == 0:
    print("Resultado não encontrado")
  else:
    print("ID Removido")  

  if contador is not None:
    lista_strings.pop(contador)
    
  os.remove("Lista_de_dicionarios.txt")
  CSV_salvar = open("Lista_de_dicionarios.txt","w")
  for linha in range(len(lista_strings)):
    CSV_salvar.write(lista_strings[linha])
    CSV_salvar.write('\n')
  CSV_salvar.close()
  menu_de_operação()

#Ordena o arquivo CSV em ordem crescente ou decrescente
def Operação_de_ordenação(): 
  a_ordenar = None
  Manipular_CSV()
  try:
    a_ordenar = int(input("Para Crescente digite 0, para Decrescente digite 1: "))
    lista_dic_sorted = []
  except:
    print()
    print("ERRO")
    print("Insira apenas o valor inteiro: 0 ou 1")

  else:
    
    #A função itemgetter salva os resultados das chaves "id" de cada index da lista de dicionarios. Permitindo assim a ordenação via ID
    
    #Lista ordenada Crescente
    if a_ordenar == 0:
      lista_dic_sorted = sorted(lista_dic, key=itemgetter('id'),reverse=False)
      print("Ordenação Crescente concluida")
    
    #Lista ordenada Decrescente
    if a_ordenar == 1:
      lista_dic_sorted = sorted(lista_dic, key=itemgetter('id'),reverse=True)
      print("Ordenação Decrescente concluida")

    #os.remove apaga o arquivo anterior, permitindo assim que eu possa criar um novo baseado na nova lista aqui feita
    os.remove("Lista_de_dicionarios.txt")
    
    CSV_salvar = open("Lista_de_dicionarios.txt","w")
    for linha in range(len(lista_dic_sorted)):
      CSV_salvar.write(str(lista_dic_sorted[linha]))
      CSV_salvar.write('\n')
    CSV_salvar.close()
  
    
  
  
  
  menu_de_operação()


# Essa função garante que ao cadastrar um filme novo, a lista vai ser ordenada de forma crescente como padrão
def ordenar_obrigatória():
  
  #A função itemgetter salva os resultados das chaves "id" de cada index da lista de dicionarios. Permitindo assim a ordenação via ID
  lista_dic_sorted = sorted(lista_dic, key=itemgetter('id'),reverse=False)
  
  os.remove("Lista_de_dicionarios.txt")
  CSV_salvar = open("Lista_de_dicionarios.txt","w")
  for linha in range(len(lista_dic_sorted)):
      CSV_salvar.write(str(lista_dic_sorted[linha]))
      CSV_salvar.write('\n')
  CSV_salvar.close()
  Manipular_CSV()



# Apresenta um menu de operação ao usuario, permitindo-o navegar pelas opções apresentadas.
def menu_de_operação():
  

  # 200 permite que entre no loop, este que o usuario não irá sair caso insira um valor invalido
  esc_usuario = 200
  while esc_usuario < 0 or esc_usuario > 4:
    print()
    print("Operação_de_cadastro digite 0")
    print("Operação_de_listagem digite 1")
    print("Operação_de_busca digite 2")
    print("Operação_de_remoção digite 3")
    print("Operação_de_ordenação digite 4")
    print("Finalizar digite 5")
    print()

    try:
    
      esc_usuario = int(input("Insira o numero para escolher uma opção :  "))
      print()
    except:
      print()
      print("ERRO")
      print("Digite somente um numero de 0 a 5")
  
    else:
      # Mensagem de erro caso o usuario digite algo errado.
      
      if esc_usuario ==  0:
        Operação_de_cadastro()
        break
      if esc_usuario == 1:
        Operação_de_listagem()
        break
      if esc_usuario == 2:
        Operação_de_busca()
        break
      if esc_usuario == 3:
        Operação_de_remoção()
        break
      if esc_usuario == 4:
        Operação_de_ordenação()
        break

      if esc_usuario == 5:
        print("Programa encerrado ")
        break




#Essa função garante a interação com o arquivo CSV, e salva o que estava escritoo em uma lista de Strings e uma lista de dicionários 

def Manipular_CSV():
  

  CSV_salvar = open("Lista_de_dicionarios.txt","a")
  CSV_salvar = open("Lista_de_dicionarios.txt","r")

  # Salva as linhas do arquivo CSV em uma lista de strings
  global lista_strings
  lista_strings = []
  
  #Quando uma linha do arquivo csv é transformado  para lista, ele vemm com uma quebra de linha escrita, .strip() retira essa  quebra 
  for linha in CSV_salvar:
    lista_strings.append(linha.strip())

  CSV_salvar.close()

  #Converte a lista de strings para uma lista de dicionários
  global lista_dic
  lista_dic = []
  
  #ast.literal_eval consegue identificar a sintaxe de um dicionario em formato  string e converter para dicionário novamente.
  for i in range(len(lista_strings)):
    lista_dic.append(ast.literal_eval(lista_strings[i]))
  

Manipular_CSV()
menu_de_operação()

