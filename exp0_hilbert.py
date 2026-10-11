import numpy as np
from scipy.linalg import hilbert

for n in [5, 8, 11, 14]:
    A = hilbert(n)                      # 著名的病态矩阵
    x_exact = np.ones(n)                # 人为设定的真解
    b = A @ x_exact                     # 反推右端项
    x_num = np.linalg.solve(A, b)       # 调库求解
    cond = np.linalg.cond(A)            # 条件数
    err = np.linalg.norm(x_num - x_exact) / np.linalg.norm(x_exact)
    print(f"n={n:2d}  条件数={cond:.2e}  解的相对误差={err:.2e}")