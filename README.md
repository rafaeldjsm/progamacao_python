# Exercícios Básicos executados no aprendizado de Python.

## [Jogo Nim](https://github.com/rafaeldjsm/Data_Science/blob/8e3eba2e4d9693338c3e567ae801e01f8ffb51ad/Exercicios_basicos/jogo_nim.py)

Nesse jogo, n peças são inicialmente dispostas numa mesa ou tabuleiro. Dois jogadores jogam  alternadamente, retirando pelo menos 1 e no máximo m peças cada um. Quem tirar as últimas peças possíveis ganha o jogo.

Existe uma estratégia para ganhar o jogo que é muito simples: ela consiste em deixar sempre múltiplos de (m+1) peças ao jogador oponente.
### Objetivo
Você deverá escrever um programa na linguagem Python, versão 3, que permita a uma "vítima" jogar o NIM contra o computador. O computador, é claro, deverá seguir a estratégia vencedora descrita acima.

Sejam n o número de peças inicial e m o número máximo de peças que é possível retirar em uma rodada. Para garantir que o computador ganhe sempre, é preciso considerar os dois cenários possíveis para o início do jogo:

>>> Se n é múltiplo de (m+1), o computador deve ser "generoso" e convidar o jogador a iniciar a partida com a frase "Você começa!"

>>> Caso contrário, o computador toma a inciativa de começar o jogo, declarando "Computador começa!"

Uma vez iniciado o jogo, a estratégia do computador para ganhar consiste em deixar sempre um número de peças que seja múltiplo de (m+1) ao jogador. Caso isso não seja possível, deverá tirar o número máximo de peças possíveis.

Seu trabalho, então, será implementar o Jogo e fazer com que o computador se utilize da estratégia vencedora.

### Seu Programa
Com o objetivo do EP já definido, uma dúvida que deve surgir nesse momento é como modelar o jogo de forma que possa ser implementado em Python 3 correspondendo rigorosamente às especificações descritas até agora.

Para facilitar seu trabalho e permitir a correção automática do exercício, apresentamos a seguir um modelo, isto é, uma descrição em linhas gerais de um conjunto de funções que resolve o problema proposto neste EP. Embora sejam possíveis outras abordagens, é preciso atender exatamente o que está definido abaixo para que a correção automática do trabalho funcione corretamente.

O programa deve implementar:

>>> Uma função computador_escolhe_jogada que recebe, como parâmetros, os números n e m descritos acima e devolve um inteiro correspondente à próxima jogada do computador (ou seja, quantas peças o computador deve retirar do tabuleiro) de acordo com a estratégia vencedora.

>>> Uma função usuario_escolhe_jogada que recebe os mesmos parâmetros, solicita que o jogador informe sua jogada e verifica se o valor informado é válido. Se o valor informado for válido, a função deve devolvê-lo; caso contrário, deve solicitar novamente ao usuário que informe uma jogada válida.

>>> Uma função partida que não recebe nenhum parâmetro, solicita ao usuário que informe os valores de n e m e inicia o jogo, alternando entre jogadas do computador e do usuário (ou seja, chamadas às duas funções anteriores). A escolha da jogada inicial deve ser feita em função da estratégia vencedora, como dito anteriormente. A cada jogada, deve ser impresso na tela o estado atual do jogo, ou seja, quantas peças foram removidas na última jogada e quantas restam na mesa. Quando a última peça é removida, essa função imprime na tela a mensagem "O computador ganhou!" ou "Você ganhou!" conforme o caso.

Observe que, para isso funcionar, seu programa deve sempre "lembrar" qual é o número de peças atualmente no tabuleiro e qual é o máximo de peças a retirar em cada jogada.

### Campeonatos
Como todos sabemos, uma única rodada de um jogo não é suficiente para definir quem é o melhor jogador. Assim, uma vez que a função partida esteja funcionando, você deverá criar uma outra função chamada campeonato. Essa nova função deve realizar três partidas seguidas do jogo e, ao final, mostrar o placar dessas três partidas e indicar o vencedor do campeonato. O placar deve ser impresso na forma

**Placar: Você ??? X ??? Computador**

### Execução
Dado que é possível jogar partidas individuais ou campeonatos, seu programa deve começar solicitando ao usuário que escolha se prefere jogar apenas uma partida (opção 1) ou um campeonato (opção 2).


# [**Leap Year**](https://github.com/rafaeldjsm/progamacao_python/blob/main/is_leap.py)

An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

In the Gregorian calendar, three conditions are used to identify leap years:

- The year can be evenly divided by 4, is a leap year, unless:
  - The year can be evenly divided by 100, it is NOT a leap year, unless:
    - The year is also evenly divisible by 400. Then it is a leap year.<br>

This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. [Source](https://www.timeanddate.com/date/leapyear.html)

**Task**

Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

Input Format

Read , the year to test.

Constraints

$1900 \leq year \leq 10^{5}$


Output Format

The function must return a Boolean value (True/False).
