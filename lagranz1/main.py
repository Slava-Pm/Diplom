import math
import matplotlib.pyplot as plt

def lagrange_interpolation(y, x, x_interp):

    x0, x1, x2, x3 = x
    y0, y1, y2, y3 = y

    L0 = ((x_interp - x1) * (x_interp - x2) * (x_interp - x3)) / ((x0 - x1) * (x0 - x2) * (x0 - x3))
    L1 = ((x_interp - x0) * (x_interp - x2) * (x_interp - x3)) / ((x1 - x0) * (x1 - x2) * (x1 - x3))
    L2 = ((x_interp - x0) * (x_interp - x1) * (x_interp - x3)) / ((x2 - x0) * (x2 - x1) * (x2 - x3))
    L3 = ((x_interp - x0) * (x_interp - x1) * (x_interp - x2)) / ((x3 - x0) * (x3 - x1) * (x3 - x2))
    interpolated_y = y0 * L0 + y1 * L1 + y2 * L2 + y3 * L3

    return interpolated_y

def sinys (A, Fn, Fd, fi, t):
    Y = [A * math.sin(2 * math.pi * (Fn / Fd) * i + fi) for i in t]
    return (Y)
n = 21
t = list(range(n))
A = 1
t_inter = []
Fn = 1
Fd = 10
fi = 0

interpolated_point = []
dif = []
Y = sinys(A, Fn, Fd, fi, t)
#plt.plot(t, Y)
#plt.show()


for i in range(n-3):
    interpolated_point.append(lagrange_interpolation(Y[i:4 + i], [i, i+1, i+2, i+3], i+0.5))
    t_inter.append(i + 0.5)
t_inter.append(n-3 + 0.5)
t_inter.append(n-2 + 0.5)
interpolated_point.append(lagrange_interpolation(Y[n-4:n],[n-4,n-3,n-2,n-1], n-3 + 0.5))
interpolated_point.append(lagrange_interpolation(Y[n-4:n],[n-4,n-3,n-2,n-1], n-2 + 0.5))
point = sinys(A, Fn, Fd, fi, t_inter)
for i in range(n-3):
    dif.append (interpolated_point[i] - point[i])
plt.plot(t_inter, interpolated_point, 'ro')
plt.plot(Y, 'g')

plt.show()

M = sum(dif) / len(dif)
print('Mатематическое ожидание = ', M)
D = sum((x - M) ** 2 for x in dif) / len(dif)
print('Дисперсия  = ', D)

sigma = D ** 0.5
print('Среднее квадратичное = ', D)
Y = Y[:-2]

P_sig = (1 / len(Y)) * sum(y ** 2 for y in Y)
P_noise = (1 / len(dif)) * sum(d ** 2 for d in dif)

SNR = P_sig / P_noise
SNR_db = math.floor(10 * math.log10(SNR))
print('SNR_db = ', SNR_db)
