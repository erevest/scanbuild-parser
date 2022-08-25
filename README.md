# clang_db_parser
Parse code issues from clang scan-build html page to psql database. The code is very human

1. Install psql and configure it.
2. Paste you server data in main.py "connection" (9 line).
3. Add table in psql with name "clang" and with rows "bug_group, bug_type, file, function, line, path_lengt"
4. Run the main.py

Парсер выявленых ошибок кода утилитой scan-build в базу данных PostgreSQL
Парсит ошибки кода из html страницы в базу данных
