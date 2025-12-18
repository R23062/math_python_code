import numpy as np
import time
from scipy import integrate

# 1. 積分する関数
def f(x):
    return x**2

a, b = 0, 1  # 積分範囲 [0, 1]
n = 100000   # 分割数

# 2. 基本的な文法（for文）による実装
start_basic = time.time()
h = (b - a) / n
s = 0.5 * (f(a) + f(b))
for i in range(1, n):
    s += f(a + i * h)
ans_basic = s * h
end_basic = time.time()

# 3. 数値計算ライブラリ（SciPy）による実装
start_lib = time.time()
ans_lib, error = integrate.quad(f, a, b)
end_lib = time.time()

print(f"基本実装の結果: {ans_basic}, 実行時間: {end_basic - start_basic:.6f}s")
print(f"ライブラリの結果: {ans_lib}, 実行時間: {end_lib - start_lib:.6f}s")
