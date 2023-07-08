
def search(x):

    if x >= 0:
        return has[x][0] == 1
    x = abs(x)
    return has[x][1] == 1


def insert(a, n):
    for i in range(0, n):
        if a[i] >= 0:
            has[a[i]][0] = 1
        else:
            has[abs(a[i])][1] = 1


# *Emporikotmima1*
if __name__ == "__main__":

    a = [-1, 9, -5, -8, -5, -2]
    n = len(a)

    MAX = 10

    has = [[0 for i in range(2)] for j in range(MAX + 1)]

    insert(a, n)

    x = -5
    if search(x) == True:
        print("Present")
    else:
        print("Not Present")

    print(has)
