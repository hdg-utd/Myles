import sqlite3

class AirlineDatabase:

    def create_table(conn, c):
        c.execute('CREATE TABLE IF NOT EXISTS milesForStores(storename TEXT PRIMARY KEY, domain TEXT)')

    def test_data_entry(conn, c):
        c.execute("INSERT INTO milesForStores VALUES('Staples', 'www.staple.com')")
        conn.commit()

    def check_data(conn, c, storename):
        try:
            sql = 'SELECT domain FROM milesForStores WHERE storename="%s"' % (storename)
            c.execute(sql)
            store = c.fetchall()
            return store[0][0]
        except:
            return ""

    def insert_data(conn, c, storename, url):
        c.execute("INSERT INTO milesForStores (storename, domain) VALUES (?, ?)", (storename, url))
        conn.commit()

    def close_table(conn, c):
        c.close()
        conn.close()
