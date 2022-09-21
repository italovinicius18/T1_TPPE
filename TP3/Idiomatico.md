# Idiomático

No _Wiktionary_, "idiomático" é definido como "pertencente ou conforme ao modo natural de expressão de uma língua". No contexto de programação, um código idiomático é aquele que segue as convenções e boas práticas da linguagem de programação utilizada. Desta maneira, um código idiomático é mais fácil de ser lido e entendido por outros desenvolvedores que usam a mesma linguagem, sendo que esse maior entendimento é de extrema importância, pois isso torna o código mais fácil de ser mantido, já que se torna mais fácil alterá-lo.

Um exemplo na prática do que é um código idiomático pode ser visto na linguagem Python, na qual o engenheiro de software Tim Peters escreveu um conjunto de 19 princípios orientadores para se criar código em Python, princípios estes que foram criados por um usúario da linguagem e que toda a comunidade de desenvolvedores de Python adotou como um padrão de boas práticas. Estes princípios são conhecidos como "The Zen of Python" e foram escritos no formato de um poema, que pode ser visto abaixo:

```
Bonito é melhor que feio.
Explícito é melhor que implícito.
Simples é melhor que complexo.
Complexo é melhor que complicado.
Linear é melhor do que aninhado.
Esparso é melhor que denso.
Legibilidade conta.
Casos especiais não são especiais o bastante para quebrar as regras.
Ainda que praticidade vença a pureza.
Erros nunca devem passar silenciosamente. 
A menos que sejam explicitamente silenciados.
Diante da ambiguidade, recuse a tentação de adivinhar.
Dever haver um — e preferencialmente apenas um — modo óbvio para fazer algo.
Embora esse modo possa não ser óbvio a princípio a menos que você seja holandês.
Agora é melhor que nunca.
Apesar de que nunca normalmente é melhor do que *exatamente* agora
Se a implementação é difícil de explicar, é uma má ideia
Se a implementação é fácil de explicar, pode ser uma boa ideia
Namespaces são uma grande ideia — vamos ter mais dessas!
```

Consequentemente, cada verso do poema simboliza um padrão de escrita da linguagem Python que a comunidade prioriza seguir, por exemplo:

- No primeiro verso, "Bonito é melhor que feio", em uma situação como a abaixo, a comunidadade de Python prefere a segunda opção, pois a primeira é mais difícil de ser lida e entendida:

```python
if funcao(x) && y == 0 || z == 'yes':
```
```python
if funcao(x) and y == 0 or z == 'yes':
```

## Eliminando maus-cheiros de código

Um código idiomático ajuda a eliminar maus-cheiros de código, como: código duplicado, método longo e classe inchada, lista de parâmetros longa demais, cirurgia com rifle, dentre outros. Sendo que, um código idiomático por natureza evita a criação de maus-cheiros, pois ele segue as boas práticas que a documentação e a comunidade lentamente foram construindo. 


## Exemplo de refatoração utilizando código idiomático

Um exemplo de operação de refatoração que pode ser aplicada para favorecer a idiomatização de um código é a decomposição de condicionais. Esta operação de refatoração é muito útil para favorecer a idiomatização de um código, pois ela permite que o código fique mais legível e mais fácil de ser entendido, além de também favorecer a eliminação de Método longo.

- Exemplo de método longo em Python:
```python
def calcular_media(self, notas):
    soma = 0
    for nota in notas:
        soma += nota
    return soma / len(notas)
```
- Exemplo de código idiomático em Python, evitando o mau-cheiro de método longo:
```python
def calcular_media(self, notas):
    return sum(notas) / len(notas)
```

### Autor

Ian Fillipe Pontes Ferreira
