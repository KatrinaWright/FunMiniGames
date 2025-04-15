
def start(x, y):
    if len(str(x)) > len(str(y)):
        return path_a(x + y, x)
    elif len(str(x)) < len(str(y)):
        return path_b(y, x + y)
    else:
        return path_c(x, y)

def path_a(a, b):
    if len(str(a)) % 2 == 0:
        return path_d(a + a, b)
    else:
        return path_e(b, a + b)

def path_b(p, q):
    if len(str(p)) < 10:
        return path_f(p + q, q)
    else:
        return path_g(q, p)

def path_c(m, n):
    return path_h(m + n + m)

def path_d(j, k):
    if len(str(j)) < len(str(k)):
        return path_i(j + j, k)
    else:
        return path_j(k, j + k)

def path_e(r, s):
    return path_k(r + s, s + r)

def path_f(u, v):
    if len(str(u + v)) > 20:
        return path_l(v, u + u)
    else:
        return path_m(u + v, v)

def path_g(c, d):
    if len(str(c)) > len(str(d)):
        return path_n(c, d)
    else:
        return path_f(c + d, d)

def path_h(z):
    if len(str(z)) % 3 == 0:
        return path_o(z + z + z)
    else:
        return path_p(z + z)

def path_i(f, g):
    return path_q(g + f)

def path_j(h, i):
    if len(str(h + i)) > 50:
        return path_r(i, h + h)
    else:
        return path_s(h, i + i)

def path_k(w, x):
    return path_t(w + x)

def path_l(aa, bb):
    return path_u(aa + bb, bb)

def path_m(cc, dd):
    if len(str(cc)) < len(str(dd)):
        return start(cc, dd)
    else:
        return path_a(cc, dd)

def path_n(ee, ff):
    if len(str(ee)) > 20:
        return path_o(ee + ff)
    else:
        return path_b(ee, ff)

def path_o(gg):
    return gg + gg

def path_p(hh):
    return hh + hh + hh + hh + hh

def path_q(ii):
    return ii + ii

def path_r(jj, kk):
    return jj + kk

def path_s(ll, mm):
    return ll + mm

def path_t(nn):
    return nn + nn

def path_u(oo, pp):
    return oo + pp

# Test examples
print(start(15, 10))
print(start(8, 12))
print(start(20, 20))
print(start("hello", "world"))
print(start("short", "longer string"))
print(start("same", "size"))
print(start("a very long string", "short"))
print(start("short", "a very long string"))
print(start("medium length", "also medium"))