#!/usr/bin/python3

def pascal_triangle(n):
    arr = []
    for i in range(n):
        col = [1] * (i + 1)
        for j in range(1, i):
            col[j]=(arr[i-1][j-1]+arr[i-1][j])
        arr.append(col)
    return arr

if __name__ == '__main__':
    print(pascal_triangle(5))

