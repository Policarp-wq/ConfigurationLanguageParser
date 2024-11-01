# Парсер из учебного языка в yaml


## Синтаксис учебного языка

Массивы:
( значение, значение, значение, ... )
Имена:
[a-z][a-z0-9_]*
Значения:
- Числа.
- Массивы.
  
Объявление константы на этапе трансляции:
global имя = значение;

Вычисление константного выражения на этапе трансляции (постфиксная
форма), пример:

$имя 1 +$

Результатом вычисления константного выражения является значение.
Для константных вычислений определены операции и функции:

1. Сложение.
2. Вычитание.
3. Умножение.
4. max().
5. min().
