import sqlite3

# メモリ上に展開する
conn = sqlite3.connect(':memory:')

curs = conn.cursor()

curs.close()
conn.close()
