import time

t0 = time.time()



t1 = time.time()
print(t1 - t0)

dict = {0:(0,1), 1:(1,1)}
def fibonacci_rec_cnt(n: int):
    if n in dict:
        return dict[n], 1
    else:
        x1, cnt1 = fibonacci_rec_cnt(n - 1)
        x2, cnt2 = fibonacci_rec_cnt(n - 2)
        dict[n] = (x1 + x2, cnt1 + cnt2 + 1)
        return dict[n]

print(fibonacci_rec_cnt(5), dict)