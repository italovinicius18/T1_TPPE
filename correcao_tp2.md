UnB - Universidade de Brasilia  
FGA - Faculdade do Gama  
TPPE - Técnicas de Programação para Plataformas Emergentes  

### Correção Trabalho Prático 2 - _Refactoring_

---

- **Critério 1 -** Aplicação da operação ``Extrair Método``: (35 pontos)  
  _Foi criado novo método com o nome explicando o seu propósito? Os locais em
que havia o método foram substituídos por chamadas ao novo método? Não há mais
código duplicado?  (-10 pontos por erro encontrado)_  
  Obs.: foram extraídas instruções de formatação de datetime para novos métodos.
Ok.
  Nota: 30/30 pontos.

- **Critério 2 -** Aplicação da operação ``Substituir método por objeto-método``: (50 pontos)  
  _Foi criada uma nova classe com o método ``Computar()``? O construtor recebe
os parâmetros do método de origem e a referência do objeto de origem? O
método-objeto utiliza os atributos da sua própria classe? O método de origem foi
substituído pela chamada ao método de origem? (-10 pontos por erro encontrado)_  
  Obs.: Não há referência para objeto da classe de origem do método. O
construtor da classe Cadastrar_acesso não recebe referencia para o objeto de
origem do método-objeto. Elementos do objeto de origem não foram acessados a
partir do método objeto (foram movidos juntos?). 
  Nota: 20/50 pontos.

- **Critério 3 -** Aplicação da operação ``Extrair constante``: (15 pontos)  
  _Para todos os valores espalhados pelo código foram definidas constantes
simbólicas e tais constantes foram utilizadas? (-5 pontos por constante não
definida/substituída)_  
  Obs.: Ok! 
  Nota: 15/15 pontos.

**NOTA FINAL:** 65/100 pontos.
