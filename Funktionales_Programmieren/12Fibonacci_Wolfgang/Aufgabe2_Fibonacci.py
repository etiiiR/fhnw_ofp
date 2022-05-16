cnt = 0
def fibonacci_rec(n: int) -> int:
    global cnt
    cnt += 1
    return n if n <= 1 else fibonacci_rec(n - 1) + fibonacci_rec(n - 2)


def fibonacci_rec_cnt(n: int):
    if n <= 1:
        return n, 1
    else:
        x1, cnt1 = fibonacci_rec_cnt(n - 1)
        x2, cnt2 = fibonacci_rec_cnt(n - 2)
        return x1 + x2, cnt1 + cnt2 + 1

print(fibonacci_rec(3), cnt)
print(fibonacci_rec_cnt(3))
