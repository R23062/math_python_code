import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def f(x):
    return x**2

a, b = 0, 1
n = 10  # 可視化用に分割数をあえて少なくします

# --- 可視化用の処理 ---
x = np.linspace(a, b, 100)
y = f(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, 'r', weight='bold', label='f(x) = x^2') # 関数

# 台形を塗りつぶす
x_trap = np.linspace(a, b, n + 1)
y_trap = f(x_trap)
plt.fill_between(x_trap, y_trap, alpha=0.3, color='blue', step=None, label='Trapezoidal Rule')
plt.xticks(x_trap)
plt.title("Visualization of Trapezoidal Rule")
plt.legend()
plt.grid(True)
plt.show() # ここでグラフが表示されます

# --- 計算（前回と同じ） ---
ans_lib, _ = integrate.quad(f, a, b)
print(f"ライブラリの積分結果: {ans_lib}")
