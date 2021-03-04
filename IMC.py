def imc(estatura,peso):
    return peso/estatura**2

peso=float(input('Ingrese su peso en kg por favor'))
estatura=float(input('Ingrese su estatura en m por favor'))
indice=imc(estatura,peso)
print('su indice de masa muscular es: '"{:.2f}".format(indice))