class Sample:
    '''
        This is a sample class
    '''

    # class variables shared by all instances may cause undesirable side effects
    __privateClassVar = "Private"
    publicClassVar = "Public"

    def __init__(self, msg):
        self.__msg = msg

    # convention is always to pass the first parameter named self. we can use any name too, but self is recommended. linters might throw this as error when the first parameter is not named as self 'no-self-argument'
    def getMessage(this):
        return this.__msg

    def getPrivateClassVar(self):
        return Sample.__privateClassVar
        # or return self.__privateClassVar
        # but assigning to self.__privateClassVar creates an attribute inside the object with same name and not the class variable.


def main():
    print(Sample("Hello world").getMessage())
    obj = Sample("Object")
    obj2 = Sample("Object2")
    # stores ref to method object
    # method can be invoked later
    objMethod = obj.getMessage

    # printing the class variables
    print(obj.publicClassVar)
    print(obj2.publicClassVar)
    print(obj.getPrivateClassVar())

    print(type(obj.getMessage))
    print(type(main))
    print(type(objMethod))
    print(objMethod())
    print(Sample.getMessage(obj))


main()
