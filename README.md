# Colorindo-Cenarios

**Número da Lista**: 6<br>
**Conteúdo da Disciplina**: Grafos1<br>

## Alunos

|Matrícula | Aluno |
| -- | -- |
| 18/0037439  |  Sérgio de Almeida Cipriano Júnior |
| 18/0030264  |  Antonio Igor Carvalho |

## Sobre 

&emsp;&emsp; Nosso trabalho almeja aplicar a famosa função de "colorir com balde" oferecida por editores de imagens, tais como o GIMP.
Utilizamos o algoritmo flood fill para realizar essa tarefa. Nossa ideia era mostrar visualmente o algoritmo funcionando.

&emsp;&emsp; Além disso, o trabalho foi feito pensando em facilitar expansão. Adicionar novos botões e novas funcionalidades é bem simples.
Inclusive, para brincar com novos algoritmos bastaria criar instâncias diferentes gerenciadas por um único menu.

&emsp;&emsp; Nosso foco foi em manter um escopo pequeno, prezando por qualidade. Assim, podemos expandir esse mesmo app durante toda a
disciplina, se necessário/desejado.

## Screenshots

As imagens estão disponíveis em [releases](https://github.com/projeto-de-algoritmos/Grafos1_Colorindo-Cenarios/releases).

## Instalação

**Linguagem**: python3

**Framework**: python3-pygame

**SO utilizado no desenvolvimento**: Debian GNU/Linux

&emsp;&emsp; Nossa instalação automatizada foi criada pensando no sistema operacional Debian e suas variantes. Caso necessite instalar em outro sistema operacional, confira o arquivo requirements que descreve os softwares necessários.

Primeiro, clone o repositório e entre na pasta:

```
$ git clone https://github.com/projeto-de-algoritmos/Grafos1_Colorindo-Cenarios.git
$ cd Grafos1_Colorindo-Cenarios
```

Instale os requisitos:

```
$ ./scripts/install.sh
```

Caso não tenha permissão de execução, execute:

```
$ chmod +x ./scripts/install.sh
```

Por fim, execute o app:

```
$ python3 ColorindoCenarios/main.py
```

## Testes

&emsp;&emsp; Para rodar os testes basta fazer:

```
$ cd ColorindoCenarios/
$ python3 nome_do_teste
```

## Uso

O programa consiste em três tipos de opções:
- DRAW
- CLEAR
- FLOODFILL (Representada pelos botões de cores)

&emsp;&emsp; A função DRAW seleciona a ferramenta para que o usuário desenhe na tela com a cor preta.

&emsp;&emsp; A função CLEAR faz com que a tela volte ao estado inicial(toda branca).

&emsp;&emsp; Os botões de cores funcionam para ativar a função flood fill.

Explicação por [vídeo](https://www.youtube.com/watch?v=sgMV80p0V0o&feature=youtu.be).
