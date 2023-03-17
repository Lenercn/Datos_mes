##dividir cadena
cadena="Descubre los cursos que tenemos para ti."
print("***************************\nLa frase se divide en: "+str( cadena.split()))

##busqueda
print("***************************")
print( "los" in cadena)

## poscion
print("***************************\nla palabra ocupa la pos: "+ str(cadena.find("ti"))
)

## conteo 
print("la palabra se repite: "+ str(cadena.count("los")) + " veces")

##ninusculas
cadena1="+50 EMPRESAS CONFÍAN EN NOSOTROS\n Miles de estudiantes han mejorado sus habilidades técnicas con DSRP. ¡Sé el siguiente!"
print("***************************\n minusculas\n"+ str (cadena1.lower()))
print("***************************\n MAYUSCULAS\n"+ str (cadena1.upper()))