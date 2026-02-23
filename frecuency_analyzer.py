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
print(frec_ngramas("PUT THE CIPHERTEXT HERE AND THE NUMBER OF N-GRAMS TO ANALYZE IN THE LEFT", 2))