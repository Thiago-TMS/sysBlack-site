def menu():
    print("Menu")
    print("1 - Tabuada")
    print("2 - Soma números")
    print("3 - Multiplicação")
    print("9 - Sair")
   
def tabuada(n):
   for i in range(1,11):
     res = n * i
     print(f"{n} x {i} = {res}")

def somaNumeros(n1,n2):
   res = n1 + n2
   return res

def multiplicaNumeros(n1,n2):
   res = n1 * n2
   return res

opcao = 0
while opcao != 9:
    menu()
    opcao = int(input("Digite a opção: "))
    if (opcao == 1):
      n = int(input("Digite um número: "))
      tabuada(n)            
    elif (opcao == 2):
      n1 = int(input("Digite 1 número: "))
      n2 = int(input("Digite 2 número: "))
      print("Soma = ",somaNumeros(n1,n2)) 
    elif (opcao == 3):
      n1 = int(input("Digite 1 número: "))
      n2 = int(input("Digite 2 número: "))
      print("Multiplicação = ",multiplicaNumeros(n1,n2)) 
    elif (opcao!=9):
         print("ERRO: digite 1,2,3 ou 9")
