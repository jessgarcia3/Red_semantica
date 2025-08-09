red_semantica = {
    "Inteligencia Artificial": [
        ("Aprendizaje Automático", "incluye"),
        ("Razonamiento Automático", "incluye"),
        ("Procesamiento de Lenguaje Natural", "incluye"),
        ("Visión por Computadora", "incluye"),
        ("Robótica", "incluye")
    ],
    "Aprendizaje Automático": [
        ("Aprendizaje Supervisado", "se divide en"),
        ("Aprendizaje No Supervisado", "se divide en"),
        ("Aprendizaje por Refuerzo", "se divide en")
    ],
    "Aprendizaje Supervisado": [
        ("Clasificación", "usa técnica"),
        ("Regresión", "usa técnica"),
        ("Redes Neuronales", "usa algoritmo"),
        ("SVM", "usa algoritmo"),
        ("Árboles de Decisión", "usa algoritmo")
    ],
    "Aprendizaje No Supervisado": [
        ("Clustering", "usa técnica"),
        ("Reducción de Dimensionalidad", "usa técnica")
    ],
    "Clustering": [
        ("K-means", "usa algoritmo"),
        ("DBSCAN", "usa algoritmo")
    ],
    "Reducción de Dimensionalidad": [
        ("PCA", "usa algoritmo")
    ],
    "Aprendizaje por Refuerzo": [
        ("Agentes", "se basa en"),
        ("Entornos", "se basa en"),
        ("Recompensas", "se basa en"),
        ("Q-Learning", "usa algoritmo"),
        ("Deep Q-Networks", "usa algoritmo")
    ],
    "Procesamiento de Lenguaje Natural": [
        ("Análisis Sintáctico", "incluye"),
        ("Análisis Semántico", "incluye"),
        ("Generación de Lenguaje Natural", "incluye"),
        ("Modelos de Lenguaje", "usa técnica"),
        ("Embeddings", "usa técnica")
    ],
    "Embeddings": [
        ("Word2Vec", "ejemplo"),
        ("BERT", "ejemplo")
    ],
    "Razonamiento Automático": [
        ("Lógica Proposicional", "incluye"),
        ("Lógica de Primer Orden", "incluye"),
        ("Sistemas Expertos", "usa"),
        ("Inferencia", "usa")
    ]
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
