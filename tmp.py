class Foo(object):
    @staticmethod
    def bar():
        return 'bar'

    @staticmethod
    def __call__():
        return '__call__'

print (Foo.bar())
print (Foo())

