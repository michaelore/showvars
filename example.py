import showvars

sv = showvars.ShowVars(locals())
sv.ban('sv')
sv.ban('t')

def distance(t):
    v = 5
    a = 1
    return v*t+0.5*a*t**2

data = []

for t in range(10):
    dist = distance(t)
    data.append(dist)

print('Call #1:')
sv.showvars(locals())

for t in range(10):
    data[t] = 2*data[t]

toomuchdata = range(10000)
sv.hide('toomuchdata', toomuchdata)

print('Call #2:')
sv.showvars(locals())

lessdata = range(20)

print('Call #3:')
sv.showvars(locals())
