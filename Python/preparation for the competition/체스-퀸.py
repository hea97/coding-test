def n_queens(i, col):
    n = len(col) - 1
    if promising(i, col):
        if i == n:
            print(col[1: n + 1])
        else:
            for j in range(1, n + 1):
                col[i + 1] = j
                n_queens(i + 1, col)

def promising(i, col):
    k = 1
    flag = True
    while k < i and flag:
        if col[i] == col[k] or abs(col[i] - col[k]) == (i - k):
            flag = False
        k += 1
    return flag

def main():
    while True:
        try:
            n = int(input("체스판의 크기 N을 입력하세요: "))
            if n < 1:
                raise ValueError("N은 1 이상의 정수여야 합니다.")
            break
        except ValueError as e:
            print(f"잘못된 입력입니다. 다시 시도하세요. ({e})")
    
    col = [0] * (n + 1)
    n_queens(0, col)

if __name__ == "__main__":
    main()

    # 선생님께서 보내주신 Python 예시 활용하여 작성.