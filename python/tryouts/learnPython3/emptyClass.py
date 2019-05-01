'''
This program explains the usage of pass statement in python
'''


class EmptyClass:
    pass


def main():
    # no-op loop
    for i in range(0, 10):
        pass

    # object that can have attributes dynamically added
    ins = EmptyClass()
    ins.attr1 = "attr1"
    ins.attr2 = "attr2"
    print(ins.attr1)


main()
