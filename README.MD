# Финальный проект третьего спринта
### Для генерации данных можно использовать библиотеку [mimesis](https://mimesis.name/en/master/)

```python
from mimesis import Person
from mimesis.enums import Locale

person = Person(locale=Locale.RU)

with open('user_data.txt', "w", encoding='utf-8') as f:
    f.write('ФИО: ' + person.full_name() + '\n')
    f.write('Email: ' + person.email() + '\n')
    f.write('Password: ' + person.password(length=6))
```