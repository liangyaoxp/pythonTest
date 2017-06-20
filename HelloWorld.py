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

    print(dir(dog))


def test_len():
    print("adsfasdfasdf00".__len__())


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


def test_getattr():
    b = MyObject()
    print(dir(b))

    print(hasattr(b, 'x'))
    print(getattr(b, 'x'))
    # print(getattr(b, 'z'))
    print(hasattr(b, 'y'))
    setattr(b, "x", 10)
    print(getattr(b, 'x'))

    setattr(b, "y", 9)
    print(hasattr(b, "y"))
    print(getattr(b, "y"))
    print(b.y)

    print(getattr(b, "power"))
    f = getattr(b, "power")
    print(f())


class Student(object):
    # __slots__ = ("name", "age", "set_age", "_score")

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be integer!')
        if value < 0 or value > 100:
            raise ValueError('score must in [0, 100]!')
        self._score = value


def test_band():
    from types import MethodType

    s = Student()
    s.name = "liangyao"
    print(s.name)

    def set_age(self, age):
        self.age = age

    s.set_age = MethodType(set_age, s)
    s.set_age(25)
    print(s.age)
    s.score(100)
    print(s.score)

    # def set_score(self, score):
    #     self.score = score
    #
    # Student.set_score = set_score
    # s.set_score(100)
    # print(s.score)


class Chain(object):

    def __init__(self, path='GET '):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __call__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


def test__getattr__():
    a = Chain().users('michael').age('123').repos
    print(a)
    print(callable(Chain))


if __name__ == "__main__":
    test__getattr__()
