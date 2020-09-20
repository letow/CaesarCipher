# Caesar Cipher (Шифр Цезаря)
____
## Принцип работы

**Шифр Цезаря** — это вид шифра подстановки, в котором каждый символ в открытом тексте заменяется символом, находящимся на некотором постоянном числе позиций левее или правее него в алфавите. Например, в шифре со сдвигом вправо на 3, A была бы заменена на D, B станет E, и так далее.
Пример:

![](https://link.gerki.ws/attachments/2137/ "Шифр Цезаря со сдвигом 3")

## Описание работы программы

Данная программа является шифратором, использующим сдвиг Цезаря для кодирования и декодирования введенных пользователем сообщений.
Программа дает пользователю выбор режима работы программы: шифровка, расшифровка или выход из программы (1, 2 и 0, соответственно).
После этого предлагает выбрать алфавит (русский или английский),  ввести шаг сдвига и само сообщение.
На выходе получается зашифрованное или расшифрованное сообщение.

## Пример работы программы
Для примера возьмем словосочетание "Zoopark Yota" и прогоним его через цикл "зашифровать-расшифровать", после чего выйдем из программы.
#### Пример шифрования и расшифровки сообщения с последующим завершением программы

![](https://i.imgur.com/J3S4sOb.jpg "Шифрование сообщения")

Вернулось то же самое словосочетание, значит программа работает.

## Работа с программой
### Выбор IDE для запуска
Программа написана на ЯП Python 3 и является консольным приложением (без графического интерфейса), следовательно, для ее запуска необходима среда разработки, поддерживающая файлы формата ".py" (например, я использовал PyCharm).
Можно воспользоваться и онлайн-редакторами кода Python, но при копировании может слететь табуляция, на что Питон будет ругаться.
### Запуск
Запуск программы осуществляется посредством открытия файла "main.py", расположенного в этом репозитории.
### Как работать с программой
См. раздел "Описание работы программы".
Можно еще добавить, что в программе пристуствует "защита от дурака", так что все вводимые значения проверяются на валидность. Поэтому если Вы вдруг введете, что-то неправильно, программа сообщит, что не так.
