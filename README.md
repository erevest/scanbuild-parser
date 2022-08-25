# clang_db_parser
Parse code issues from clang scan-build html page to psql database. The code is very human

1. Install psql and configure it.
2. Paste you server data in main.py "connection" (9 line).
3. Add table in psql with name "clang" and with rows "bug_group, bug_type, file, function, line, path_lengt"
4. Run the main.py

Problems issues? Write me on my email: yyyyxxxx@bk.ru

Парсер выявленых ошибок кода утилитой scan-build в базу данных PostgreSQL
Парсит ошибки кода из html страницы в базу данных
1. Установите psql и настройте его
2. Вставьте данные вашего сервера в main.py в переменную connection (9 строка
3. Добавьте таблицу с именем clang со столбцами "bug_group, bug_type, file, function, line, path_lengt" в Вашу БД.
4. Запустите main.py

По вопросам прошу обращаться на почту yyyyxxxx@bk.ru
