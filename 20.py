"""
定义一个类，该类具有一个类参数和一个相同的实例参数
"""


class Person(object):
    name = "haha"

    def __init__(self, name=None):
        self.name = name


jerry = Person("Jerrfy")
print("%s name is %s" % (Person.name, jerry.name))

print("-------")

# 两种方式
nicio = Person()
nicio.name = "fsdf"
print("%s name is %s" % (Person.name, nicio.name))