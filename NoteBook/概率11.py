import numpy as np #数组包
from scipy import stats #统计计算包的统计模块
import matplotlib.pyplot as plt #绘图包

# --------分布参数---------
lam = 5 # 每天卖的馒头均值
# -----------------------------
X = np.arange(0, 21, 1)
p_list = stats.poisson.pmf(X,lam)

plt.plot(X, p_list, linestyle='None', marker='o')
plt.vlines(X, 0, p_list)
plt.xticks(np.arange(0, 21, 1))
plt.xlabel('Random Variable: X, X(Experimental Result) = the num of things happen in time interval T')
plt.ylabel('Probability')
plt.title('poisson, lambda:{}'.format(lam))

plt.show()
