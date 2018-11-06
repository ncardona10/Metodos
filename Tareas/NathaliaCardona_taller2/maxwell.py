import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate


k = 1.38064852E-23
C = np.sqrt(2.0/np.pi)
u = 1.660539040E-27
mNe = 20.1797 * u
mHe = 4.002602 * u
mAr = 39.9488 * u
masas = [mNe, mHe, mAr]


def prob(T, M, v):
    return C * v ** 2*np.exp(-0.5 * v**2/sigma(T, M)**2)/(sigma(T, M)**3)


def sigma(T, M):
    return np.sqrt(k * T / M)


vs = np.linspace(0, 9999, 10000)


Ts = np.linspace(100, 1000, 10000)
ms = []
for M in masas:
    maxvs = []
    for T in Ts:
        ys = prob(T, M, vs)
        maxv = np.max(ys)
        maxvs.append(vs[ys == maxv][0])
    ms.append(maxvs)

plt.plot(Ts, ms[0], label="Neon")
plt.plot(Ts, ms[1], label="Helium")
plt.plot(Ts, ms[2], label="Argon")
plt.legend()
plt.xlabel(r"$Temperature\ (K)$")
plt.ylabel(r"$v_{max}\ (ms^{-1})$")
plt.savefig("pico.png")
plt.close()


def funcInt(T, M, phi):
    return C * np.exp(-0.5/(phi**2 * sigma(T, M)**2))/(phi**4 * sigma(T, M)**3)


ms = []
vs = np.linspace(0.0000000000001, 1.0/300.0, 1000)
ms1 = []
for M in masas:
    fracs = []
    for T in Ts:
        part = integrate.simps(funcInt(T, M, vs), vs)
        fracs.append(part)
    ms1.append(fracs)


plt.plot(Ts, ms1[0], label="Neon")
plt.plot(Ts, ms1[1], label="Helium")
plt.plot(Ts, ms1[2], label="Argon")
plt.legend()
plt.xlabel(r"$Temperature\ (K)$")
plt.ylabel(r"$f_{300}$")
plt.savefig("fraccion.png")
plt.close()
