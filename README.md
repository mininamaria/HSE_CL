# Создание словаря
Каждому человеку рано или поздно нужно создать словарь для хранения английских и русских слов на Python. Но могут возникнуть некоторые проблемы.
## Защита от *дураков*
Что они могут сделать не так:
* Ввести цифры
* Использовать русские и английские буквы в одном слове
* Ввести два слова на одном языке
```python
if ('0'<= w1[i]) and (w1[i] <= '9'):
        sys.exit("Please, do not use numbers")
    else:
        if (('a' <= w1[i]) and (w1[i] <= 'z')) or (('A' <= w1[i]) and (w1[i] <= 'Z')):
            cnt1 += 1
        elif (('а' <= w1[i]) and (w1[i] <= 'я')) or (('А' <= w1[i]) and (w1[i] <= 'Я')):
            cnt2 += 1
```
Сообщения их **напугают**
