def ngramas(texto, n):
    """Divide the text into n-grams."""
    texto = texto.replace(" ", "")  # Eliminar espacios
    return [texto[i:i+n] for i in range(len(texto)-n+1)]

from collections import Counter
import pandas as pd
def frec_ngramas(texto, n):
    """Calculate the frequency of n-grams in the text."""
    ng=ngramas(texto, n)
    frec = Counter(ng)
    return pd.DataFrame(frec.most_common(), columns=['N-grams', 'Frecuency'])
import os
import pandas as pd

def leer_frecuencias(archivo):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    ruta = os.path.join(base_dir, archivo)
    return pd.read_csv(ruta, sep='\t', names=['N-grams', 'Frequency'])

if __name__ == "__main__":
    df = leer_frecuencias("PUT THE NAME OF YOUR TEXT HERE.txt")

    print(df)
