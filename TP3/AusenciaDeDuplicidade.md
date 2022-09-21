# Ausência de duplicidades

Um código bem projetado não possui duplicação. A duplicação vai contra os princípios do design elegante e simples. Com códigos redundantes e desnecessários levam a um programa frágil: pois tendo duas partes de código semelhantes que diferem apenas em pequenos detalhes, é possível que ao encontrar e corrigir um bug em um, e depois não lembrar de corrigir o mesmo bug no outro. Dessa maneira, claramente compromete a segurança do código. 
Logo, quando identificado bloco de códigos semelhantes sendo feitas por seções separadas de código, é melhor generalizar em uma função com parâmetros apropriados. Sendo assim, haverá um único lugar para corrigir quaisquer falhas. Isso tem a vantagem de tornar a intenção do código mais clara com um nome de função descritivo. Classes que são surpreendentemente semelhantes indicam que algumas funcionalidades podem ser enviadas para uma superclasse ou que há uma interface ausente para descrever o comportamento comum.

## Eliminando maus-cheiros de código

Um código com Ausência de duplicidades ajuda a eliminar diversos maus-cheiros de código, como, código duplicado, classes alternativas com interfaces diferentes e cirurgia com rifle. Um exemplo claro de como a Ausência de duplicidades evita a cirurgia com rifle é caso tenha algum bloco de código com um bug em que foi copiado e colado em vários locais diferentes. Dessa forma, seria necessário ficar buscando e corrigindo repetidas vezes o mesmo bug, logo, é possível que passe desapercebido em algum local. Portanto, a Ausência de duplicidades naturalmente evita a criação de maus-cheiros, devido as suas boas práticas intrínsecas. 


## Exemplo de refatoração utilizando código com Ausência de duplicidades

Aqui temos dois métodos que fazem praticamente a mesma coisa, mas diferem apenas no tipo em que operam. Os genéricos nos dão a capacidade de realmente refatorar essas informações de tipo, assim como faríamos com os dados.

- Exemplo, em C#, de métodos semelhantes:
```C#
public int FindIntMatch(int i){
   var match = (int)container.Get(i);
   return match;
}
 
public string FindStringMatch(string s){
   var match = (string)container.Get(s);
   return match;
}
```
- Exemplo de Ausência de duplicidade em C#, evitando o mau-cheiro de cirurgia com rifle. Ao refatorar para o método abaixo, eliminamos a duplicação e caso tenha algum erro precisaríamos corrigir em somente um método.
```C#
public T FindMatch(T t){
   var match = (T)container.Get(t);
   return match;
}
```

### Autor

Ítalo Fernandes S. de Serra