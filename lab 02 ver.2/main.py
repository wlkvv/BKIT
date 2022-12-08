from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import cowsay
def main():

    r = Rectangle("синего", 3, 2)
    c = Circle("зеленого", 5)
    s = Square("красного", 5)
    cowsay.meow(str(r) + '\n' + str(c) + '\n' + str(s))

if __name__ == "__main__":
    main()