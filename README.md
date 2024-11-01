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
форма)

Результатом вычисления константного выражения является значение.
Для константных вычислений определены операции и функции:

1. Сложение.
2. Вычитание.
3. Умножение.
4. max().
5. min().

<br>

## Примеры:

Определение минимальной загрузки:
```
general server1load = 150;
general server2load = 250;
general server3load = 300;
general minimum = $server1load $server2load server3load min$ min$;
```

![image](https://github.com/user-attachments/assets/78bfc21c-d778-4dac-b1db-2c3837662b6c)

Вычисление стоимости товаров:
```
general amount = 150;
amount = $amount 100 +$;
general cost = 14;
general res = $amount cost *$;
```

![image](https://github.com/user-attachments/assets/b4ba9eba-21bd-4646-a1f6-fbb52dda94a7)

Использование в качестве калькулятора с запоминанием значений

```
general calc = ($654 131 *$, $131 131464 + $, $606 0 *$);
```

![image](https://github.com/user-attachments/assets/4cee61d8-68ba-4d0f-80ac-c4284d91826d)

## Как запустить:
1. Клонируем репозиторий
```bash
git clone https://github.com/Policarp-wq/ConfigurationLanguageParser.git
cd .\ConfigurationLanguageParser
```
2) Создаём и запускаем виртуальное окружение
```bash
python -m venv venv
venv\Scripts\activate
```
3) Устанавливаем зависимости
```bash
pip install -r requirements.txt
```
4) Запускаем скрипт
```bash
py .\visualizer.py --path [Путь к файлу для записи] 
```


5) Запуск тестирования:
   ```bash
   pytest -v
   ```

Вывод: 

![image](https://github.com/user-attachments/assets/b0d91577-2cb3-408a-a27c-45ec64d94226)






