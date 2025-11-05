import os
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extraer_texto_pdf(ruta):
    texto = ""
    with open(ruta, 'rb') as f:
        lector = PdfReader(f)
        for pagina in lector.pages:
            texto += pagina.extract_text() or ""
    return texto

# Directorio con los PDF
carpeta = "pdfs/"
archivos = [f for f in os.listdir(carpeta) if f.endswith('.pdf')]

# Extraer texto de todos los PDFs
textos = [extraer_texto_pdf(os.path.join(carpeta, f)) for f in archivos]

# Calcular similitud
vectorizer = TfidfVectorizer().fit_transform(textos)
similitudes = cosine_similarity(vectorizer)

# Mostrar resultados
for i in range(len(archivos)):
    for j in range(i+1, len(archivos)):
        porcentaje = similitudes[i][j] * 100
        if porcentaje > 50:
            print(f"⚠️ Posible plagio entre '{archivos[i]}' y '{archivos[j]}': {porcentaje:.2f}%")
        else:
            print(f"{archivos[i]} vs {archivos[j]}: {porcentaje:.2f}%")
