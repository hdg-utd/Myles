import sqlite3

class AirlineDatabase:

    #def create_table(conn, c):
        #c.execute('CREATE TABLE IF NOT EXISTS storeNames(store_id INTEGER PRIMARY KEY AUTOINCREMENT, store_name TEXT NOT NULL, domain TEXT NOT NULL)')
        #c.execute('CREATE TABLE IF NOT EXISTS pointsData(points_id INTEGER PRIMARY KEY, store_id INTEGER, airline_id INTEGER, afilliate_link TEXT, points INTEGER, FOREIGN KEY (store_id) REFERENCES storeNames(store_id))')

    def check_domain(conn, c, storename):
        try:
            sql = 'SELECT domain FROM storeNames WHERE store_name="%s"' % (storename)
            c.execute(sql)
            store = c.fetchall()
            return store[0][0]
        except:
            return ""

    def insert_domain(conn, c, store_name, domain):
        c.execute("INSERT INTO storeNames (store_name, domain) VALUES (?, ?)", (store_name, domain))
        conn.commit()

    def close_table(conn, c):
        c.close()
        conn.close()
