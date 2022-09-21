# Simplicidade

Uma das características mais importantes para o desenvolvimento de um projeto consistente, a Simplicidade busca facilitar a compreensão e entendimento daquilo que está sendo desenvolvido. Uma vez que dessa forma, toda a equipe poderá ter maior conhecimento de todas as partes do código, além do fato que as ações de reparo realizado por terceiros que não estão familiarizados com a arquitetura do projeto, será realizada de maneira mais eficiente.

Priorizando sempre a consistência e compreensão do código, a Simplicidade se baseia na ideia do "Less is more", ou seja, buscar sempre desenvolver um código pequeno que abranja uma ampla vasta de funcionalidades, ao invés de algo complexo que funcionará em proporções reduzidas. Ainda assim, a "complexidade" ainda é vista erroneamente como um benefício em ambientes de desenvolvimento, ao invés de tentar evitá-la. A complexidade esconde erros, cria dificuldades para os processos de manutenções além de dificultar a leitura dentro da própria organização ou equipe. Desse modo, bons programadores devem sempre buscar combater a complexidade e buscar produzirem o mais simples possível, aperfeiçoando suas habilidades.

## Eliminando maus-cheiros de código

Um código simples ajuda a eliminar grande parte dos maus-cheiros de código, sendo classificada como uma das características mais importantes para desenvolvimento de software, como: código duplicado, método longo e classe grande, lista de parâmetros longa demais, cirurgia com rifle, aglomerado de dados, dentre outros que apresentam potencial para refatoração e assim serem aplicadas esses pontos de melhoria.

## Exemplo de refatoraçao utilizando Simplicidade

Um exempli de operação de refatoração que pode ser aplicada para favorecer a simplicidade de um código é reduzir seu tamanho original, descartando linhas desnecessárias. Favorecendo a simplicidade do código, pois ela permite que o código fique mais legível e mais fácil de ser entendido, além de da facilidade em trabalhar com suporte. No exemplo abaixo, foi utilizado o método de refatoração de redução de tamanho de código, que consiste em remover linhas de código que não são necessárias para o funcionamento do programa. Por exemplo, no código abaixo implementa uma função que some os números em uma frase onde os só devam ser considerados os números que não estão ligados a palavras (caracteres de texto). O código original possui várias linhas, enquanto o código refatorado retorna o mesmo resultado com apenas uma linha de código.

- Exemplo de código original em Python:
```python
def sum_numbers(text: str) -> int:
    x = text.split()
    soma = 0
    for i in range(len(x)):
        y = x[i].isdigit()
        if y:
            soma = soma + int(x[i])
    return soma
```

- Exemplo de código refatorado em Python:
```python
def sum_numbers(text: str) -> int:
    return sum(( int(word) for word in text.split() if word.isdigit()))
```