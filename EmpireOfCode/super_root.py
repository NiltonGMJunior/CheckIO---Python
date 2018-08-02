
def super_root(number):

    root = 1
    eps = 0.001

    while True:
        if abs(root**root - number) <= eps:
            return root
        else:
            root = abs(root**root - number)/2

    return root

def main():
    number = 4
    print("I'm running!")
    print(super_root(number))
    
    return

if __name__ == "__main__":
    main()