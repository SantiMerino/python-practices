funcion = lambda valor:valor ** 2
print(funcion(4))

# Sintaxis lambda [Parameter]: Function 
convers = lambda C: (C * 9/5) + 32
print(convers(0))

tempsC = [0, 10, 20, 30, 40]
tempsF = list(map(lambda datos: (datos * 9/5) + 32,  tempsC))
print(tempsF)

# filter
tempsC = [0,18,23,38,15, 6, 32, 44, 15, 21]
# Sublista 1 -> 15 < Temp < 22
tempsSub1 = list(filter(lambda datos: datos > 15 and datos < 22, tempsC))
# Sublista 2 -> Temp %! 2 and Temp > 15
tempsSub2 = list(filter(lambda datos: datos % 2 >0 and datos > 15, tempsC))

print(tempsSub1)
print(tempsSub2)