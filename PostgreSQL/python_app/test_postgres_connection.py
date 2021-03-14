import psycopg2

def get_postgis_connection():
    # logging.info("Obtaining DB connection Object")
    print("Obtaining DB connection Object")
    conn = psycopg2.connect(host="localhost",
                            dbname="postgres",
                            user="postgres",
                            password="postgres")
    conn.autocommit = True
    return conn


if __name__ == '__main__':
    print("Starting process...")
    try:
        conn = get_postgis_connection()
        print("Got the connection variable")
        cur = conn.cursor()
        query = "SELECT * FROM products;"
        print("Executing the query - " + query)
        cur.execute(query)
        print("Fetching the results")
        records = cur.fetchall()
        print("Print each row and it's columns values")
        print("Print each row and it's columns values")
        for row in records:
            print("product_no = ", row[0], )
            print("name = ", row[1])
            print("price  = ", str(row[2]), "\n")
            msg = "product_no = " + str(row[0]) + '. name = ' + str(row[1]) + '. price = ' + str(row[2])
            print("Details --> " + msg)
    except Exception as e:
        err_msg = 'ERROR [test_postgres_connection] : ' + str(e)
        print(str(err_msg))
