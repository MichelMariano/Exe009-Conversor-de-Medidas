#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e
# milimetros

metro = float(input('Digite quantos Metros: '))
cm = metro * 100
mm = metro * 1000 #Cada metro tem 1000 milimetros

print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm '.format(metro, cm, mm))
