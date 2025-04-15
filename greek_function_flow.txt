def alpha(x, y):
    if x > y:
        return beta(x - y, y)
    elif x < y:
        return gamma(x, y - x)
    else:
        return delta(x, y)

def beta(a, b):
    if a % 2 == 0:
        return epsilon(a // 2, b)
    else:
        return zeta(a, b * 2)

def gamma(p, q):
    if p < 10:
        return eta(p + q, q)
    else:
        return theta(p, q + 5)

def delta(m, n):
    return lambda_func(m + n)

def epsilon(j, k):
    if j < k:
        return mu(j * 2, k)
    else:
        return nu(j, k * 2)

def zeta(r, s):
    return xi(r + s, s - r)

def eta(u, v):
    if u > 20:
        return omicron(u - 10, v)
    else:
        return pi(u + v, v)

def theta(c, d):
    return rho(c * d, d)

def lambda_func(z):
    if z % 3 == 0:
        return sigma(z // 3)
    else:
        return tau(z + 1)

def mu(f, g):
    return upsilon(f + g)

def nu(h, i):
    if h > 50:
        return phi(h - 25, i)
    else:
        return chi(h, i + 10)

def xi(w, x):
    return psi(w * x)

def omicron(aa, bb):
    return omega(aa + bb, bb)

def pi(cc, dd):
    if cc < dd:
        return alpha(cc, dd)
    else:
        return beta(cc, dd)

def rho(ee, ff):
    return gamma(ee % ff, ff)

def sigma(gg):
    return gg * 2

def tau(hh):
    return hh - 5

def upsilon(ii):
    return ii ** 2

def phi(jj, kk):
    return jj + kk

def chi(ll, mm):
    return ll * mm

def psi(nn):
    return nn // 2

def omega(oo, pp):
    return oo - pp

# Test examples
print(alpha(15, 10))
print(alpha(8, 12))
print(alpha(20, 20))
print(mu('hello', 'world'))
