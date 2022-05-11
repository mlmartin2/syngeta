# Syngeta - Desafio Técnico

Software para analisar opções de hotéis com menor custo ou melhor custo-benefício dada as datas de estadia e dado o tipo de assinatura do usuário

## Classes
hotel.py:

**Hotel**:
classe para hotel, modelada a partir dos dados fornecidos para o desafio.

 - **name**: nome do hotel
 - **classification**: classificação de qualidade do serviço
 - **day_rates**: taxas de usuários Rewards/Regular, dependendo do
 da semana (Fim de semana ou Dia de semana)

## Funções
argdecoder.py:

**decode_defaultArgument( default_argument: string ):**
decodifica argumento padrão fornecido, retornando valores numéricos
das informações relevantes (Tipo de assinatura, dias da semana marcados)

**slice_defaultArgument( default_argument: string):**
prepara a string do argumento padrão para tratamento no codificador. Separa em
array bidimensional de strings, com a primeira posição contendo o tipo de assinatura
do usuário, e a segunda posição contendo array de datas marcadas

**get_weekdayValue_fromString(str: string):**
getter do valor numérico para dias da semana. A função recebe uma string
no formato de data DDmonthYYYY(weekday), exemplo: 15Dec2012(mon)
e retorna o valor, sendo 0 = Segunda-Feira -> ... -> 6 = Domingo

## Formatos
1. **Argumento padrão:**

> `<Subscription>:<Date1>,<Date2>,<Date3>,...,<DateN>`

   Exemplo:
   

> `Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)`

2. **Data**

> `DDmonthYYYY(weekday)`

Exemplo:

> `15Dec2012(mon)`
## FAZER
 - [ ] Tornar get_cheapest_hotel compatível com argumentos numéricos
 - [ ] Testar funcionalidade no console
 - [X] Consertar testes não funcionando quando imports não contém **src.** antes