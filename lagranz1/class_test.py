import math
from statistics import mean
import matplotlib.pyplot as plt
class LagrangeInterpolation:
    def __init__(self, y, x):
        self.y = y
        self.x = x

    def interpolate(self, x_interp):
        L = []
        for i in range(len(self.y)):
            L.append(self.y[i])
            for j in range(len(self.x)):
                if (i != j):
                    L[i] = L[i] * (x_interp - self.x[j]) / (self.x[i] - self.x[j])
        y_interp = sum(L)
        return y_interp

def sinys(A, Fn, Fd, fi, t):
    Y = [A * math.sin(2 * math.pi * (Fn / Fd) * i + fi) for i in t]
    return Y

n = 21
t = list(range(n))
A = 1
Fn = 1
Fd = 10
fi = 0
Y = sinys(A, Fn, Fd, fi, t)
parametr = 4
fi_srednee = []
fi_h = []
file = open('test_2.txt', 'w')
el = [i/10 for i in range(1,10)]
for h in el:
    t_inter = []
    interpolated_point = []
    dif_otnos = []
    dif = []
    lagrange_interpolator = LagrangeInterpolation(Y, t)
    for i in range(n - parametr + 1):
        x = [i + k for k in range(parametr)]
        interpolated_point.append(lagrange_interpolator.interpolate(i + h))
        t_inter.append(i + h)
    for i in range(parametr - 1):
        interpolated_point.append(lagrange_interpolator.interpolate(n - parametr + i + h))
        t_inter.append(n - parametr + i + h)

    point = sinys(A, Fn, Fd, fi, t_inter)
    for i in range(n - parametr + 1):
        dif.append(abs(interpolated_point[i] - point[i]))
        dif_otnos.append(dif[i] / abs(point[i]))
    srednee = mean(dif_otnos)
    print(srednee)
    stroka = ' '.join([str(elem) for elem in dif_otnos])
    slova = stroka.split()
    for slovo in slova:
        file.write(slovo + '\n')
    file.write('\n')
    file.write('Среднее значение: ' + str(srednee) + '\n' + '\n')
    fi_h.append(h)
    fi_srednee.append(srednee)
file.close()

plt.title('Зависимость изменения шага на погрешность')
plt.ylabel('Погрешность')
plt.xlabel('Шаг')
plt.plot(fi_h, fi_srednee)
plt.show()
# print(max_diff)
# print(dif)
# print(dif_otnos)
# plt.plot(t_inter, interpolated_point, 'ro')
# plt.plot(Y, 'g')

plt.show()

# M = sum(dif) / len(dif)
# print('Mатематическое ожидание = ', M)
# D = sum((x - M) ** 2 for x in dif) / len(dif)
# print('Дисперсия  = ', D)
#
# sigma = D ** 0.5
# print('Среднее квадратичное = ', D)
# Y = Y[:-2]
#
# P_sig = (1 / len(Y)) * sum(y ** 2 for y in Y)
# P_noise = (1 / len(dif)) * sum(d ** 2 for d in dif)
#
# SNR = P_sig / P_noise
# SNR_db = math.floor(10 * math.log10(SNR))
# print('SNR_db = ', SNR_db)
