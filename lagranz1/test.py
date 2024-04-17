import math
import matplotlib.pyplot as plt

def lagrange(y, x, x_interp):
    L = []
    for i in range(len(y)):
        L.append(y[i])
        for j in range(len(x)):
            if (i != j):
                L[i] = L[i] * (x_interp - x[j]) / (x[i] - x[j])
    y_interp = sum(L)
    return y_interp

def sinys (A, Fn, Fd, fi, t):
    Y = [A * math.sin(2 * math.pi * (Fn / Fd) * i + fi) for i in t]
    return (Y)
n = 21
t = list(range(n))
A = 1
Fn = 1
Fd = 10
fi = 0
h = 0.5
Y = sinys(A, Fn, Fd, fi, t)
parametr = 10
fi_parametr = []
fi_max = []
file = open('test.txt', 'w')
for parametr in range(2, 10):
    t_inter = []
    interpolated_point = []
    dif_otnos = []
    dif = []
    for i in range(n-parametr + 1):
        x = [i + k for k in range(parametr)]
        interpolated_point.append(lagrange(Y[i:parametr + i], x, i+h))
        t_inter.append(i + h)
    for i in range(parametr - 1):
        interpolated_point.append(lagrange(Y[n-parametr:n], x, n - parametr + i + h))
        t_inter.append(n - parametr + i + h)

    point = sinys(A, Fn, Fd, fi, t_inter)
    # Погрешность абсолютная и относительная
    for i in range(n-parametr + 1):
        dif.append (abs(interpolated_point[i] - point[i]))
        dif_otnos.append(dif[i]/abs(point[i]))
    max_diff = max(dif_otnos)
    fi_max.append(max_diff)
    fi_parametr.append(parametr)
    print(max_diff)
plt.title('Зависимость')
plt.ylabel('Погрешность')
plt.xlabel('Порядок интерполяции')
plt.plot(fi_parametr, fi_max)
plt.show()
plt.savefig('test.png')
#запись в файл относительной погрешности
stroka = ' '.join([str(elem) for elem in fi_max] )
slova = stroka.split()
for slovo in slova:
    file.write(slovo + '\n')
file.close()

# print(max_diff)
# print(dif)
# print(dif_otnos)
# plt.plot(t_inter, interpolated_point, 'ro')
# plt.plot(Y, 'g')


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