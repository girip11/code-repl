print("This is a simple python program")
print(3+4)
print('Hello world')
x = 10
print('x =', x)

x = eval(input('Enter input'))
if x >= 100:
    print(x, 'greater than or equal to 100')
else:
    print(x, 'is less than 100')

for c in "abc":
    # type is str
    print(type(c))
    print(c)

# example of variable arguments


def varargsMethod(arg1, *args):
    print(arg1)
    for a in args:
        print(a)


def main():
    varargsMethod("hello")
    varargsMethod("hello", 1, 2, 3, 4)


main()
