import psycopg2



conn_string = "dbname=amazon_scrapping user=postgres password=postgres host=db port=5432"

list_of_data = []


def update_data(id, price, new_price, highest_price):
    conn = psycopg2.connect(conn_string)
    cur = conn.cursor()
    try:
        if price > new_price:
            cur.execute("UPDATE products SET price = %sWHERE id = %s", (new_price, id))
        elif new_price > highest_price:
            cur.execute("UPDATE products SET highest_price = %s WHERE id = %s", (new_price, id))
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()


def select_data():

    conn = psycopg2.connect(conn_string)
    cur = conn.cursor()
    cur.execute("SELECT * FROM products")
    rows = cur.fetchall()
    for row in rows:
        list_of_data.append(row)
    return list_of_data
    cur.close()
    conn.close()


def insert_data(url):
    import price_logic
    conn = psycopg2.connect(conn_string)
    cur = conn.cursor()
    cur.execute("INSERT INTO products(url,current_price,lowest_price,highest_price) VALUES(%s,%s,%s,%s)",
                (url, 0, 0, 0))
    conn.commit()
    price_logic.update_price()
    cur.close()
    conn.close()


def create_table():
    conn = psycopg2.connect(conn_string)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS products(id SERIAL PRIMARY KEY, url TEXT, current_price INTEGER, "
                "lowest_price INTEGER, highest_price INTEGER, link TEXT)")
    conn.commit()
