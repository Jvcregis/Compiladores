# IF688 - Teoria e Implementação de Linguagens Computacionais

## Atividade 3 - Type Checking com Escopos

Este exercício visa trabalhar os conceitos de análise semântica vistos em sala de aula. A ideia é implementar um checador de tipos para a linguagem simples que temos desenvolvido em aula, levando em consideração escopo de bloco, o que permite *shadowing* de variáveis.

Para simplificar o processo de desenvolvimento, é fornecido aqui um esqueleto de código disponível em `visitor.py` como ponto de partida para implementar o analisador (veja a classe `TypeCheckVisitor`), bem como alguns testes para verificar a corretude da sua implementação usando a biblioteca `pytest` (se não tiver a biblioteca instalada, rode `pip3 install pytest`). 

**O seu repositório será avaliado automaticamente pelo Github Classroom, rodando os testes por meio de uma Github Action. Esta ferramenta só avalia commits enviados até a data limite, portanto tenha em mente isso.**

O único arquivo que deve ser enviado **também** no Google Classroom é a sua versão de `visitor.py`, e o nome do arquivo deve ser o seu login. Então, no meu caso seria `lmt.py`.

## Instruções

A sua resolução precisa implementar todas as funções da classe `TypeCheckVisitor` em `visitor.py` cujo corpo atualmente está com o conteúdo `pass`. O código já existente no restante do arquivo **não precisa, nem deve** ser modificado, inclusive os métodos da classe `GenericVisitor`.

## ATENÇÃO!

Você **_não precisa_, *nem deve***, alterar nada do esqueleto de projeto dado além do arquivo `visitor.py` com a sua implementação.

### Testando o Projeto
- Faça o download deste projeto;
- Caso ainda não tenha `pytest` instalada, rode `pip3 install pytest`
- Na linha de comando, rode `pytest` e veja que a maioria dos testes não estão passando; 
- Implemente as funções descritas acima em `visitor.py`, usando apenas a parte dedicada do arquivo para tanto;
- Use o arquivo `basic.py` se quiser rodar algo no console e observar o *output*.