import pymysql


class Animal(object):
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs

    def print_legs(self, animal):
        animal.print_legs()


class Dog(Animal):
    def print_legs(self):
        print("Dog has %d legs!" % self.legs)


class Chicken(Animal):
    def print_legs(self):
        print("Chicken has %d legs!" % self.legs)


def test_mysql():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='mysql', charset='UTF8')
    cur = conn.cursor()
    query = "SELECT Host,User FROM user"
    cur.execute(query)
    for row in cur:
        print(row)
    cur.close()
    conn.close()


def test_class():
    animal = Animal("test", 2)
    dog = Dog("ketty", 4)
    chicken = Chicken("gogo", 2)

    # 编译多态
    dog.print_legs()
    chicken.print_legs()

    # 运行时多态
    animal.print_legs(dog)
    animal.print_legs(chicken)

if __name__ == "__main__":
    test_class()