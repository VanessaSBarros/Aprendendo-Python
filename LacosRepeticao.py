
#Exercícios
#Estrutura e Laços de repetição
#Fonte: https://wiki.python.org.br/EstruturaSequencial e https://wiki.python.org.br/EstruturaDeDecisao


# 1.Faça um Programa que mostre a mensagem "Alo mundo" na tela:
print("Alô Mundo")

# 2.Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número]:
numero = int(input("Digite um número:"))
print("O número informado foi: ",numero)

# 3.Faça um Programa que peça dois números e imprima a soma.
numero1 = int(input("Número 1:"))
numero2 = int(input("Número 2:"))

print("O resultado é: ",numero1+numero2)

# 4.Faça um Programa que peça as 4 notas bimestrais e mostre a média. O programa deve calcular a média alcançada por aluno e apresentar: A mensagem "Aprovado", se a média alcançada for maior ou igual a sete; A mensagem "Reprovado", se a média for menor do que sete; A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = float(input("Nota 1:") or "0")
nota2 = float(input("Nota 2:") or "0")
nota3 = float(input("Nota 3:") or "0")
nota4 = float(input("Nota 4:") or "0")

media = ((nota1+nota2+nota3+nota4)/4)

print("A média das notas é: ",media)

if media == 10:
  print("Aprovado com Distinção")
elif media >= 7:
  print("Aprovado")
elif media < 7:
  print("Reprovado")

# 5.Faça um Programa que converta metros para centímetros:

metro = float(input("Digite os metros:"))
centimetro = metro*100

print(metro, "metros equivalem a ", centimetro, "centímetros")

# 6.Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. Fórmula: C = (5 * (F-32) / 9):

grausF = float(input("Digite os graus em Farenheit:") or "0")
grausC = float(5*(grausF-32)/9)

print(grausF, "graus Farenheit equivalem a",grausC,"graus celsius",)

# 7.João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas:

peso = float(input("Digite o peso: ") or "0")
excesso = float(peso-50)
multa = float(excesso*4)

if peso <= 50:
  print("Não há excedente de peso")
else:
  print("O excedente foi de",excesso," kg, e a multa será de ",multa)

# 8.Faça um Programa que peça dois números e imprima o maior deles.

numero1 = float(input("Digite o primeiro número: ") or "0")
numero2 = float(input("Digite o segundo número: ") or "0")

maximo = max(numero1, numero2)
print(maximo)

# 9.Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo:

numero = float(input("Digite um número: ")  or "0")

if numero >= 0:
  print("O número ",numero,"é positivo")
else:
  print("O número ",numero,"é negativo")

# print("Negativo" if numero < 0 else "Positivo") Alternativa 2 para o print


# 10.Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido:

letra = input("Digite F para Feminino ou M para Masculino: ")

if letra == "F":
  print("F - Feminino")
elif letra == "M":
  print("M - Masculino")
else:
  print("Sexo Inválido")

# 11.Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input("Qual é o seu turno M-Matutino, V-Vespertino ou N-Noturno? ")

if turno == "M-Matutino" or turno == "M-matutino" or turno == "M" or turno == "Matutino":
  print("Bom dia!")
elif letra == "V-Vespertino" or turno == "V-vespertino" or turno == "V" or turno == "Vespertino" :
  print("Boa tarde")
elif letra == "N-Noturno" or turno == "N-noturno" or turno == "N" or turno == "Noturno":
  print("Boa Noite")
else:
  print("Valor Inválido")

# 12.Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

numero = int(input("Digite o número correspontente ao dia da semana: "))

x = ["Domingo", "Segunda-Feira","Terça-Feira","Quarta-Feira","Quinta-Feira","Sexta-Feira","Sábado"]

if numero > 0 and numero < 7:
  print(x[numero])
else: 
  print("Valor Inválido")

# 13.Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = float(input("Digite uma nota entre 0 e 10: "))

while (nota < 0 or nota > 10):
  nota = float(input("Por favor, digite uma nota válida: "))
else: 
  print(nota)

# 14.Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nome = input("Digite o seu nome: ")
senha = input("Digite o sua senha: ")

while (nome == senha):
  print("Erro: A senha não pode ser igual ao seu nome")
  nome = input("Digite o seu nome: ")
  senha = input("Digite o sua senha: ")
else:
  print("ok!")

# 15.Faça um programa que leia e valide as seguintes informações:

#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

# nome
nome = input("Digite o seu nome: ")
while len(nome) <= 3:
  print("Seu nome precis ser maior que 3 caracteres")
  nome = input("Digite o seu nome: ")

#idade
idade = int(input("Idade: "))
while idade <0 or idade >150:
  print("Idade inválida")
  idade = input("Idade: ")

#salario
salario = float(input("Salario: "))
while salario <0:
  print("Salário inválido")
  salario = input("Salario: ")

#estado civil
estado_civil = ["s", "c", "v", "d", "S", "C", "V","D"]
ec = input("Estado Civil S-Solteiro, C-Casado, V-Viúvo ou D-Divorciado: ")
while ec not in estado_civil:
  print("Estado civil válido")
  ec = input("Estado Civil s,c,v ou d: ")

#sexo
lista = ["F","M", "f","m"]
opcao = input("Sexo (M ou F): ")

while opcao not in lista:
  sexo = input("Sexo inválido, digite novamente: ")
else:
  print("ok")

# 16.Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

numero = int(input("Digite um número: ")) # Entrada do número escolhido
seq = range(numero) # Lista com a sequencia entre 0 e o numero escolhido
excluido = [0,1,numero] # Números que a divisao com resto é = 0 (primo)
cont = 0 # Contador para identidicar quantas divisoes dão mais que zero

for i in seq: # Faz um loop percorrendo todos os numeros da sequencia
  if seq[i] not in excluido: # Apenas considera tudo que é diferente de 0, 1 ou o proprio número
    resto = numero % seq[i] # Divide o numero pelo número da sequencia naquele momento
    if resto == 0: # Se houver resto na divisão ele soma +1 no contador
      cont += 1

if cont != 0: # Se o contador for diferente de 0:
  print("O número",numero,"não é primo")
else: # Se o contador for igual a 0:
  print("O número",numero,"é primo")




