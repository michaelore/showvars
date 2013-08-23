import showvars

sv = showvars.ShowVars(locals())

def distance(t):
    v = 5
    a = 1
    return v*t+0.5*a*t**2

data = []

for t in range(10):
    dist = distance(t)
    data.append(dist)

sv.showvars(locals())
