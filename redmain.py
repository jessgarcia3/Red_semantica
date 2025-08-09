# Definimos la red semántica con un diccionario donde
# cada concepto apunta a una lista de tuplas (concepto_relacionado, tipo_relacion)
red_semantica = {
    "Inteligencia Artificial": [("Aprendizaje Automático", "incluye")],
    "Aprendizaje Automático": [
        ("Aprendizaje Supervisado", "se divide en"),
        ("Aprendizaje No Supervisado", "se divide en")
    ],
    "Aprendizaje Supervisado": [
        ("Clasificación", "usa técnica"),
        ("Regresión", "usa técnica")
    ],
    # Puedes agregar más conceptos y relaciones aquí
}

def mostrar_relaciones_texto(concepto, nivel=0):
    indent = "  " * nivel
    print(f"{indent}- {concepto}")
    if concepto in red_semantica:
        for (relacionado, tipo_relacion) in red_semantica[concepto]:
            print(f"{indent}  ({tipo_relacion})")
            mostrar_relaciones_texto(relacionado, nivel + 2)

def main():
    concepto = input("Ingrese un concepto clave: ").strip()
    if concepto not in red_semantica:
        print(f"Concepto '{concepto}' no encontrado o sin relaciones registradas.")
    else:
        mostrar_relaciones_texto(concepto)

if __name__ == "__main__":
    main()
