import unicodedata

def remove_accents(text):
    normalized = unicodedata.normalize('NFKD', text)
    return ''.join(c for c in normalized if unicodedata.category(c) != 'Mn') # Essa linha filtra os caracteres que não são marcas de acentuação (Mn).
"""
Acima temos uma função que remove acentos de uma string.
Ela funciona normalizando a string para o formato NFKD (Normalization Form KD)
e, em seguida, filtrando os caracteres que não são marcas de acentuação (Mn).
Isso resulta em uma string sem acentos.
"""
