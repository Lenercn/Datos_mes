# texto ="3.14159265359"
# print("El valor de PI es %s " % texto )


Pais ="peru"
Region= "Cajamarca"
Altitud=  2.750 

template="""
Datos de altura de {Pais}
__________________________
Nombre de Region: {Region}
Ubicado a {Altitud} msnm"""
print (template.format(Pais=Pais, Region=Region, Altitud=Altitud).upper())



tecto= "hola mundo "
print(tecto.find("hola"))