# tarefa3.py
from transformers import AutoTokenizer

def testar_wordpiece():
    # Instancia o tokenizador multilingue do BERT
    tokenizer = AutoTokenizer.from_pretrained("bert-base-multilingual-cased")
    
    # Frase de teste para forçar o particionamento morfológico
    texto = "Os hiper-parâmetros do transformer são inconstitucionalmente difíceis de ajustar."
    
    # Utiliza o método tokenize() para segmentar a frase
    tokens = tokenizer.tokenize(texto)
    
    print(tokens)