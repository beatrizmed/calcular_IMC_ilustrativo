# Cálculo de IMC - Índice de massa corporal 

'''
Qual é a ALTURA em cm?
Qual é o seu PESO em kg?
'''

# NENOR que 18,5 = MAGREZA
# ENTRE 18,5 e 24,9 = NORMAL
# ENTRE 25,0 e 29,9 = SOBREPESO
# ENTRE 30,0 e 39,9 = OBESIDADE
# MAIOR que 40,0 = OBESIDADE GRAVE

altura = float(input('Informe a sua altura em cm: '))
peso = float(input('Informe o seu peso em kg: '))

IMC = peso/(altura/100)**2
print(IMC)

if IMC < 18.5:
  print('VOCÊ ESTÁ ABAIXO DO PESO!')

elif IMC >= 18.5 and IMC < 25: 
  print('SEU PESO ESTÁ NORMAL!')

elif IMC >= 25 and IMC < 30:
  print('PROCURE FAZER MAIS EXERCICIOS E PROCURE MANTER UMA ALIMENTAÇÃO SAUDAVEL, POIS VOCÊ ESTAR SOBREPESO')

elif IMC >= 30 and IMC <= 39.9:
  print('VOCÊS ESTAR OBESO, POR TANTO VÁ TREINAR E FAZER UMA DIETA!')

else:
  print('OBESIDADE GRAVE, TU VAI MORRER!')
