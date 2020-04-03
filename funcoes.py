# Exercicios de Funções
# Material de apoio : https://www.caelum.com.br/apostila-python-orientacao-objetos/funcoes/#o-que--uma-funo
# fontes: https://wiki.python.org.br/ExerciciosFuncoes


# 1.Crie uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def soma(numero1,numero2,numero3):
  soma = numero1+numero2+numero3
  return(soma)

print("Calcule a soma de 3 números")
resultado = soma(float(input("Digite o primeiro: ")),float(input("Digite o segundo: ")),float(input("Digite o terceiro: ")))

print(resultado)

# 2.Crie uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def define(numero):
    if numero > 0:
        verifica = ('Este número é Positivo')
    elif numero == 0:
        verifica = ('Nulo')
    else:
        verifica = ('Este número é Negativo')

    return verifica

print("Positivo OU Negativo?")
numero = int(input("digite um número: "))
define(numero)

# 3.Crie uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(custo, taxaImposto):

  total = (custo*(taxaImposto/100))+custo
  return total

print("Calcule valor total do produto com imposto: ")
custo = float(input("Digite o custo: "))
taxaImposto = float(input("Digite a porcentagem de imposto: "))

print(somaImposto(custo,taxaImposto))


# 4.Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados

import random

def embaralha(palavra):
  palavra = list(palavra) #passa a palavra para uma lista
  palavra = palavra.upper() # passa string para maiusculo 
  random.shuffle(palavra) #coloca os caracteres separador e aleatorios
  palavra = ''.join(palavra) #junta os caracteres novamente
  return palavra #retorno da função

palavra = str(input("Digite uma palavra: "))

palavra = embaralha(palavra)
print(palavra)

# 5.Crie uma função que calcule a raiz quadrada de um numero dado pelo usuário

def raiz(numero):
  
  for i in range(numero):
    multiplicacao = i*i
    print(multiplicacao)

    if multiplicacao == numero:
      numeroRaiz = i
      return numeroRaiz
    else:
      i += 1

print("Calcule a raiz quadrada exata:")
numero = int(input("Digite um número: "))
resultado = raiz(numero)
print(resultado)

# 6.Crie uma função que verifique a idade e informe se a pessoa é menor ou maior de idade

def verificaIdade(numero):

  if numero >= 18:
    verifica = ("Maior de idade")
  else: 
    verifica = ("Menor de idade")
  
  return verifica

numero = int(input("Digite sua idade: "))
print(verificaIdade(numero))