"""
Mi principal error fue el no entender del todo bien 
el algoritmo y entender las especificaciones,
No me habia dado cuenta que el objetivo no es que al final
quede 1 solo digito, si no que ambos se puedan dividir de la 
misma manera n para poder aplicar la formula x=x1*10n + x2.
Por esa razon la condicion queda definida como si algunos 
de los dos tiene 1 solo digito y por esa razon se divide 
el numero solo si tiene los digitos suficientes
"""
def karatzuba(x, y):
    # Condiciones base para la recursión
    """
    Si algunos de los dos tiene un solo digito 
    no tiene caso serguir diviendo ya que el objetivo 
    es hacer una pasada en la operaciones. 
    El objetivo no es que al final quede un solo digito 
    en ambos numeros.
    """
    if len(x) == 1 or len(y) == 1:
        return str(int(x) * int(y))

    """
    Determina el maximo numero de digitos entre ambos numeros
    con el objetivo de obtener la mitad de ambos.
    Yo cometi un error, de acuerdo a los pdfs el objetivo no es 
    dividir a la mitad los numeros, mas bien es divirlos en la 
    misma cantidad de digitos, por esta razon es importante 
    determinar la mitad maxima ya que si uno no tiene suficientes
    digitos para dividirse no lo hace se queda como esta 
    """
    n = max(len(x), len(y))
    n2 = n // 2

    """
    Divide los numeros en partes, izquierda y derecha, de ser posible
    En ambos numeros si la izquierda no es posible dividirla por falta de digitos
    entonces se define como 0 y la parte derecha contendra todo el numero. 
    """

    # Divide los números en partes
    a = x[:-n2] if len(x) > n2 else '0'
    b = x[-n2:]
    c = y[:-n2] if len(y) > n2 else '0'
    d = y[-n2:]

    # Calcula las tres multiplicaciones recursivamente
    ac = karatzuba(a, c)
    bd = karatzuba(b, d)
    ad_bc = (
        int(karatzuba(str(int(a) + int(b)), str(int(c) + int(d)))) -
        int(ac) - int(bd)
    )

    # Combina los resultados
    resultado = str(int(ac) * 10**(2 * n2) + int(ad_bc) * 10**n2 + int(bd))

    return resultado

number_1 = "3"
number_2 = "5000"

result = karatzuba(number_1, number_2)

print(result)