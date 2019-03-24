# Proteins match challange

## Definição do problema

Uma demanda frequente em Bioinformática é o cruzamento de base de dados (cross-reference) para encontrar coisas em comum. Este desafio consiste em comparar dois conjuntos de dados, que contém nomes de proteínas, procurando por similaridades entre elas.
O primeiro conjundo de dados (dataset A) contém proteínas de um experimento das quais deseja-se encontrar suas referências. O segundo conjunto (dataset B) consiste em uma base curada de dados que será utilizado como referência.

## Regras

O intuito é buscar no dataset B as possíveis referêcias para proteínas do dataset A, levando em consideração as seguintes regras:

### Pré-similaridade
- Devem ser igonadas quaisquer palavras com 3 ou menos caracteres.
- Devem ser ignorados caracteres alfanuméricos.
- Devem ser ignorados todos os caracteres especiais.
- Devem ser igonorados quaiser palavras dentro de colchetes (`[]`).
- Devem ser desconsideradas quaisquer proteínas que contenham a palavra `hypothetical` em seu nome.

### Similaridade
- As proteínas devem ser comparadas de acordo com a quantidade de palavras em comum que elas possuem.
- Se qualquer uma das keyswords tiverem uma quantidade nula de palavras a similaridede deve ser 0.
- O tamanho do maior nome não pode interferir na comparação
- A ordem de comparação não é importante, ou seja, os conjuntos `A1 = ('foo', 'bar', 'foobar')` e `B1 = ('barfoo','bar')` têm similaridade de `0.5`, assim como `A2 = ('foo', 'foobar')` e `B2 = ('barfoo','bar','foo','barbar')`.

### Desempate
- Proteínas que contenham a palavra `putative` são menos importante do que as que não possuem.
- Proteínas que contenham a palavra `predicted` são menos importante do que as que não possuem.
- Proteínas que contenham a palavra `putative` são menos importante do que as que possuem a palavra `predicted`.


## Funções a serem implementadas

 - `s0_load_file`:
 Carrega um arquivo no formato de tabela a partir do disco rígido e retorna os nomes das proteínas de uma determinada coluna do arquivo.

 - `s1_pre_process_name`:
 Realiza o pré-processamento do nome de protínas, segundo as regras de [__pré-similaridade__](#pré-similaridade) especificadas acima. Retorna um conjunto de palavras chaves que representa a proteína.

 - `s2_find_match`: 
 Realiza a comparação de dois conjutos de palavras chaves (`keys_a` e `keys_b`), segundo as regras de [__similaridade__](#similaridade) . `keys_a` e `keys_b` são referentes as palavras chaves das proteínas do dataset A e B, respectivamente. Retorna um valor entre 0 e 1 representando a similaridade entre elas, sendo:
 - - 0: nada similar e; 
 - - 1: totalmente similar (ou uma está contida na outra). 

 - `s3_compare_match`:
 Aplica as regras de desempate entre as keywords do dataset (keys_a e keys_b), segundo as regras de [__desempate__](#desempate). Retorna um valor inteiro que representa o pareamento de ambas. Sendo:
- - 0: totalmente pareadas;
- - menor que 0: keys_a tem maior valor que keys_b e;
- - maior que 0: keys_a tem menor valor que keys_b;

## O que se espera
- O problema deve ser resolvido utilizando a linguagem de programação Python (versão 3.5 ou mais recente). 
- Devem ser utilizadas apenas funções ou módulos nativos do Python, incluindo [Built-in Functions](https://docs.python.org/3.6/library/functions.html), [String Methods](https://docs.python.org/3.6/library/stdtypes.html#string-methods), [CSV File Reading and Writing](https://docs.python.org/2/library/csv.html?highlight=csv#module-csv) e [Regular expression operations](https://docs.python.org/3.6/library/re.html?#module-re). 
- Espera-se que sejam propostas abordagens escaláveis para o processamento de um grande input de dados . (_Dica: a partir da versão 3, a funções `map` retorna um iterator ao invés de uma lista, o que pode tornar sua utilização mais otimizada_).
