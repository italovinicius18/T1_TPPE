# T1_TPPE

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 18/0096991  |  Álvaro Leles |
| 18/0102087  |  Ian Fillipe |
| 18/0102613  |  Ítalo Fernandes |
| 18/0102656  |  Ítalo Vinicius |
| 18/0103431  |  João Victor Valadão |

## Instalação 
**Linguagens**: Python 3.X<br>
```
Caso não tenha o pytest instalado, instale-o usando o comando:
    pip install pytest
```

## Uso (Windows)

```
Para rodar o programa, basta, na pasta raiz do repositório, digitar o comando:
    
    python main.py

Para rodar os testes, basta, na pasta raiz do repositório, digitar o comando:
    pytest

E para rodar cada grupo de teste de forma individual, deve-se escolher o arquivo e digitar:
    pytest <nomeArquivo>
```

## TP3 - Bons projetos de software

### Elegância

- A elegância de um código tem relação com a estética do projeto e na maioria das vezes está diretamente relacionada com a simplicidade do código, ou seja, não se tem no código trechos muito complexos ou muito complicados de se entender ao revisá-lo. Um bom projeto possui estruturas agradáveis de se observar. Algumas características que compõem um código elegante são: Fluídez sensata ao longo do sistema, ou seja, operações que passam apenas pelos módulos necessários; Complemento e conexão entre as partes; Não há muitas exceções para as regras estabelecidas; Não existência de artimanhas (gambiarra) para solucionar os problemas; Mudanças em pequenos trechos do código não afetam muitos outros lugares.
- Pode-se associar essa característica com muitos maus-cheiros como: Código duplicado (atrapalha a fluídez), método longo e classe inchada (adiciona complexidade desnecessária), lista de parâmetros longa demais (informações desnecessárias passando por módulos que não as utilizarão), cirurgia com rifle (complexidade elevada). Além destes, outros maus-cheiros podem ser relacionados com essa característica, evidenciando ainda mais os benefícios da aplicação desta característica.
- Extração de método é um exemplo de operação de refatoração que pode ser aplicado para favorecer a elegância de um código, já que este método favorece uma simplicidade de código, remoção de código duplicado, além de também contribuir para que cada módulo seja utilizado corretamenta apenas quando necessário
