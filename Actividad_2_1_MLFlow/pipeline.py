import subprocess
import sys
from validate_data import validate_dataset


def main():

    print("\n==============================")
    print("INICIO DEL PIPELINE")
    print("==============================")

    try:

        validate_dataset()

        print("\nIniciando entrenamiento...")

        

        subprocess.run(
           [sys.executable, "train.py"],
        check=True)

        print("\nPIPELINE FINALIZADO")

    except Exception as e:

        print("\nERROR EN EL PIPELINE")
        print(e)


if __name__ == "__main__":
    main()