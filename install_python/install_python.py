import os
folder_name = "saved"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

with open("saved/Hello.txt", "w") as f:
    f.write("Hello World!\n")
    f.write("Hello World!2\n")
    f.write("Hello World!3\n")

with open("saved/Hello.txt", "r") as f:
    for i in range(3):
        s = f.readline().rstrip()
        print(s)

def my_func(*args):
    print(f"a 에는 {args}가 들어가있다. 타입은 {type(args)} 라고 한다.")

my_func(1,2)

def my_func(**kwargs):
    print(f"k 에는 {kwargs}가 들어가있다. 타입은 {type(kwargs)} 라고 한다.")

my_func(name="혁펜", age=100, address="한국")

print((lambda x: x + 10)(10))

f = lambda a, b: a + b
print(list(map(f, [1, 2, 3], [2, 3, 4])))

a = [1, 2, 3]
a_it = iter(a)
print(next(a_it))
print(next(a_it))
print(next(a_it))