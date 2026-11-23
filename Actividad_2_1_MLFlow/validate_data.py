from sklearn.datasets import load_iris


def validate_dataset():

    print("\n===== VALIDACIÓN DE DATOS =====\n")

    iris = load_iris()

    X = iris.data

   

    feature_names = iris.feature_names

    # Validar nulos
    for fila in X:
        for valor in fila:
            if valor is None:
                raise ValueError(
                    "Se encontraron valores nulos."
                )

    print("- Sin valores nulos")

    # Validar tipos
    for fila in X:
        for valor in fila:
            if not isinstance(valor, (int, float)):
                raise TypeError(
                    f"Tipo inválido detectado: {type(valor)}"
                )

    print("- Tipos de datos correctos")

    # Validar rangos lógicos

    for fila in X:

        sepal_length = fila[0]
        sepal_width = fila[1]
        petal_length = fila[2]
        petal_width = fila[3]

        if not (0 <= sepal_length <= 10):
            raise ValueError(
                "Valor fuera de rango en sepal_length"
            )

        if not (0 <= sepal_width <= 10):
            raise ValueError(
                "Valor fuera de rango en sepal_width"
            )

        if not (0 <= petal_length <= 10):
            raise ValueError(
                "Valor fuera de rango en petal_length"
            )

        if not (0 <= petal_width <= 10):
            raise ValueError(
                "Valor fuera de rango en petal_width"
            )

    print("- Rangos válidos")
    print("\nVALIDACIÓN EXITOSA")


if __name__ == "__main__":
    validate_dataset()