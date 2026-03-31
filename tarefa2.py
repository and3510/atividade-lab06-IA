import re
from tarefa1 import get_stats

def merge_vocab(pair, v_in):
    """
    Substitui todas as ocorrências de um par isolado pela sua versão unificada.
    """
    v_out = {}
    # Utilizamos expressões regulares para garantir que fundimos apenas os pares exatos, 
    # respeitando os espaços que separam os tokens no formato BPE.
    bigram = re.escape(' '.join(pair))
    p = re.compile(r'(?<!\S)' + bigram + r'(?!\S)')
    
    for word in v_in:
        w_out = p.sub(''.join(pair), word)
        v_out[w_out] = v_in[word]
    return v_out

def treinar_bpe(vocab, iteracoes=5):
    """
    Loop Principal de Treinamento do Tokenizador.
    Executa sucessivamente por um número K de iterações.
    """
    v = vocab.copy()
    for i in range(iteracoes):
        pairs = get_stats(v)
        if not pairs:
            break
        
        # Identifica o par mais frequente
        best = max(pairs, key=pairs.get)
        
        # Imprime o par mais frequente fundido naquela rodada
        print(f"Iteração {i+1} | Par fundido: {best}")
        
        # Atualiza o vocabulário
        v = merge_vocab(best, v)
        
        # Imprime o estado do dicionário após a fusão
        print(f"Estado do dicionário: {v}\n")
    
    return v