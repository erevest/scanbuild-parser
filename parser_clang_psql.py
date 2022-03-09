import psycopg2
from psycopg2 import Error
import requests
from bs4 import BeautifulSoup
import pandas as pd

try:
    # Подключение к существующей базе данных
    connection = psycopg2.connect(user="postgres_user",
                                  # пароль, который указали при установке PostgreSQL
                                  password="password",
                                  host="localhost",
                                  port="5432",
                                  database="my_postgres_db")

    # Курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    # Распечатать сведения о PostgreSQL
    print("Информация о сервере PostgreSQL")
    print(connection.get_dsn_parameters(), "\n")
    # Выполнение SQL-запроса
    # Вставка в БД ------------------------------->
    #cursor.execute(insert_query)
    connection.commit()
    cursor.execute("select * from clang;")
    # Получить результат
    record = cursor.fetchall()
    print("Вы подключены к - ", record, "\n")
  

    url = "http://127.0.0.1:8181/"
    response = requests.get(url)
    bs = BeautifulSoup(response.text, "lxml")
    #https://vc.ru/newtechaudit/109368-web-parsing-osnovy-na-python

    start = False
    header_finished = False
    headers = []
    cols = []
    rows = []
    for el in bs.find_all('td'): 
            if el.text == 'Bug Group':
                    start = True
            if start == True and header_finished == False:
                    if len(headers) < 8:
                            headers.append(el.text)
                    else:
                            header_finished = True
            elif start == True:
                    if len(cols) < 8:
                            cols.append(el.text)
                    else:
                            rows.append(cols)
                            cols = []
    for one_row in rows:
                print(one_row[0]+'\t'+one_row[1]+'\t'+one_row[2]+'\t'+one_row[3]+'\t'+one_row[4]+'\t'+one_row[5]+'\t')
                one_row = [w.replace("'", "''") for w in one_row] #удаляет кавычки
                insert_query = "INSERT INTO clang (bug_group, bug_type, file, function, line, path_lengt) VALUES ( '{}', '{}', '{}','{}', '{}', '{}');".format(one_row[0], one_row[1], one_row[2], one_row[3], str(one_row[4]), str(one_row[5])) #работает  
                cursor.execute(insert_query)
                connection.commit()
        #print(one_row[0])

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")