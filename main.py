from funcao_conversao import *

def menu():

    resp = "S"
    while resp == "S":
        print("<========== Conversor de Temperatura ==========>")
        print("Converta de :")
        print("1-Celsius → Kelvin")
        print("2-Celsius → Fahrenheit")
        print("3-Fahrenheit → Celsius")
        print("4-Fahrenheit → Kelvin")
        print("5-Kelvin → Celsius")
        print("6-Kelvin → Fahrenheit")
        op = int(input("Insira sua opção:"))

        if op == 1:
            Celsius= float(input("Insira a temperatura em Celsius: "))
            print(f"{celcios_to_kelvin(Celsius)}°C")
        elif op == 2:
            Celsius = float(input("Insira a temperatura em Celsius: "))
            print(f"{celcios_to_fahrenheit(Celsius)}°C")
        elif op == 3:
            Fahrenheit = float(input("Insira a temperatura em Fahrenheit: "))
            print(f"{fahrenheit_to_celsius(Fahrenheit)}°F")
        elif op == 4:
            Fahrenheit = float(input("Insira a temperatura em Fahrenheit: "))
            print(f"{fahrenheit_to_kelvin(Fahrenheit)}°F")
        elif op == 5:
            Kelvin = float(input("Insira a temperatura em Kelvin: "))
            print(f"{Kelvin_to_celsius(Kelvin)}K")
        elif op == 6:
            Kelvin = float(input("Insira a temperatura em Kelvin: "))
            print(f"{Kelvin_to_fahrenheit(Kelvin)}K")
        else:
            print("Opção invalida")

        resp = input("Deseja continuar? [S/N]").upper()

if __name__ == "__main__":
    menu()