import pymysql

def test_mysql():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='mysql', charset='UTF8')
    cur = conn.cursor()
    query = "SELECT Host,User FROM user"
    cur.execute(query)
    for row in cur:
        print(row)
    cur.close()
    conn.close()

if __name__ == "__main__":
    test_mysql()
    test_mysql()