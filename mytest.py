class People(object):
    name = "请叫我类变量"

    def __init__(self, name):
        self.name = name

    @property  # 把eat方法变为静态属性
    def eat(self):
        print("%s is eating" % self.name)


d = People("cc")
d.eat
