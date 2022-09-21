# Modularidade (baixo acoplamento e alta coesão)

Modularidade seria a capacidade de um sistema ser dividido em partes independentes, que podem ser desenvolvidas e testadas de forma independente. Essas partes são chamadas de módulos, funções ou procedimentos. A modularidade é um dos princípios mais importantes da engenharia de software, pois permite que o sistema seja desenvolvido de forma mais rápida e eficiente. Além disso, a modularidade permite que o sistema seja mais fácil de ser mantido e evoluído.

Existem qualidades chaves da modularização que caracterizam um bom módulo, são elas:

  * Baixo acoplamento
  * Alta coesão

### Estrutura

A estrutura de um módulo é composta por:

  * Entradas
  * Saídas
  * Interfaces
  * Implementação

### Claridade

A claridade de um módulo é a capacidade de um módulo ser compreendido por um programador que não o desenvolveu. Para que um módulo seja claro, ele deve seguir algumas regras:

  * O nome do módulo deve ser claro e preciso
  * O módulo deve ser pequeno
  * O módulo deve ser simples
  * O módulo deve ser coeso
  * O módulo deve ser acoplado
  * O módulo deve ser independente
  * O módulo deve ser reutilizável
  * O módulo deve ser testável

## Baixo acoplamento

Acoplamento é a medida da dependência entre módulos. Um módulo com baixo acoplamento é aquele que depende de poucos outros módulos. Um módulo com alto acoplamento depende de muitos outros módulos. Um módulo com alto acoplamento é chamado de módulo espaguete, pois ele se parece com um macarrão espaguete. Um módulo com baixo acoplamento é mais fácil de ser mantido e evoluído, pois ele depende de poucos outros módulos. Um módulo com alto acoplamento é mais difícil de ser mantido e evoluído, pois ele depende de muitos outros módulos. Caso você desenvolva um módulo com alto acoplamento, você pode acabar tendo que modificar muitos outros módulos para fazer uma pequena alteração no módulo com alto acoplamento, isto faz com que o baixo acoplamento seja um dos princípios mais importantes da engenharia de software, otimizando o tempo de desenvolvimento e a qualidade do software.

## Alta coesão

Coesão é a medida da relação entre as responsabilidades de um módulo. Um módulo com alta coesão é aquele que tem uma única responsabilidade. Um módulo com baixa coesão é aquele que tem várias responsabilidades. Um módulo com baixa coesão é mais difícil de ser mantido e evoluído, pois ele tem várias responsabilidades. Um módulo com alta coesão é mais fácil de ser mantido e evoluído, pois ele tem uma única responsabilidade. Caso você desenvolva um módulo com baixa coesão, você pode acabar tendo que modificar muitos outros módulos para fazer uma pequena alteração no módulo com baixa coesão, isto faz com que a alta coesão seja um dos princípios mais importantes da engenharia de software, otimizando o tempo de desenvolvimento e a qualidade do software. Por isso é essencial que você, ao desenvolver, opte por módulos com baixo acoplamento e alta coesão. Facilitando assim o desenvolvimento e a manutenção do software.

## Relação de modularização com maus cheiros de código

### Código duplicado

Este mau cheiro é totalmente relacionado com a modularização, pois o fato de existir códigos redundantes faz com que as futuras mudanças e alterações sejam mais difíceis de serem feitas, pois o programador terá que alterar o código em vários lugares diferentes. Para evitar esse mau cheiro, é necessário que o programador faça a modularização do código, criando funções e procedimentos que possam ser reutilizados em outros lugares do código. Ou seja, a modularização é uma forma de evitar o mau cheiro de código duplicado.

### Método longo

Métodos longos refutam a alta coesão de um módulo, pois automaticamente são feitos para resolver mais de uma responsabilidade. Isto faz com que as mudanças e modificações sejam feitas e assim alterem consequentemente grande parte do código, oiu seja, um método longo também refuta o baixo acoplamento de um módulo. 

### Lista de parâmetros longa demais

Aqui podemos ver que a modularização também é uma forma de evitar o mau cheiro de lista de parâmetros longa demais, pois ao modularizar o código, o programador pode criar funções e procedimentos que recebam parâmetros e retornem valores, assim evitando que o programador tenha que passar muitos parâmetros para uma função ou procedimento. Aqui podemos recomendar o envio de objetos como parâmetros, pois assim o programador pode enviar apenas um objeto para a função ou procedimento, e assim evitar a lista de parâmetros longa demais.

### Cirurgia com rifle

Aqui podemos imaginar o caso em que o retorno de uma função seja de um tipo, por exemplo, o nome de uma pessoa, porém caso exista a necessidade de mudança de de tipo, no caso, vamos mudar para um objeto Pessoa, o programador terá que alterar o código em vários lugares diferentes, pois o retorno da função é utilizado em vários lugares diferentes. Neste caso é essencial que o tratamento do retorno do módulo também seja feito, ou que as modificações sejam feitas dentro do módulo e o retorno se mantenha o mesmo.


### Obsessão primitiva

Neste caso, podemos verificar que modularizações as quais recebem objetos ou classes são melhores adaptáveis pois podem se adequar ao objetivo o qual foi desenvolvido, ao invés de trabalhar com dados primitivos brutos, podemos ver que ele se relaciona bastante com o mau cheiro da lista de parâmetros longa demais.

### Classe preguiçosa

Aqui podemos destacar os métodos muito simples ou generalistas demais que são associados a uma classe e também representam um módulo, caso você possua um método que não vai ser utilizado mais de uma vez e que seja muito pequeno, seria uma boa opção removê-lo.

### Cadeias de mensagens

Aqui podemos mencionar as arquiteturas de middlewares ou funções simples que chamam outras funções, neste caso, é importante que a modularização não crie uma cadeia de mensagens, pois isso pode dificultar a manutenção do código. É essencial que as chamadas não sejam exageradas ou que não sejam feitas de forma desnecessária.

### Homem do meio

Aqui podemos relacionar diretamente este mau cheiro com as cadeias de mensagens, pois existem funções que são chamadas para no fim chamarem outras funções, isto faz com que existam condições que encaminham para outras funções e assim por diante, o que pode dificultar a manutenção do código. É importante que o programador não crie funções que chamem outras funções, pois isso pode dificultar a manutenção do código.

## Exemplo de refatoração utilizando modularização

Vamos utilizar a linguagem Python para exemplificar a refatoração utilizando modularização. Vamos supor que temos um código que verifica se um número é primo ou não, e que o código está da seguinte forma:

```python
def main():
    numero = int(input("Digite um número: "))
    if numero == 1:
        print("O número 1 não é primo")
    elif numero == 2:
        print("O número 2 é primo")
    else:
        for i in range(2, numero):
            if numero % i == 0:
                print("O número {} não é primo".format(numero))
                break
        else:
            print("O número {} é primo".format(numero))

if __name__ == "__main__":
    main()
```

Neste código, podemos verificar que o código está muito grande, e que ele possui muitas responsabilidades, pois ele verifica se o número é primo ou não, e também imprime a mensagem na tela. Para refatorar este código, vamos criar uma função que verifica se o número é primo ou não, e outra função que imprime a mensagem na tela, ficando da seguinte forma:

```python
def verifica_primo(numero):
    if numero == 1:
        return False
    elif numero == 2:
        return True
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return False
        else:
            return True

def imprime_mensagem(numero):
    if verifica_primo(numero):
        print("O número {} é primo".format(numero))
    else:
        print("O número {} não é primo".format(numero))

def main():
    numero = int(input("Digite um número: "))
    imprime_mensagem(numero)
```

### Autor

Ítalo Vinícius P. Guimarães