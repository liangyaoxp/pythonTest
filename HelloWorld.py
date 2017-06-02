import pymysql
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='mysql', charset='UTF8')
cur = conn.cursor()
query = "SELECT Host,User FROM user"
cur.execute(query)
for i in cur:
    print(i)
cur.close()
conn.close()