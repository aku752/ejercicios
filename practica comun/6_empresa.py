kilovatio = int(input("Ingrese cantidad kilovatio: "))
costo = kilovatio*0.015
print("Costo kilovatio: ", costo)
adicional = (costo/100)*10
print("Adicional 10% : {0:.2f}".format(adicional))
total = costo + adicional
print("Total a pagar: ", total)
