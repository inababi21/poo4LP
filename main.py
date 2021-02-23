#2°ANO DE INFORMÁTICA MATUTINO
#Disciplina: Programação Orientada a Objeto
#Docente: Camila Carolina Salgueiro Serrão
#Discentes: Inaê Bárbara Oliveira Campos; Milleni Santos Durão; Pedro Lucas De Queiroz Gomes


import getpass

# passo 1:  a classe Pessoa desempenha os papéis de entidade existente na vida real e que agora irá executar ações(métodos) e possui certas características(atributos) para diferenciar cada espécime do restante dos outros da mesma classe. 
class Pessoa:
    def __init__(self,nome,cpf, email,senha, endereco,tel):
        self.nome = nome
        self.cpf = cpf
        self.listEmail=[] #lista
        self.email = email
        self.listEmail.append(email)
        self.listSenha=[] #lista
        self.senha=senha
        self.listSenha.append(senha)
        self.endereco = endereco
        self.telefone= tel

     #métodos: são as ações da classe 
        

    def fazerLogin (self):
        while True:
            print('\n===================================')
            print('   ---FAÇA LOGIN---  ')
            loginemail= input('-email-')
            loginsenha = getpass.getpass('-senha-')
            #email errado e senha errada
            if loginemail not in self.listEmail and loginsenha not in self.listSenha:
                print('\nlogin incorreto')
                print('\ntente novamente')
                continue

            #email errado e senha correta
            if loginemail not in self.listEmail and loginsenha not in self.listSenha:
                print('\nlogin incorreto')
                print('\ntente novamente')
                continue
                
            #email correto e senha errada
            if loginemail not in self.listEmail and loginsenha in self.listSenha:
                print('\nlogin incorreto')
                print('\ntente novamente')
                continue
                
            #email correto e senha correta
            if loginemail in self.listEmail and loginsenha in self.listSenha:
                print(f'\n------SEJA BEM VINDO A TEMAKERIA IF, {self.nome}------')
                break

            
#fimdaclasse

#subclasse : a subclasse Cliente deriva da super classe Pessoa, dentro do sistema é necessário que ocorra de foerma diferenciada entre as subclasses Cliente e Funcionario 
class Cliente (Pessoa):
    def __init__(self,nome, cpf, email, senha, endereco,tel):
        
        super().__init__(nome,cpf,email,senha,endereco,tel)#os atributos herdados da superclasse Pessoa 
    def fazerCadastro (self):
        while True:
            print('\n===================================')
            print('\n  REGISTRE-SE')
            nome= input('Nome:')
            self.nome=nome
            email=input('Email:')
            self.email=email
            senha= getpass.getpass('Digite sua senha:')
            self.senha=senha
            senha2= getpass.getpass('Confirme sua senha:')
            cpf = input('CPF: ')
            self.cpf = cpf
            tel = input('Telefone: ')
            self.tel = tel
            endereco=input('Endereço: ')
            self.endereco= endereco
            if senha == senha2:
                self.listEmail.append(email)
                self.listSenha.append(senha)
                print('\n===================================')
                print(f'\n CADASTRO REALIZADO COM SUCESSO, {self.nome}!|')
                break
# caso a senha ou a senha não constar nas listas dentro do programa, esses avisos serão postos ao um usário que tentou realizar esse login mal sucedido   
            else:
                print('\n Sua senha não confere!')
                print('\n Faça seu cadastro novamente!')
                

#método exclusivo da classe Cliente, uma vez que após executar esta ação, o cliente poderá fazerLogin que é um método herdado da superclasse Pessoa. 
    
#método exclusivo da classe Cliente
    def editarDados (self):
        while True:
            print("Escolha o dado que deseja alterar:")
            dados=input('''\n - - - - - - - - - - - -  
- 1 - email             -
- 2 - senha             -
- 3 - endereço          -
- 4 - telefone          -
- - - - - - - - - - - - |''' )
            if dados not in ['1','2','3','4']:
                print('OPERAÇÃO INVÁLIDA!\n')
                continue
            if dados == '1':
                self.listEmail.remove(self.email)
                novoEmail= input('Digite seu novo email: ')
                clie1.email=novoEmail #alteraremail
                self.listEmail.append(novoEmail)
                print('ALTERAÇÃO REALIZADA COM SUCESSO!')
                break

            if dados == '2':
                senhaAntiga= getpass.getpass('Digite sua antiga senha:')#alterarsenha
                if senhaAntiga not in self.listSenha:
                    print('\n SENHA INVÁLIDA')
                    continue
                else:
                    print('\n SENHA VÁLIDA')
                    self.listSenha.remove(self.senha)
                    novaSenha= getpass.getpass ('Digite sua nova senha: ')
                    confSenha= getpass.getpass('Confime sua senha:')
                    if novaSenha == confSenha:
                        clie1.senha = novaSenha
                        self.listSenha.append(novaSenha)
                        print("ALTERAÇÃO REALIZADA COM SUCESSO! ")
                        break
                    else:
                        print("SENHA INVÁLIDA")
                        continue

            if dados == '3':
                novoEnder = input('Digite o novo endereço: ')#alterarendereço
                clie1.endereco = novoEnder
                print('ALTERAÇÃO REALIZADA COM SUCESSO!')
                break

            if dados == '4':#alterartelefone
                novoTel = input('Digite o novo telefone: ')
                clie1.tel = novoTel
                print('ALTERAÇÃO REALIZADA COM SUCESSO!')
                break
    
    

# a classe funcionario pode tanto ser uma super classe de Operador de Caixa e Entregador quanto subclasse de Pessoa 
class Funcionario (Pessoa):
    def __init__(self, nome, cpf, email, senha, endereco, tel,cargo):
        self.cargo= cargo #atributo diferente
        super().__init__(nome,cpf, email, senha, endereco,tel) # indica os atributos herdados pela super classe Pessoa

# A subclasse Entregador é uma classe que possui um atributo exclusivo, o id_veiculo, meio pelo qual o entregador posso ser idetificado dentro do programa de forma única 
class Entregador (Funcionario):
    def __init__(self, nome, cpf, email, senha,endereco,tel, cargo, id_veiculo,pedidoAserEntregue):
        self.id_veiculo= id_veiculo # atributo único 
       

        super().__init__(nome,cpf,email,senha,endereco,tel,cargo) #indica os atributos herdados pela super classe Funcionario 
        
# a subclasse OperadordeCaixa é a classe reponsável por calcular um valor final do caixa e ser armazenado no sistema.
class OperadordeCaixa (Funcionario):
    def __init__(self,nome, cpf, email, endereco, cargo, tel,ValorDiarioCaixa):
        self.ValorDiarioCaixa= ValorDiarioCaixa #atributo diferenciado 
        super().__init__(nome,cpf,email,endereco,tel,cargo) #indica os atributos herdados pela super classe Funcionario 
 #a classe Pagamento foi criada pensado na  necessidade do sistema em possui em organizar  as informações do pagamento. Armazenando-as 
class Pagamento: 
  def __init__(self, Cliente):
    self.modoPagamento= ""
#a função realizarPagamento é onde o Cliente possui um menun para a escolha do mode de pagamento que mais se adque a necessidado de quem irá pagar pelo Pedido
  def realizarPagamento(self, Pedido):
    
    while True:
      
      print("\n Qual é seu método de pagamento?\n")
      self.modoPagamento=input(" 1 - Dinheiro 💸 \n 2 - Cartão de Crédito 💳 \n 3 - Cartão de Débito 💳: ")
      if self.modoPagamento not in ['1','2','3']:
                print('OPERAÇÃO INVÁLIDA!\n')
                continue
      
      if self.modoPagamento == '1':
        print("\n-> MODO DE PAGAMENTO ESCOLHIDO: DINHEIRO \n")
        print(f""">>> SEU PEDIDO FOI REALIZADO!, {clie1.nome}<<<\n""") 
        print('___________________________________\n')
        break
      if self.modoPagamento == '2':
        print ("\n ->MODO DE PAGAMENTO ESCOLHIDO : CARTÃO DE CRÉDITO\n")
        print(f"""...PAGAMENTO REALIZADO COM SUCESSO!  AGUARDE SEU PEDIDO, {clie1.nome}!...\n""")
        print('___________________________________\n')
        break
      if self.modoPagamento == '3':
        print("\n->MODO DE PAGAMENTO ESCOLHIDO:  CARTÃO DE DÉBITO\n ")
        print(f"""...PAGAMENTO REALIZADO COM SUCESSO!  AGUARDE SEU PEDIDO, {clie1.nome}!...\n""")
        print('___________________________________\n')
        break   
     
    
 #Uma nova classe foi criada, sendo a mesma referente aos produtos disponibilizados pela temakeria.
 #A Superclasse Produtos É UMA GENERALIZAÇÃO da subclasse Pratos e da subclasse Bebidas:     
class Produtos:
    def __init__(self, nomeProduto, descricaoPro,tipoProduto, valorProduto, quantidade):
      #atributos
        self.nomeProduto= nomeProduto
        self.descricaoPro =descricaoPro
        self.tipoProduto=tipoProduto
        self.valorProduto= valorProduto
        self.quantidade= quantidade
        
#método para saber a quatidade de produtos que o cliente deseja:
    def quantProdutos(self):
        self.quantidade= int(input("Quantas unidades você quer?"))
#classe Pedido guarda os comportamentos dos objetos Pedidos realizados por clientes
class Pedido:
  def __init__(self,cliente):
    self.carrinho=[]#lista de produtos
    self.cliente=cliente
    self.entregador=entregador1
  def carrin (self,Produtos):#método para guardar os produtos pedidos pelo  cliente
  #peq = (Produtos.valorProduto * Produtos.quantidade)
    for x in range (Produtos.quantidade):
      self.carrinho.append(Produtos.valorProduto)
  def valorTotal(self): #1º produto   
       total=0        
       tamanhodalista= len(self.carrinho)
       for x in range (tamanhodalista):
         total=self.carrinho[x]+total
       print(total)



                        #instaciando objetos
temaki= Produtos ('Temaki de salmão 🍣', 'SALMÃO, CEBOLINHA E MAIONESE OU CREAM CHEESE', 'Temaki simles', 15.00, 1)
barca= Produtos('Barca completa 🍱', '6 SASHIMI, 2 NIGURI, 2 JOW, 10 HOT ROLL, 2 URAMAKI, 2 HARUMAKI DE QUEIJO, 2 HOSSOMAKI, 2 GUIOZA, 2 TEMAKI P, 1 YAKISSOBA VEGGIE P, 1 SHIMEJI P','combo', 74.00, 1)
yakisoba= Produtos ('Yaki Tradicional 🍜','YAKISOBA DE CARNE, COUVE FLOR, BRÓCOLIS,REPOLHO, ALHO PORÓ, CENOURA, MACARRÃO ESPECIAL E MOLHO YAKI SECRET','prato quente', 24.00,1)

refrigerante=Produtos('Refrigerante🥤',"OPÇÕES:Coca-cola Sprite, Guaraná e Fanta uva", '(lata 350ml)', 4.50, int())
suco= Produtos('Del valle 🧃','OPÇÕES: UVA, LARANJA,PÊSSEGO E MARACUJÁ','(lata 350ml)', 3.00,int())
cha= Produtos('Chá Gelado 🧉 ','OPÇÃO:ICE TEA LIMÃO','(lata 350ml)',5.00, 0)

#método para mostrar os produtos da temakeria

def cardapio (objPedido):
  while True: #cardapio
    menu=input("\n '1' - PRATOS \n '2' - BEBIDAS \n '3' - FINALIZAR |") 
    if menu not in ['1','2','3']:
      print("OPERAÇÃO INVÁLIDA!")
      continue
    if menu == '1':#opçoes de pratos
      print(f"""\n-------------------------------------------------------------------
|'1' - {temaki.nomeProduto}  - {temaki.descricaoPro} - R${temaki.valorProduto} -und.|__________________________________________________________________________
|'2' - {barca.nomeProduto}    - {barca.descricaoPro}  -  R${barca.valorProduto} -und.| __________________________________________________________________________
|'3' - {yakisoba.nomeProduto}   - {yakisoba.descricaoPro} -  R${yakisoba.valorProduto}  -und.| __________________________________________________________________________
--------------------------------------------------------------------------- """)
# o codPrato é uma variável que serve como identificador do prato do clienteb 
      codPrato= input("Digite o código referente ao produto que deseja: ")
      if codPrato not in ['1','2','3']:
        print('ALGO DEU ERRADO') # caso ocorra a aplicação de outra tecla nesse menu, o sistema avsa que aconteceu um erro 
      
# caso o Cliente escolha o codPrato 1, ele estará escohendo a opção de temaki como prato 
      if codPrato == '1':
        temaki.quantProdutos()
        objPedido.carrin(temaki)
        objPedido.valorTotal()
        #se acabar aqui
        #retorna o pedido modificado
        
# caso o Cliente escolha a opção codPrato 2, ele estará escolhendo a opção de barca de sushi como prato
      if codPrato == '2':
        barca.quantProdutos()
        objPedido.carrin(barca)
        objPedido.valorTotal()
# caso o Cliente escolha a opção codPrato 3, ele estará escolhendo a opção de yakisoba como prato
        

      if codPrato == '3':
        yakisoba.quantProdutos()
        objPedido.carrin(yakisoba)
        objPedido.valorTotal()
      continue
      return objPedido


    if menu == '2':#opçoes de bebidas
      print(f"""\n-----------------------------------------------------------------
      |'1' - {refrigerante.nomeProduto} -{refrigerante.descricaoPro}    R${refrigerante.valorProduto} und.
      |'2' - {suco.nomeProduto}    - {suco.descricaoPro}          R${suco.valorProduto} und.
      |'3' - {cha.nomeProduto}   - {cha.descricaoPro}          R${cha.valorProduto}  und.
 ---------------------------------------------    """)
      codBebida= input('Digite o código da bebida que deseja:')
# caso o Cliente escolha o codBebida 1, ele estará escohendo a opção de refrigerante como  opção bebida  
      if codBebida == '1':
        refrigerante.quantProdutos()
        objPedido.carrin(refrigerante)
        objPedido.valorTotal()
# caso o Cliente escolha o codBebida 2, ele estará escohendo a opção de suco como  opção bebida 
      if codBebida == '2':
        suco.quantProdutos()
        objPedido.carrin(suco)
        objPedido.valorTotal()
# caso o Cliente escolha o codBebida 3, ele estará escohendo a opção de chá como opção de bebida

      if codBebida == '3':
        cha.quantProdutos()
        objPedido.carrin(cha)
        objPedido.valorTotal()
      continue
      return objPedido
     
        
# o if serve para somar todos itens escolhidos em um pedido 
    if menu == '3':
      print('\n TOTAL DO PEDIDO É:')
      objPedido.valorTotal()
      break


#instaciando objetos do tipo pessoa
clie1= Cliente ('', '','','','','')
entregador1= Entregador("Nelson","060","nelson@gmail.com","1234","Av.Jatu",6999557782,"entregador","1090","pedido1")
pedido1=Pedido(clie1)
pedido1=Pedido(entregador1)
pedido1.carrinho
pag1=Pagamento(clie1)

#FUNCIONARIO PREDEFINIDO
funcio1= Funcionario ('Pedro', '09283728909','funcipe@gmail.com', '12345', 'AV.Calama', 99300000,'Operador')
codfuncio1= '1090'

#NOME DO RESTAURANTE
print(" ________________________________________\n")
print (" *********  🍣  TEMAKERIA IF 🍣  ********** ")
print(" ________________________________________")

while True:
  print()#MENU INICIAL
  print(' ==================================\n')
  print('   ->Escolha uma das opções:<- \n')
  menu1 = input("  '1' - FAZER LOGIN\n  '2' - CADASTRA-SE  : ")

  if menu1 not in ['1','2']:
    print('ALGO DEU ERRADO!\nTENTE NOVAMENTE\n')
    continue

  if menu1 == '2':#OPÇÃO 2 PARA EXECUTAR O MÉTODO fazerCadastro
    clie1.fazerCadastro()
    continue
    
  if menu1 == '1': #QUEM ESTÁ LOGANDO
    while True:
      print(' ==================================\n')
      menu2 = input("\n     ---  ESCOLHA COMO VOCÊ DESEJA LOGAR:---\n'c' - CLIENTE \n'f' - FUNCINÁRIO -")
      if menu2 not in ['c', 'f']:
        print('OPÇÃO INVÁLIDA!')
        continue

      if menu2 == 'c': #Executando o método fazerLogin 'c' se caso for um cliente
        clie1.fazerLogin() 
        while True: 
          menu3 = input("""1'- Alterar dados\n'2'- Fazer pedido\n '3'- Sair """)
          if menu3 == '1':
            clie1.editarDados()
            continue
          if menu3 == '3':
            clie1.fazerLogin()
            continue
            
          if menu3 =='2':
              
            pedido1=cardapio(pedido1)
           
           
            #pedido1 = pedido1 depois de passsar pelo cardápio ou seja
            #pedido1 = pedido1 Atualizado 
            
            while True:
              
              final = input('\n ->DIGITE 1 PARA FINALIZAR:  \n') #finalizar pedido
              if final not in ['1']:
                print('operação inválida')
                continue
              else:
                pag1.realizarPagamento(pedido1)
                print('=============================\n')
                print(f"""|SEU PEDIDO ESTÁ A CAMINHO...🏍️!|\n""")
                print(f""">>>ENTREGADOR DO SEU PEDIDO,{clie1.nome}:<<<\n  Nome:{entregador1.nome}\n  Telefone: {entregador1.telefone}\n  id_veiculo: {entregador1.id_veiculo}\n  """)
                print('=============================\n')
                print('*********************************')
                print(f"""Bem vindo de volta ao menu inicial, {clie1.nome}\n""")
                
                
              
              break          

      if menu2 == 'f':#Executando o método fazerLogin 'f' se caso for um funcionario
        cod = input('\n digite o código de funcionário: ')
      if cod == codfuncio1:
       funcio1.fazerLogin()
      break


      
    break

  break 