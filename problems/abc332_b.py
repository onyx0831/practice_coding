k, g_limit, m_limit = map(int, input().split())
g = 0
m = 0
for i in range(k):
    if g == g_limit:
        g = 0
    elif m == 0:
        m = m_limit
    else:
        # mがgの限界より多い場合
        if (g_limit - g) <= m:
            m -= (g_limit - g)
            g = g_limit
        # mがgの限界より少ない場合
        else:
            g += m
            m = 0
print(f'{g} {m}')
