# Laboratório Técnico 06: Construindo um Tokenizador BPE e Explorando o WordPiece

Este repositório contém a entrega do Laboratório 06 do iCEV. O objetivo é construir do zero o motor básico do algoritmo **Byte Pair Encoding (BPE)** para entender como modelos de linguagem e a arquitetura Transformer processam tensores numéricos mapeados a partir de um vocabulário, em vez de strings de texto puras. A abordagem de sub-palavras é o padrão da indústria para lidar com palavras raras e manter o tamanho do vocabulário otimizado, geralmente entre 32.000 a 37.000 tokens.

## Bibliotecas Utilizadas

* **Python 3.x**
* **transformers** (Hugging Face) 
* **re** (Expressões Regulares) 
* **collections** (Contagem de frequências)

## Como rodar o código

1. Clone este repositório no seu ambiente local.
2. É recomendado usar o seu ambiente virtual já configurado:
```bash
source venv/bin/activate
```

3. Instale as bibliotecas necessárias através do arquivo de requerimentos:
```bash
pip install -r requirements.txt
```

4. A execução está centralizada no script principal que orquestra as tarefas:
```bash
python3 main.py
```

## O que o script faz

Diferente de tokenizadores baseados apenas em espaços, este projeto implementa a lógica de segmentação por sub-palavras utilizada em modelos como BERT. O sistema executa três tarefas principais:

1. **O Motor de Frequências (Tarefa 1):** Inicia com um corpus onde as palavras são separadas em caracteres e acrescidas do símbolo de fim de palavra `</w>`. A função `get_stats` varre o dicionário `vocab` para contar a frequência de cada par de símbolos adjacentes.

2. **O Loop de Fusão (Tarefa 2):** Após identificar o par mais frequente, o algoritmo realiza uma fusão (*merge*), criando um novo token para o vocabulário. O processo é executado em um loop de $K=5$ iterações, imprimindo o par fundido e o estado atualizado do vocabulário a cada rodada.

3. **Integração Industrial e WordPiece (Tarefa 3):** Utiliza a biblioteca `transformers` para instanciar o tokenizador multilingue do BERT (`bert-base-multilingual-cased`), que utiliza a lógica WordPiece. O script segmenta uma frase complexa projetada para forçar o particionamento morfológico.

---

## Lógica Matemática (Requisito do Contrato Pedagógico)

O algoritmo BPE funciona através da identificação iterativa de padrões estatísticos. Em cada etapa, ele busca o par de caracteres $(a, b)$ com a maior frequência conjunta no corpus. Ao fundi-los em um novo símbolo único $ab$, o algoritmo reduz o comprimento das sequências representadas, transformando caracteres individuais em morfemas e, eventualmente, palavras inteiras. Essa eficiência permite que modelos de tradução de ponta criem representações robustas para sequências comuns. No WordPiece, embora a lógica de sub-palavras seja mantida, a decisão de fusão baseia-se em regras probabilísticas ligeiramente diferentes para maximizar a verossimilhança dos dados de treinamento.

## Validação de Resultados

Ao rodar os scripts, o console exibirá:

* **Validação da Tarefa 1:** O par `('e', 's')` retorna a contagem máxima de **9**, confirmando a precisão do motor de frequências.
* **Evolução do BPE:** O log das 5 iterações demonstra a formação de tokens morfológicos lógicos, especificamente o sufixo `est</w>`.
* **Segmentação WordPiece:** A frase *"Os hiper-parâmetros do transformer são inconstitucionalmente difíceis de ajustar"* é decomposta em tokens menores.

## Relatório: O significado do `##`

Os sinais de cerquilha (**##**) nos tokens resultantes (como em `##mente`) indicam que aquele fragmento é uma sub-palavra que não inicia uma sequência, funcionando como uma marcação de continuidade de um token anterior. O uso dessas sub-palavras é o que impede o travamento do modelo diante de vocabulário desconhecido, pois permite que palavras raras sejam construídas a partir de componentes conhecidos.



## Nota de Crédito

Partes geradas/complementadas com IA, revisadas por Anderson.

Conforme as regras da disciplina e o contrato pedagógico sobre o uso de IA Generativa, registro que utilizei o assistente virtual para:
* Construir a lógica de expressões regulares para a função `merge_vocab` na Tarefa 2.
* Estruturar a modularização dos arquivos Python e a organização deste `README.md`.