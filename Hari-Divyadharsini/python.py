#This is my initial file.
def star_pattern1(n):
    for i in range(1, n+1):
        for j in range(1, i + 1):
            print("* ", end="")
        print()
n = int(input("Enter number of rows:"))
star_pattern1(n)