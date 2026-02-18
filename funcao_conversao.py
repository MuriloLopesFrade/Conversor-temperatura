def celcios_to_kelvin(Celcios):
    k = Celcios + 273.15
    return k

def celcios_to_fahrenheit(Celcios):
    F=(Celcios*9/5)+32
    return F

def fahrenheit_to_celsius(Fahrenheit):
    C=(Fahrenheit-32)*5/9
    return C

def fahrenheit_to_kelvin(Fahrenheit):
    K=((Fahrenheit-32)*5/9) +273.15
    return K

def Kelvin_to_celsius(Kelvin):
    C=Kelvin-273.15
    return C

def Kelvin_to_fahrenheit(Kelvin):
    F=((Kelvin-273.15)*9/5)+32
    return F