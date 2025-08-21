# a = input('Ingrese el valor de a: ')
# b = input('Ingrese el valor de b: ')

total = input('Ingrese el total de la cuenta: ')
propina = input('Ingrese la propina: ') #Aqui meto el dato de la propina
print('-----------------------------------------------')
total = float(total) # 
propinapercentual =  float(propina) 
totalconpropina = float(total) +  ( float(propina)) # 
print(f'Total de la cuenta ingresada: ${total:.2f}') #
print(f'Propina calculada: ${propinapercentual:.2f}') # Aqui muestro el dato de la propina
print(f'Total de la cuenta con propina: ${totalconpropina:.2f}')