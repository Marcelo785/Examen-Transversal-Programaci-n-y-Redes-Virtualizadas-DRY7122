def validar_vlan(vlan):
    if 1 <= vlan <= 1005:
        return "Rango normal (1-1005)"
    elif 1006 <= vlan <= 4094:
        return "Rango extendido (1006-4094)"
    else:
        return "VLAN inválida (fuera de rango 1-4094)"

def main():
    try:
        vlan = int(input("Ingrese el número de VLAN: "))
    except ValueError:
        print("Debe ingresar un número entero.")
        return
    print(f"La VLAN {vlan} corresponde a: {validar_vlan(vlan)}")

if __name__ == "__main__":
    main()
