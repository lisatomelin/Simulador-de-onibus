#UNISENAI – SANTA CATARINA
# CURSO SUPERIOR DE TECNOLOGIA EM ANÁLISE E DESENVOLVIMENTO DE SISTEMAS
# UC: ALGORITMOS E PROGRAMAÇÃO
# ACADÊMICAS: LISIANA REINHOLD TOMELIN, LÍVIA BARCELOS DE OLIVEIRA
import random

atualPassageiros = 0
atualparadasdeonibus = 0
capacidademaxima = 40
totaldePassageiros = 0

for atualparadasdeonibus in range(1,21):
  print()
  print("Paradas de Ônibus: ", atualparadasdeonibus)
  
   # embarcar passageiro
  if atualparadasdeonibus != 20:
    entrada = random.randint(0,10)
    print("Quantidade de passageiros que entraram: ", entrada)
    totaldePassageiros = totaldePassageiros + entrada
    if capacidademaxima == atualPassageiros:
       atualPassageiros = capacidademaxima - entrada
    else:
      atualPassageiros = atualPassageiros + entrada
   
    # desembarcar passageiros 
  if atualparadasdeonibus != 1:
      saida = random.randint(0,10)
      saida = atualPassageiros - entrada
      print("Quantidade de passageiros que sairam: ", saida)
      atualPassageiros = atualPassageiros - saida
      print("Quantidade atual de passageiros: ", atualPassageiros)
    
        
  if atualparadasdeonibus == 20:
    saida == atualPassageiros
    print("Desembarque de todos os passageiros: ", atualPassageiros)
    print()
    print ("Total de passageiros transportados:", totaldePassageiros)
    print("Fim")
