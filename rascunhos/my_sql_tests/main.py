import sqlite3

my_connection = sqlite3.connect('test_db_1.sqlite')

con_cursor = my_connection.cursor()

res = con_cursor.execute("SELECT name FROM sqlite_master WHERE name='kid'")
if res.fetchone is None: con_cursor.execute('CREATE TABLE kid(nome, apt, responsavel)')
con_cursor.execute("""INSERT INTO kid VALUES
                ('Amanda', '10', 'Gustavo')""")


my_connection.commit()