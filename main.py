# main.py
from tarefa1 import get_stats
from tarefa2 import treinar_bpe
from tarefa3 import testar_wordpiece

def main():
    # Dicionário inicial limpo e formatado corretamente a partir do PDF
    vocab = {
        'l o w </w>': 5,
        'l o w e r </w>': 2,
        'n e w e s t </w>': 6,
        'w i d e s t </w>': 3
    }
    
    print("--- INICIANDO VALIDAÇÃO DA TAREFA 1 ---")
    pares = get_stats(vocab)
    print(f"Contagem do par ('e', 's'): {pares.get(('e', 's'), 0)}") # Deve obrigatoriamente retornar 9
    
    print("\n--- INICIANDO TAREFA 2: LOOP BPE ---")
    treinar_bpe(vocab, iteracoes=5) # K=5
    
    print("--- INICIANDO TAREFA 3: TESTE WORDPIECE ---")
    testar_wordpiece()

if __name__ == "__main__":
    main()