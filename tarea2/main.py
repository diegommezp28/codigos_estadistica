from scipy.stats import uniform, binom, norm
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(seed=10)
Y_list = []
Z_list = []
for i in range(0, 1000):
    muestreo = uniform.rvs(loc=0, scale=1, size=100)
    media_muestral = np.mean(muestreo)
    Y_n = (101 / 100) * np.amax(muestreo)
    Z_n = 2 * media_muestral

    Y_list.append(Y_n)
    Z_list.append(Z_n)
Y_array = np.array(Y_list)
Z_array = np.array(Z_list)

mu_Y = np.mean(Y_array)
mu_Z = np.mean(Z_array)

fig = plt.figure()

plot_y = plt.hist(Y_array, 30, alpha=0.1, density=True, color='b')
plt.axvline(x=np.mean(Y_array), color='b', lw=1, label=f' $Y_n$ sample $\mu = {round(mu_Y, 6)}$')
plot_Z = plt.hist(Z_array, 30, alpha=0.1, color='r', density=True)
plt.axvline(x=np.mean(Z_array), color='r', lw=1, label=f'$Z_n$ sample $\mu = {round(mu_Z, 6)}$')

plt.legend()
plt.title('100 Samples')

plt.show()

fig.savefig('100 SAMPLES.png', bbox_inches='tight')
