def main():
    m = int(input("행 수를 입력하세요: "))
    n = int(input("열 수를 입력하세요: "))

    matrix = []

    for i in range(m):
        row = []
        for j in range(n):
            element = int(input(f"{i+1}행 {j+1}열의 원소를 입력하세요: "))
            row.append(element)
        matrix.append(row)

    print("입력한 행렬:")
    for row in matrix:
        print(" ".join(map(str, row)))

    transposed = [[matrix[j][i] for j in range(m)] for i in range(n)]

    print("전치행렬:")
    for row in transposed:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()