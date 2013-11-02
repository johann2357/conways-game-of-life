from matrix import Matrix

def main():
    r = 66
    c = 66
    s = 7
    test = Matrix(rows=r, columns=c, side=s)
    test.random_matrix()
    test.run()

if __name__ == "__main__":
    main()
