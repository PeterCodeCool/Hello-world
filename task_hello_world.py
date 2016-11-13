import sys

def main():
    
    global name
    name = "World"
    if len(sys.argv) == 2:
        name = sys.argv[1]

def write():
    print("Hello " + name + "!")


main()
write()

