from collections import defaultdict

def get_stats(vocab):
    """
    Recebe um dicionário simulando o corpus e retorna as frequências 
    de todos os pares adjacentes de caracteres/símbolos.
    """
    pairs = defaultdict(int)
    for word, freq in vocab.items():
        symbols = word.split()
        for i in range(len(symbols)-1):
            pairs[symbols[i], symbols[i+1]] += freq
    return pairs