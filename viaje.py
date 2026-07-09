from math import radians, sin, cos, sqrt, atan2

# Diccionario de ciudades (lat, lon) — puedes ampliarlo
ciudades = {
    "santiago":       (-33.4489, -70.6693),
    "valparaiso":     (-33.0472, -71.6127),
    "concepcion":     (-36.8201, -73.0444),
    "buenos aires":   (-34.6037, -58.3816),
    "mendoza":        (-32.8895, -68.8458),
    "cordoba":        (-31.4201, -64.1888),
}

TRANSPORTES = {
    "avion":  900,   # km/h promedio
    "auto":   90,
    "bus":    80,
}

def distancia_km(origen, destino):
    lat1, lon1 = ciudades[origen]
    lat2, lon2 = ciudades[destino]
    R = 6371  # radio de la Tierra en km
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

def main():
    while True:
        origen = input("Ciudad de Origen: ").strip().lower()
        destino = input("Ciudad de Destino: ").strip().lower()

        if origen not in ciudades or destino not in ciudades:
            print("Ciudad no reconocida. Ciudades disponibles:", ", ".join(ciudades))
            continue

        km = distancia_km(origen, destino)
        millas = km * 0.621371

        print("\nMedios de transporte disponibles:", ", ".join(TRANSPORTES))
        transporte = input("Elige el medio de transporte: ").strip().lower()
        if transporte not in TRANSPORTES:
            print("Transporte no válido, se usará 'auto' por defecto.")
            transporte = "auto"

        horas = km / TRANSPORTES[transporte]

        print(f"\nDistancia: {km:.2f} km ({millas:.2f} millas)")
        print(f"Duración estimada en {transporte}: {horas:.2f} horas")
        print(f"Narrativa: El viaje comienza en {origen.title()} y culmina en {destino.title()}, "
              f"recorriendo {km:.0f} km ({millas:.0f} millas) a bordo de {transporte}, "
              f"un trayecto de aproximadamente {horas:.1f} horas cruzando la cordillera "
              f"entre Chile y Argentina.\n")

        salir = input("Escribe 's' para salir o Enter para continuar: ").strip().lower()
        if salir == "s":
            print("Fin del programa.")
            break

if __name__ == "__main__":
    main()
